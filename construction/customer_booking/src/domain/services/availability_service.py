from datetime import datetime, date
from typing import List, Dict
from ..entities.franchise import Franchise

class AvailabilityService:
    def __init__(self, booking_repository):
        self.booking_repository = booking_repository
    
    def check_availability(self, franchise: Franchise, start_time: datetime, end_time: datetime) -> bool:
        if not franchise.is_active:
            return False
        
        # Check operating hours
        if not self._is_within_operating_hours(franchise, start_time, end_time):
            return False
        
        # Check capacity
        existing_bookings = self.booking_repository.get_by_franchise_and_date(
            franchise.id, start_time.date()
        )
        
        overlapping_count = sum(1 for b in existing_bookings 
                              if self._times_overlap(b.start_datetime, b.end_datetime, start_time, end_time))
        
        return overlapping_count < franchise.max_capacity
    
    def _is_within_operating_hours(self, franchise: Franchise, start_time: datetime, end_time: datetime) -> bool:
        weekday = start_time.weekday() + 1  # Monday = 1
        if weekday not in franchise.operating_days:
            return False
        
        # Simple time check - just verify it's a reasonable time
        return 8 <= start_time.hour <= 18 and 8 <= end_time.hour <= 18
    
    def _times_overlap(self, start1: datetime, end1: datetime, start2: datetime, end2: datetime) -> bool:
        return start1 < end2 and start2 < end1