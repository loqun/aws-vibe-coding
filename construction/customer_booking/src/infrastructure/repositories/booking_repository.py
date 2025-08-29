from typing import Dict, List, Optional
from datetime import date
from ...domain.entities.booking import Booking

class BookingRepository:
    def __init__(self):
        self._bookings: Dict[str, Booking] = {}
    
    def save(self, booking: Booking) -> None:
        self._bookings[booking.id] = booking
    
    def get_by_id(self, booking_id: str) -> Optional[Booking]:
        return self._bookings.get(booking_id)
    
    def get_by_franchise_and_date(self, franchise_id: str, booking_date: date) -> List[Booking]:
        return [b for b in self._bookings.values() 
                if b.franchise_id == franchise_id and b.start_datetime.date() == booking_date]
    
    def get_all(self) -> List[Booking]:
        return list(self._bookings.values())