# Unified Childcare Management System

A Domain-Driven Design implementation combining Customer Booking and Admin Portal for childcare franchises.

## Architecture

- **Domain Layer**: Entities, Value Objects, Domain Events, Domain Services
- **Application Layer**: Application Services for both Customer and Admin operations
- **Infrastructure Layer**: In-memory Repositories, Event Store
- **API Layer**: Unified FastAPI with Customer + Admin endpoints

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Seed Demo Data
```bash
python migrate_demo.py
```

### 3. Run Unified Demo
```bash
python unified_demo.py
```

### 4. Run API Server (with auto-seeded data)
```bash
cd src
uvicorn api.main:app --reload
```

## API Endpoints

### Customer Endpoints
- `POST /api/v1/bookings` - Create booking
- `GET /api/v1/bookings/{id}` - Get booking details
- `POST /api/v1/bookings/{id}/payment` - Process payment
- `DELETE /api/v1/bookings/{id}` - Cancel booking
- `GET /api/v1/franchises` - List franchises

### Admin Portal Endpoints
- `POST /api/v1/admin/sessions` - Start session (QR scan)
- `POST /api/v1/admin/sessions/{id}/checkin` - Check-in child
- `POST /api/v1/admin/sessions/{id}/overtime` - Apply overtime charge
- `POST /api/v1/admin/sessions/{id}/checkout` - Check-out child
- `POST /api/v1/admin/sessions/{id}/complete` - Complete session
- `GET /api/v1/admin/sessions/{id}` - Get session details
- `GET /api/v1/admin/sessions` - List active sessions

## Complete Workflow Demo

The unified demo demonstrates:
1. **Customer**: Create booking → Pay → Get QR code
2. **Admin**: Scan QR → Start session → Check-in child → Apply overtime → Check-out → Complete
3. **Events**: 7 domain events published throughout the process

## Key Features

- **Unified System**: Customer booking + Admin portal in one API
- **Event-driven architecture**: Rich domain events for both contexts
- **QR Code Workflow**: Complete scan-to-completion process
- **Overtime Management**: Automatic charge calculation
- **Photo Capture**: Mock parent photo verification
- **Clean DDD Structure**: Proper bounded contexts with shared infrastructure