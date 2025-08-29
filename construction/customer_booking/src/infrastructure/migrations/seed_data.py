from decimal import Decimal
from datetime import datetime, timedelta
from ...domain.entities.franchise import Franchise
from ...domain.value_objects.customer_info import CustomerInfo
from ...domain.value_objects.child_info import ChildInfo
from ...domain.entities.payment import PaymentMethod
from ..repositories.franchise_repository import FranchiseRepository
from ..repositories.booking_repository import BookingRepository
from ..repositories.payment_repository import PaymentRepository
from ..repositories.session_repository import BookingSessionRepository
from ..events.event_store import EventStore
from ..events.event_publisher import EventPublisher
from ...application.services.booking_service import BookingApplicationService

def seed_franchises(franchise_repo: FranchiseRepository):
    """Create sample franchises"""
    franchises = [
        Franchise(
            name="Happy Kids Downtown",
            address="123 Main St",
            city="Seattle",
            postal_code="98101",
            max_capacity=15,
            standard_rate=Decimal("12.00"),
            peak_hour_rate=Decimal("18.00"),
            open_time="07:00",
            close_time="19:00",
            operating_days=[1, 2, 3, 4, 5]
        ),
        Franchise(
            name="Sunshine Daycare",
            address="456 Oak Ave",
            city="Portland",
            postal_code="97201",
            max_capacity=20,
            standard_rate=Decimal("10.00"),
            peak_hour_rate=Decimal("15.00"),
            open_time="06:30",
            close_time="18:30",
            operating_days=[1, 2, 3, 4, 5, 6]
        ),
        Franchise(
            name="Little Angels Care",
            address="789 Pine Rd",
            city="Vancouver",
            postal_code="V6B 1A1",
            max_capacity=12,
            standard_rate=Decimal("15.00"),
            peak_hour_rate=Decimal("22.50"),
            open_time="08:00",
            close_time="17:00",
            operating_days=[1, 2, 3, 4, 5]
        )
    ]
    
    for franchise in franchises:
        franchise_repo.save(franchise)
    
    return franchises

def seed_bookings(booking_service: BookingApplicationService, franchises):
    """Create sample bookings"""
    customers = [
        {
            "customer": CustomerInfo(
                name="Sarah Johnson",
                email="sarah@example.com", 
                phone="+1-555-0101",
                emergency_contact="Mike Johnson +1-555-0102"
            ),
            "child": ChildInfo(
                name="Emma Johnson",
                age=4,
                allergies="Nuts",
                pickup_authorization="Sarah Johnson, Mike Johnson"
            )
        },
        {
            "customer": CustomerInfo(
                name="David Chen",
                email="david@example.com",
                phone="+1-555-0201", 
                emergency_contact="Lisa Chen +1-555-0202"
            ),
            "child": ChildInfo(
                name="Alex Chen",
                age=6,
                special_needs="ADHD medication at 2pm",
                pickup_authorization="David Chen, Lisa Chen, Grandma Chen"
            )
        },
        {
            "customer": CustomerInfo(
                name="Maria Rodriguez",
                email="maria@example.com",
                phone="+1-555-0301",
                emergency_contact="Carlos Rodriguez +1-555-0302"
            ),
            "child": ChildInfo(
                name="Sofia Rodriguez", 
                age=3,
                allergies="Dairy",
                special_instructions="Nap time 1-2pm"
            )
        }
    ]
    
    bookings = []
    base_date = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
    
    for i, customer_data in enumerate(customers):
        # Create booking for next Monday + i days
        days_until_monday = (7 - base_date.weekday()) % 7
        if days_until_monday == 0:
            days_until_monday = 7
        
        start_time = base_date + timedelta(days=days_until_monday + i)
        end_time = start_time + timedelta(hours=8)
        
        booking_id = booking_service.create_booking(
            franchises[i % len(franchises)].id,
            start_time,
            end_time,
            customer_data["customer"],
            customer_data["child"]
        )
        
        # Pay for some bookings
        if i < 2:
            booking_service.process_payment(booking_id, PaymentMethod.CREDIT_CARD)
        
        bookings.append(booking_id)
    
    return bookings

def run_migration(franchise_repo, booking_repo, payment_repo, session_repo, event_store, event_publisher):
    """Run complete data migration"""
    print("🌱 Seeding database with demo data...")
    
    # Initialize services
    booking_service = BookingApplicationService(
        booking_repo, franchise_repo, payment_repo, event_publisher
    )
    
    # Seed data
    franchises = seed_franchises(franchise_repo)
    bookings = seed_bookings(booking_service, franchises)
    
    print(f"✅ Created {len(franchises)} franchises")
    print(f"✅ Created {len(bookings)} bookings")
    print("🎉 Migration completed!")