#!/usr/bin/env python3
"""
Unified Demo: Customer Booking + Admin Portal
Demonstrates complete workflow: booking → QR scan → check-in → overtime → check-out
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from datetime import datetime, timedelta
from decimal import Decimal
import base64

from src.domain.entities.franchise import Franchise
from src.domain.value_objects.customer_info import CustomerInfo
from src.domain.value_objects.child_info import ChildInfo
from src.domain.entities.payment import PaymentMethod
from src.infrastructure.repositories.booking_repository import BookingRepository
from src.infrastructure.repositories.franchise_repository import FranchiseRepository
from src.infrastructure.repositories.payment_repository import PaymentRepository
from src.infrastructure.repositories.session_repository import BookingSessionRepository
from src.infrastructure.events.event_store import EventStore
from src.infrastructure.events.event_publisher import EventPublisher
from src.application.services.booking_service import BookingApplicationService
from src.application.services.session_service import SessionManagementService

def setup_demo_data():
    """Setup sample franchise data"""
    franchise_repo = FranchiseRepository()
    
    franchise = Franchise(
        name="Happy Kids Daycare",
        address="123 Main St",
        city="Seattle",
        postal_code="98101",
        max_capacity=10,
        standard_rate=Decimal("15.00"),
        peak_hour_rate=Decimal("22.50"),
        open_time="08:00",
        close_time="18:00",
        operating_days=[1, 2, 3, 4, 5]
    )
    
    franchise_repo.save(franchise)
    return franchise_repo, franchise

def main():
    print("🎯 Unified Customer Booking + Admin Portal Demo")
    print("=" * 60)
    
    # Setup
    franchise_repo, franchise = setup_demo_data()
    booking_repo = BookingRepository()
    payment_repo = PaymentRepository()
    session_repo = BookingSessionRepository()
    event_store = EventStore()
    event_publisher = EventPublisher(event_store)
    
    booking_service = BookingApplicationService(
        booking_repo, franchise_repo, payment_repo, event_publisher
    )
    session_service = SessionManagementService(
        session_repo, booking_repo, event_publisher
    )
    
    # Demo data
    customer_info = CustomerInfo(
        name="John Doe",
        email="john@example.com",
        phone="+1234567890",
        emergency_contact="Jane Doe +1234567891"
    )
    
    child_info = ChildInfo(
        name="Alice Doe",
        age=5,
        allergies="Peanuts",
        pickup_authorization="John Doe, Jane Doe"
    )
    
    # Book for next Monday at 9 AM for 6 hours
    today = datetime.now()
    days_until_monday = (7 - today.weekday()) % 7
    if days_until_monday == 0:
        days_until_monday = 7
    
    start_time = today.replace(hour=9, minute=0, second=0, microsecond=0) + timedelta(days=days_until_monday)
    end_time = start_time + timedelta(hours=6)
    
    try:
        print("📱 CUSTOMER WORKFLOW")
        print("-" * 30)
        
        # Step 1: Customer creates booking
        print("1️⃣ Creating booking...")
        booking_id = booking_service.create_booking(
            franchise.id, start_time, end_time, customer_info, child_info
        )
        booking = booking_repo.get_by_id(booking_id)
        print(f"✅ Booking created: {booking_id}")
        print(f"   Amount: ${booking.total_amount.amount}")
        
        # Step 2: Customer pays
        print("\\n2️⃣ Processing payment...")
        payment_id = booking_service.process_payment(booking_id, PaymentMethod.CREDIT_CARD)
        print(f"✅ Payment processed: {payment_id}")
        
        # Generate QR code for admin
        qr_data = base64.b64encode(booking_id.encode()).decode()
        print(f"📱 QR Code generated: {qr_data[:20]}...")
        
        print("\\n🏢 ADMIN PORTAL WORKFLOW")
        print("-" * 30)
        
        # Step 3: Staff scans QR and starts session
        print("3️⃣ Staff scanning QR code...")
        session_id = session_service.start_session(qr_data, "staff_001")
        print(f"✅ Session started: {session_id}")
        
        # Step 4: Child check-in with parent photo
        print("\\n4️⃣ Child check-in with parent photo...")
        photo_data = "mock_photo_data_base64_encoded"
        session_service.check_in_child(session_id, photo_data)
        print("✅ Child checked in, parent photo captured")
        
        # Step 5: Apply overtime charge
        print("\\n5️⃣ Applying overtime charge...")
        session_service.apply_overtime_charge(session_id, 30)  # 30 minutes
        print("✅ Overtime charge applied: 30 minutes = $30.00")
        
        # Step 6: Child check-out
        print("\\n6️⃣ Child check-out...")
        session_service.check_out_child(session_id, "Alice had a wonderful day!")
        print("✅ Child checked out with notes")
        
        # Step 7: Complete session
        print("\\n7️⃣ Completing session...")
        session_service.complete_session(session_id)
        print("✅ Session completed")
        
        # Show final status
        print("\\n📊 FINAL STATUS")
        print("-" * 30)
        
        session = session_repo.get_by_id(session_id)
        booking = booking_repo.get_by_id(booking_id)
        
        print(f"Booking Status: {booking.booking_status.value}")
        print(f"Session Status: {session.session_status.value}")
        print(f"Additional Charges: ${sum(c.amount for c in session.additional_charges)}")
        print(f"Session Duration: {session.check_in_time} → {session.check_out_time}")
        
        # Show all events
        print("\\n📢 Events Published:")
        events = event_store.get_all_events()
        for i, event in enumerate(events, 1):
            print(f"   {i}. {event.__class__.__name__}")
        
        print(f"\\n🎉 Complete workflow demo finished!")
        print(f"   Total events: {len(events)}")
        print(f"   Customer booking → Admin session → Complete!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())