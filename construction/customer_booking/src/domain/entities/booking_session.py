from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4
from enum import Enum
from typing import List, Optional
from ..value_objects.admin_value_objects import ParentPhoto, AdditionalCharge, SessionNotes
from ..events.base_event import BaseEvent

class SessionStatus(Enum):
    STARTED = "STARTED"
    CHECKED_IN = "CHECKED_IN"
    CHECKED_OUT = "CHECKED_OUT"
    COMPLETED = "COMPLETED"

@dataclass
class BookingSession:
    booking_id: str
    staff_member_id: str
    id: str = field(default_factory=lambda: str(uuid4()))
    session_status: SessionStatus = SessionStatus.STARTED
    check_in_time: Optional[datetime] = None
    check_out_time: Optional[datetime] = None
    parent_photo: Optional[ParentPhoto] = None
    additional_charges: List[AdditionalCharge] = field(default_factory=list)
    session_notes: Optional[SessionNotes] = None
    events: List[BaseEvent] = field(default_factory=list)
    
    def check_in_child(self, parent_photo: ParentPhoto):
        self.session_status = SessionStatus.CHECKED_IN
        self.check_in_time = datetime.utcnow()
        self.parent_photo = parent_photo
    
    def check_out_child(self, notes: SessionNotes):
        self.session_status = SessionStatus.CHECKED_OUT
        self.check_out_time = datetime.utcnow()
        self.session_notes = notes
    
    def add_charge(self, charge: AdditionalCharge):
        self.additional_charges.append(charge)
    
    def complete_session(self):
        self.session_status = SessionStatus.COMPLETED
    
    def add_event(self, event: BaseEvent):
        self.events.append(event)