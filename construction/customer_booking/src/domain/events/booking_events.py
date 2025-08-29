from dataclasses import dataclass, field
from datetime import datetime
from .base_event import BaseEvent

@dataclass
class BookingCreated(BaseEvent):
    booking_id: str = ""
    franchise_id: str = ""
    start_datetime: datetime = field(default_factory=datetime.utcnow)
    end_datetime: datetime = field(default_factory=datetime.utcnow)
    customer_email: str = ""
    child_name: str = ""

@dataclass
class PaymentProcessed(BaseEvent):
    booking_id: str = ""
    payment_id: str = ""
    amount: float = 0.0
    currency: str = "USD"

@dataclass
class BookingCancelled(BaseEvent):
    booking_id: str = ""
    cancellation_reason: str = ""
    refund_amount: float = 0.0