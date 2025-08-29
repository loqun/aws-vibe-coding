from datetime import datetime
from decimal import Decimal
from ..entities.franchise import Franchise
from ..value_objects.money import Money

class PricingService:
    @staticmethod
    def calculate_booking_cost(franchise: Franchise, start_time: datetime, end_time: datetime) -> Money:
        duration_hours = (end_time - start_time).total_seconds() / 3600
        
        # Simple pricing: peak hours 16-18, otherwise standard
        is_peak = 16 <= start_time.hour < 18
        rate = franchise.peak_hour_rate if is_peak else franchise.standard_rate
        
        total_amount = Decimal(str(duration_hours)) * rate
        return Money(amount=total_amount)