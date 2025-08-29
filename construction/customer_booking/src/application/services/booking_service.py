from datetime import datetime
from ...domain.entities.booking import Booking
from ...domain.entities.booking_aggregate import BookingAggregate
from ...domain.entities.payment import Payment, PaymentMethod
from ...domain.value_objects.customer_info import CustomerInfo
from ...domain.value_objects.child_info import ChildInfo
from ...domain.services.pricing_service import PricingService
from ...domain.services.availability_service import AvailabilityService
from ...domain.events.booking_events import BookingCreated
from ...infrastructure.repositories.booking_repository import BookingRepository
from ...infrastructure.repositories.franchise_repository import FranchiseRepository
from ...infrastructure.repositories.payment_repository import PaymentRepository
from ...infrastructure.events.event_publisher import EventPublisher

class BookingApplicationService:
    def __init__(self, booking_repo: BookingRepository, franchise_repo: FranchiseRepository, 
                 payment_repo: PaymentRepository, event_publisher: EventPublisher):
        self.booking_repo = booking_repo
        self.franchise_repo = franchise_repo
        self.payment_repo = payment_repo
        self.event_publisher = event_publisher
        self.availability_service = AvailabilityService(booking_repo)
    
    def create_booking(self, franchise_id: str, start_datetime: datetime, end_datetime: datetime,
                      customer_info: CustomerInfo, child_info: ChildInfo) -> str:
        franchise = self.franchise_repo.get_by_id(franchise_id)
        if not franchise:
            raise ValueError("Franchise not found")
        
        if not self.availability_service.check_availability(franchise, start_datetime, end_datetime):
            raise ValueError("No availability for requested time")
        
        total_amount = PricingService.calculate_booking_cost(franchise, start_datetime, end_datetime)
        
        booking = Booking(
            franchise_id=franchise_id,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            customer_info=customer_info,
            child_info=child_info,
            total_amount=total_amount
        )
        
        # Create and publish event
        event = BookingCreated(
            booking_id=booking.id,
            franchise_id=franchise_id,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            customer_email=customer_info.email,
            child_name=child_info.name
        )
        booking.add_event(event)
        
        aggregate = BookingAggregate(booking)
        self.booking_repo.save(booking)
        self.event_publisher.publish_events(aggregate.get_uncommitted_events())
        aggregate.mark_events_committed()
        
        return booking.id
    
    def process_payment(self, booking_id: str, payment_method: PaymentMethod) -> str:
        booking = self.booking_repo.get_by_id(booking_id)
        if not booking:
            raise ValueError("Booking not found")
        
        payment = Payment(
            booking_id=booking_id,
            amount=booking.total_amount,
            payment_method=payment_method,
            stripe_payment_id=f"stripe_{booking_id}"
        )
        payment.mark_completed()
        
        aggregate = BookingAggregate(booking)
        aggregate.add_payment(payment)
        
        self.payment_repo.save(payment)
        self.booking_repo.save(booking)
        self.event_publisher.publish_events(aggregate.get_uncommitted_events())
        aggregate.mark_events_committed()
        
        return payment.id
    
    def cancel_booking(self, booking_id: str, reason: str) -> None:
        booking = self.booking_repo.get_by_id(booking_id)
        if not booking:
            raise ValueError("Booking not found")
        
        aggregate = BookingAggregate(booking)
        aggregate.cancel_booking(reason)
        
        self.booking_repo.save(booking)
        self.event_publisher.publish_events(aggregate.get_uncommitted_events())
        aggregate.mark_events_committed()