from typing import Dict, List, Optional
from ...domain.entities.payment import Payment

class PaymentRepository:
    def __init__(self):
        self._payments: Dict[str, Payment] = {}
    
    def save(self, payment: Payment) -> None:
        self._payments[payment.id] = payment
    
    def get_by_id(self, payment_id: str) -> Optional[Payment]:
        return self._payments.get(payment_id)
    
    def get_by_booking_id(self, booking_id: str) -> List[Payment]:
        return [p for p in self._payments.values() if p.booking_id == booking_id]