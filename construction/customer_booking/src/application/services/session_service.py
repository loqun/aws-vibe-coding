from datetime import datetime
from ...domain.entities.booking_session import BookingSession
from ...domain.value_objects.admin_value_objects import ParentPhoto, AdditionalCharge, SessionNotes
from ...domain.services.qr_service import QRScanningService, PhotoCaptureService
from ...domain.events.admin_events import SessionStarted, ChildCheckedIn, OvertimeChargeApplied, ChildCheckedOut, SessionCompleted
from ...infrastructure.repositories.session_repository import BookingSessionRepository
from ...infrastructure.repositories.booking_repository import BookingRepository
from ...infrastructure.events.event_publisher import EventPublisher

class SessionManagementService:
    def __init__(self, session_repo: BookingSessionRepository, booking_repo: BookingRepository, 
                 event_publisher: EventPublisher):
        self.session_repo = session_repo
        self.booking_repo = booking_repo
        self.event_publisher = event_publisher
    
    def start_session(self, qr_data: str, staff_id: str) -> str:
        booking_id = QRScanningService.scan_qr_code(qr_data)
        if not booking_id:
            raise ValueError("Invalid QR code")
        
        booking = self.booking_repo.get_by_id(booking_id)
        if not booking:
            raise ValueError("Booking not found")
        
        session = BookingSession(
            booking_id=booking_id,
            staff_member_id=staff_id
        )
        
        event = SessionStarted(
            session_id=session.id,
            booking_id=booking_id,
            staff_member_id=staff_id,
            qr_code_scanned=qr_data
        )
        session.add_event(event)
        
        self.session_repo.save(session)
        self.event_publisher.publish_events([event])
        
        return session.id
    
    def check_in_child(self, session_id: str, photo_data: str) -> None:
        session = self.session_repo.get_by_id(session_id)
        if not session:
            raise ValueError("Session not found")
        
        photo_id = PhotoCaptureService.capture_parent_photo(photo_data, session.staff_member_id)
        parent_photo = ParentPhoto(
            photo_data=photo_id,
            captured_at=datetime.utcnow(),
            staff_member_id=session.staff_member_id
        )
        
        session.check_in_child(parent_photo)
        
        booking = self.booking_repo.get_by_id(session.booking_id)
        event = ChildCheckedIn(
            session_id=session_id,
            booking_id=session.booking_id,
            child_name=booking.child_info.name if booking else "Unknown",
            check_in_time=session.check_in_time,
            staff_member_id=session.staff_member_id
        )
        session.add_event(event)
        
        self.session_repo.save(session)
        self.event_publisher.publish_events([event])
    
    def apply_overtime_charge(self, session_id: str, overtime_minutes: int) -> None:
        session = self.session_repo.get_by_id(session_id)
        if not session:
            raise ValueError("Session not found")
        
        # Simple overtime calculation: $1 per minute
        charge_amount = overtime_minutes * 1.0
        
        charge = AdditionalCharge(
            charge_type="overtime",
            amount=charge_amount,
            description=f"{overtime_minutes} minutes overtime",
            applied_at=datetime.utcnow()
        )
        
        session.add_charge(charge)
        
        event = OvertimeChargeApplied(
            session_id=session_id,
            booking_id=session.booking_id,
            overtime_minutes=overtime_minutes,
            charge_amount=charge_amount,
            staff_member_id=session.staff_member_id
        )
        session.add_event(event)
        
        self.session_repo.save(session)
        self.event_publisher.publish_events([event])
    
    def check_out_child(self, session_id: str, notes: str) -> None:
        session = self.session_repo.get_by_id(session_id)
        if not session:
            raise ValueError("Session not found")
        
        session_notes = SessionNotes(
            content=notes,
            created_by=session.staff_member_id,
            created_at=datetime.utcnow()
        )
        
        session.check_out_child(session_notes)
        
        duration = 0
        if session.check_in_time and session.check_out_time:
            duration = int((session.check_out_time - session.check_in_time).total_seconds() / 60)
        
        event = ChildCheckedOut(
            session_id=session_id,
            booking_id=session.booking_id,
            check_out_time=session.check_out_time,
            total_duration_minutes=duration,
            staff_member_id=session.staff_member_id
        )
        session.add_event(event)
        
        self.session_repo.save(session)
        self.event_publisher.publish_events([event])
    
    def complete_session(self, session_id: str) -> None:
        session = self.session_repo.get_by_id(session_id)
        if not session:
            raise ValueError("Session not found")
        
        session.complete_session()
        
        total_amount = sum(charge.amount for charge in session.additional_charges)
        
        event = SessionCompleted(
            session_id=session_id,
            booking_id=session.booking_id,
            total_amount=total_amount,
            all_payments_settled=True  # Simplified for demo
        )
        session.add_event(event)
        
        self.session_repo.save(session)
        self.event_publisher.publish_events([event])