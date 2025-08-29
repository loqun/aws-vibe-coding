from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class ParentPhoto:
    photo_data: str  # Base64 encoded
    captured_at: datetime
    staff_member_id: str

@dataclass(frozen=True)
class AdditionalCharge:
    charge_type: str  # "overtime", "extras"
    amount: float
    description: str
    applied_at: datetime

@dataclass(frozen=True)
class SessionNotes:
    content: str
    created_by: str
    created_at: datetime