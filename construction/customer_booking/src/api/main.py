from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from typing import Optional

from ..domain.value_objects.customer_info import CustomerInfo
from ..domain.value_objects.child_info import ChildInfo
from ..domain.entities.franchise import Franchise
from ..domain.entities.payment import PaymentMethod
from ..infrastructure.repositories.booking_repository import BookingRepository
from ..infrastructure.repositories.franchise_repository import FranchiseRepository
from ..infrastructure.repositories.payment_repository import PaymentRepository
from ..infrastructure.events.event_store import EventStore
from ..infrastructure.events.event_publisher import EventPublisher
from ..application.services.booking_service import BookingApplicationService
from ..application.services.session_service import SessionManagementService
from ..infrastructure.repositories.session_repository import BookingSessionRepository

app = FastAPI(title="Unified Childcare Management API")

@app.get("/")
async def welcome():
    return {
        "message": "Welcome to Unified Childcare Management System",
        "version": "1.0.0",
        "endpoints": {
            "customer": "/api/v1/bookings",
            "admin": "/api/v1/admin/sessions",
            "docs": "/docs"
        }
    }

# Initialize repositories and services
booking_repo = BookingRepository()
franchise_repo = FranchiseRepository()
payment_repo = PaymentRepository()
session_repo = BookingSessionRepository()
event_store = EventStore()
event_publisher = EventPublisher(event_store)
booking_service = BookingApplicationService(booking_repo, franchise_repo, payment_repo, event_publisher)
session_service = SessionManagementService(session_repo, booking_repo, event_publisher)

# Seed demo data on startup
from ..infrastructure.migrations.seed_data import run_migration
run_migration(franchise_repo, booking_repo, payment_repo, session_repo, event_store, event_publisher)

# Pydantic models
class CreateBookingRequest(BaseModel):
    franchise_id: str
    start_datetime: datetime
    end_datetime: datetime
    customer_name: str
    customer_email: str
    customer_phone: str
    emergency_contact: str = ""
    child_name: str
    child_age: int
    special_needs: str = ""
    allergies: str = ""
    pickup_authorization: str = ""
    special_instructions: str = ""

class ProcessPaymentRequest(BaseModel):
    payment_method: str = "CREDIT_CARD"

class StartSessionRequest(BaseModel):
    qr_data: str
    staff_id: str

class CheckInRequest(BaseModel):
    photo_data: str

class OvertimeChargeRequest(BaseModel):
    overtime_minutes: int

class CheckOutRequest(BaseModel):
    notes: str = ""

@app.post("/api/v1/bookings")
async def create_booking(request: CreateBookingRequest):
    try:
        customer_info = CustomerInfo(
            name=request.customer_name,
            email=request.customer_email,
            phone=request.customer_phone,
            emergency_contact=request.emergency_contact
        )
        
        child_info = ChildInfo(
            name=request.child_name,
            age=request.child_age,
            special_needs=request.special_needs,
            allergies=request.allergies,
            pickup_authorization=request.pickup_authorization,
            special_instructions=request.special_instructions
        )
        
        booking_id = booking_service.create_booking(
            request.franchise_id,
            request.start_datetime,
            request.end_datetime,
            customer_info,
            child_info
        )
        
        booking = booking_repo.get_by_id(booking_id)
        return {
            "booking_id": booking_id,
            "reference_number": booking.reference_number,
            "total_amount": float(booking.total_amount.amount),
            "currency": booking.total_amount.currency,
            "payment_required": True
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/v1/bookings/{booking_id}/payment")
async def process_payment(booking_id: str, request: ProcessPaymentRequest):
    try:
        payment_method = PaymentMethod.CREDIT_CARD
        payment_id = booking_service.process_payment(booking_id, payment_method)
        return {"payment_id": payment_id, "status": "completed"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/api/v1/bookings/{booking_id}")
async def cancel_booking(booking_id: str):
    try:
        booking_service.cancel_booking(booking_id, "Customer request")
        return {"status": "cancelled"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/v1/bookings/{booking_id}")
async def get_booking(booking_id: str):
    booking = booking_repo.get_by_id(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    
    return {
        "id": booking.id,
        "franchise_id": booking.franchise_id,
        "start_datetime": booking.start_datetime,
        "end_datetime": booking.end_datetime,
        "status": booking.booking_status.value,
        "payment_status": booking.payment_status.value,
        "total_amount": float(booking.total_amount.amount)
    }

@app.get("/api/v1/franchises")
async def get_franchises():
    franchises = franchise_repo.get_all_active()
    return [{"id": f.id, "name": f.name, "city": f.city} for f in franchises]

# Admin Portal Endpoints
@app.post("/api/v1/admin/sessions")
async def start_session(request: StartSessionRequest):
    try:
        session_id = session_service.start_session(request.qr_data, request.staff_id)
        return {"session_id": session_id, "status": "started"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/v1/admin/sessions/{session_id}/checkin")
async def check_in_child(session_id: str, request: CheckInRequest):
    try:
        session_service.check_in_child(session_id, request.photo_data)
        return {"status": "checked_in"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/v1/admin/sessions/{session_id}/overtime")
async def apply_overtime_charge(session_id: str, request: OvertimeChargeRequest):
    try:
        session_service.apply_overtime_charge(session_id, request.overtime_minutes)
        return {"status": "overtime_applied", "minutes": request.overtime_minutes}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/v1/admin/sessions/{session_id}/checkout")
async def check_out_child(session_id: str, request: CheckOutRequest):
    try:
        session_service.check_out_child(session_id, request.notes)
        return {"status": "checked_out"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/v1/admin/sessions/{session_id}/complete")
async def complete_session(session_id: str):
    try:
        session_service.complete_session(session_id)
        return {"status": "completed"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/v1/admin/sessions/{session_id}")
async def get_session(session_id: str):
    session = session_repo.get_by_id(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    return {
        "id": session.id,
        "booking_id": session.booking_id,
        "status": session.session_status.value,
        "check_in_time": session.check_in_time,
        "check_out_time": session.check_out_time,
        "additional_charges": len(session.additional_charges),
        "total_charges": sum(c.amount for c in session.additional_charges)
    }

@app.get("/api/v1/admin/sessions")
async def get_active_sessions():
    sessions = session_repo.get_active_sessions()
    return [{
        "id": s.id,
        "booking_id": s.booking_id,
        "status": s.session_status.value,
        "staff_id": s.staff_member_id
    } for s in sessions]

