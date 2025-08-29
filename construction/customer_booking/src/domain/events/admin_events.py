from dataclasses import dataclass
from datetime import datetime
from .base_event import BaseEvent

@dataclass
class SessionStarted(BaseEvent):
    session_id: str = ""
    booking_id: str = ""
    staff_member_id: str = ""
    qr_code_scanned: str = ""

@dataclass
class ChildCheckedIn(BaseEvent):
    session_id: str = ""
    booking_id: str = ""
    child_name: str = ""
    check_in_time: datetime = None
    staff_member_id: str = ""

@dataclass
class OvertimeChargeApplied(BaseEvent):
    session_id: str = ""
    booking_id: str = ""
    overtime_minutes: int = 0
    charge_amount: float = 0.0
    staff_member_id: str = ""

@dataclass
class ChildCheckedOut(BaseEvent):
    session_id: str = ""
    booking_id: str = ""
    check_out_time: datetime = None
    total_duration_minutes: int = 0
    staff_member_id: str = ""

@dataclass
class SessionCompleted(BaseEvent):
    session_id: str = ""
    booking_id: str = ""
    total_amount: float = 0.0
    all_payments_settled: bool = False