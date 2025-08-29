from dataclasses import dataclass
from decimal import Decimal
from uuid import uuid4
from typing import List

@dataclass
class Franchise:
    name: str
    address: str
    city: str
    postal_code: str
    max_capacity: int
    standard_rate: Decimal
    peak_hour_rate: Decimal
    open_time: str
    close_time: str
    operating_days: List[int]
    id: str = None
    is_active: bool = True
    
    def __post_init__(self):
        if not self.id:
            self.id = str(uuid4())