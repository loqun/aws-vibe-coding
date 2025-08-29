from typing import Dict, List, Optional
from ...domain.entities.booking_session import BookingSession

class BookingSessionRepository:
    def __init__(self):
        self._sessions: Dict[str, BookingSession] = {}
    
    def save(self, session: BookingSession) -> None:
        self._sessions[session.id] = session
    
    def get_by_id(self, session_id: str) -> Optional[BookingSession]:
        return self._sessions.get(session_id)
    
    def get_by_booking_id(self, booking_id: str) -> Optional[BookingSession]:
        for session in self._sessions.values():
            if session.booking_id == booking_id:
                return session
        return None
    
    def get_active_sessions(self) -> List[BookingSession]:
        return [s for s in self._sessions.values() 
                if s.session_status.value in ["STARTED", "CHECKED_IN"]]