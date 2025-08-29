from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4
from enum import Enum
from ..value_objects.money import Money

class PaymentMethod(Enum):
    CREDIT_CARD = "CREDIT_CARD"
    DEBIT_CARD = "DEBIT_CARD"

class PaymentStatus(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"

@dataclass
class Payment:
    booking_id: str
    amount: Money
    payment_method: PaymentMethod
    id: str = None
    stripe_payment_id: str = ""
    payment_status: PaymentStatus = PaymentStatus.PENDING
    processed_at: datetime = None
    
    def __post_init__(self):
        if not self.id:
            self.id = str(uuid4())
    
    def mark_completed(self):
        self.payment_status = PaymentStatus.COMPLETED
        self.processed_at = datetime.utcnow()