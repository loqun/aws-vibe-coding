#!/usr/bin/env python3
"""
Demo Data Migration Script
Run this to populate the system with sample data for testing
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.infrastructure.repositories.booking_repository import BookingRepository
from src.infrastructure.repositories.franchise_repository import FranchiseRepository
from src.infrastructure.repositories.payment_repository import PaymentRepository
from src.infrastructure.repositories.session_repository import BookingSessionRepository
from src.infrastructure.events.event_store import EventStore
from src.infrastructure.events.event_publisher import EventPublisher
from src.infrastructure.migrations.seed_data import run_migration

def main():
    print("🚀 Running Demo Data Migration")
    print("=" * 40)
    
    # Initialize repositories
    booking_repo = BookingRepository()
    franchise_repo = FranchiseRepository()
    payment_repo = PaymentRepository()
    session_repo = BookingSessionRepository()
    event_store = EventStore()
    event_publisher = EventPublisher(event_store)
    
    # Run migration
    run_migration(franchise_repo, booking_repo, payment_repo, session_repo, event_store, event_publisher)
    
    # Show results
    print(f"\n📊 Demo Data Summary:")
    print(f"   Franchises: {len(franchise_repo.get_all_active())}")
    print(f"   Bookings: {len(booking_repo.get_all())}")
    print(f"   Events: {len(event_store.get_all_events())}")
    
    print(f"\n🎯 Ready for demo! Available franchises:")
    for franchise in franchise_repo.get_all_active():
        print(f"   • {franchise.name} ({franchise.city}) - ${franchise.standard_rate}/hr")

if __name__ == "__main__":
    main()