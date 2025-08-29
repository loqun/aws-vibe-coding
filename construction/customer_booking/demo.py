#!/usr/bin/env python3
"""
Demo script for Customer Booking System
Demonstrates the complete booking workflow: create → pay → cancel
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from datetime import datetime, timedelta
from decimal import Decimal

from src.domain.entities.franchise import Franchise
from src.domain.value_objects.customer_info import CustomerInfo
from src.domain.value_objects.child_info import ChildInfo
from src.domain.entities.payment import PaymentMethod
from src.infrastructure.repositories.booking_repository import BookingRepository
from src.infrastructure.repositories.franchise_repository import FranchiseRepository
from src.infrastructure.repositories.payment_repository import PaymentRepository
from src.infrastructure.events.event_store import EventStore
from src.infrastructure.events.event_publisher import EventPublisher
from src.application.services.booking_service import BookingApplicationService

def setup_demo_data():
    """Setup sample franchise data"""
    franchise_repo = FranchiseRepository()
    
    # Create sample franchise
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
        operating_days=[1, 2, 3, 4, 5]  # Monday to Friday
    )
    
    franchise_repo.save(franchise)
    return franchise_repo, franchise

def main():
    print("🎯 Customer Booking System Demo")
    print("=" * 50)
    
    # Setup
    franchise_repo, franchise = setup_demo_data()
    booking_repo = BookingRepository()
    payment_repo = PaymentRepository()
    event_store = EventStore()
    event_publisher = EventPublisher(event_store)
    
    booking_service = BookingApplicationService(
        booking_repo, franchise_repo, payment_repo, event_publisher
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
    
    # Book for next Monday at 9 AM for 8 hours
    today = datetime.now()
    days_until_monday = (7 - today.weekday()) % 7
    if days_until_monday == 0:  # If today is Monday, book for next Monday
        days_until_monday = 7
    
    start_time = today.replace(hour=9, minute=0, second=0, microsecond=0) + timedelta(days=days_until_monday)
    end_time = start_time + timedelta(hours=8)  # 8 hours
    
    try:
        # Step 1: Create booking
        print("📅 Step 1: Creating booking...")
        booking_id = booking_service.create_booking(
            franchise.id, start_time, end_time, customer_info, child_info
        )
        
        booking = booking_repo.get_by_id(booking_id)
        print(f"✅ Booking created: {booking_id}")
        print(f"   Reference: {booking.reference_number}")
        print(f"   Amount: ${booking.total_amount.amount}")
        print(f"   Status: {booking.booking_status.value}")
        
        # Step 2: Process payment
        print("\n💳 Step 2: Processing payment...")
        payment_id = booking_service.process_payment(booking_id, PaymentMethod.CREDIT_CARD)
        
        booking = booking_repo.get_by_id(booking_id)  # Refresh
        print(f"✅ Payment processed: {payment_id}")
        print(f"   Booking status: {booking.booking_status.value}")
        print(f"   Payment status: {booking.payment_status.value}")
        
        # Step 3: Cancel booking
        print("\n❌ Step 3: Cancelling booking...")
        booking_service.cancel_booking(booking_id, "Demo cancellation")
        
        booking = booking_repo.get_by_id(booking_id)  # Refresh
        print(f"✅ Booking cancelled")
        print(f"   Status: {booking.booking_status.value}")
        
        # Show events
        print("\n📢 Events published:")
        events = event_store.get_all_events()
        for i, event in enumerate(events, 1):
            print(f"   {i}. {event.__class__.__name__} at {event.timestamp}")
        
        print(f"\n🎉 Demo completed successfully!")
        print(f"   Total events: {len(events)}")
        print(f"   Final booking status: {booking.booking_status.value}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())