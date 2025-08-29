# Implementation Plan for Admin Portal Unit

## Overview
Implementing the Admin Portal system based on the Domain Model. Focus on core QR workflow: scan → check-in → check-out → overtime charges → payment.

## Implementation Steps

### Phase 1: Project Structure Setup
- [ ] **Step 1.1**: Create directory structure for `/construction/admin_portal/src/`
- [ ] **Step 1.2**: Set up basic project files

### Phase 2: Domain Layer Implementation  
- [ ] **Step 2.1**: Implement Value Objects (ParentPhoto, AdditionalCharge, SessionNotes)
- [ ] **Step 2.2**: Implement Domain Events (SessionStarted, ChildCheckedIn, OvertimeChargeApplied, etc.)
- [ ] **Step 2.3**: Implement Entities (BookingSession, IncidentReport, StaffMember)
- [ ] **Step 2.4**: Implement Aggregates (BookingSessionAggregate)
- [ ] **Step 2.5**: Implement Domain Services (QRScanningService, PhotoCaptureService)

### Phase 3: Infrastructure Layer Implementation
- [ ] **Step 3.1**: Implement in-memory repositories
- [ ] **Step 3.2**: Implement event store and publisher
- [ ] **Step 3.3**: Mock external services (QR scanner, photo storage)

### Phase 4: Application Layer Implementation
- [ ] **Step 4.1**: Implement SessionManagementService
- [ ] **Step 4.2**: Implement command handlers

### Phase 5: API Layer Implementation
- [ ] **Step 5.1**: Implement FastAPI endpoints for session management
- [ ] **Step 5.2**: Implement QR scanning and photo capture endpoints

### Phase 6: Demo and Testing
- [ ] **Step 6.1**: Create demo script for QR workflow
- [ ] **Step 6.2**: Test complete session lifecycle

## Decisions Made
- Focus on core QR workflow only
- Mock QR scanning and photo capture
- Minimal overtime charging logic
- In-memory storage for demo