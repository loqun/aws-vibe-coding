from typing import List
from .booking import Booking
from .payment import Payment
from ..events.booking_events import BookingCreated, PaymentProcessed, BookingCancelled

class BookingAggregate:
    def __init__(self, booking: Booking):
        self.booking = booking
        self.payments: List[Payment] = []
    
    def add_payment(self, payment: Payment):
        self.payments.append(payment)
        if payment.payment_status.value == "COMPLETED":
            self.booking.mark_paid()
            event = PaymentProcessed(
                booking_id=self.booking.id,
                payment_id=payment.id,
                amount=float(payment.amount.amount),
                currency=payment.amount.currency
            )
            self.booking.add_event(event)
    
    def cancel_booking(self, reason: str):
        self.booking.cancel_booking()
        refund_amount = sum(p.amount.amount for p in self.payments if p.payment_status.value == "COMPLETED")
        event = BookingCancelled(
            booking_id=self.booking.id,
            cancellation_reason=reason,
            refund_amount=float(refund_amount)
        )
        self.booking.add_event(event)
    
    def get_uncommitted_events(self):
        return self.booking.events.copy()
    
    def mark_events_committed(self):
        self.booking.events.clear()