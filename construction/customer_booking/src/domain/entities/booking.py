from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4
from enum import Enum
from typing import List
from ..value_objects.money import Money
from ..value_objects.customer_info import CustomerInfo
from ..value_objects.child_info import ChildInfo
from ..events.base_event import BaseEvent

class BookingStatus(Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"

class PaymentStatus(Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    REFUNDED = "REFUNDED"

@dataclass
class Booking:
    franchise_id: str
    start_datetime: datetime
    end_datetime: datetime
    customer_info: CustomerInfo
    child_info: ChildInfo
    total_amount: Money
    id: str = field(default_factory=lambda: str(uuid4()))
    reference_number: str = field(default_factory=lambda: str(uuid4()))
    booking_status: BookingStatus = BookingStatus.PENDING
    payment_status: PaymentStatus = PaymentStatus.PENDING
    qr_code_url: str = ""
    events: List[BaseEvent] = field(default_factory=list)
    
    def confirm_booking(self):
        self.booking_status = BookingStatus.CONFIRMED
    
    def cancel_booking(self):
        self.booking_status = BookingStatus.CANCELLED
    
    def mark_paid(self):
        self.payment_status = PaymentStatus.PAID
        self.confirm_booking()
    
    def add_event(self, event: BaseEvent):
        self.events.append(event)