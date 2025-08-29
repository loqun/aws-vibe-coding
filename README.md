# Childcare Drop-off Franchise System

A comprehensive childcare management platform built with Domain-Driven Design (DDD) principles, featuring customer booking capabilities and admin portal functionality for franchise operations.

## 🏗️ Architecture

This system implements a **unified childcare management platform** combining:
- **Customer Booking System** - Guest booking, payment processing, QR code generation
- **Admin Portal** - Session management, check-in/out, overtime processing
- **Event-Driven Architecture** - Rich domain events for system integration
- **Clean DDD Structure** - Proper bounded contexts with shared infrastructure

### Tech Stack

**Backend:**
- Python 3.8+ with FastAPI
- Domain-Driven Design (DDD) architecture
- In-memory repositories (demo implementation)
- Event sourcing and CQRS patterns

**Frontend:**
- Vue 3 with TypeScript
- Pinia for state management
- Tailwind CSS for styling
- Vite for build tooling
- Stripe integration for payments

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 20.19.0+ or 22.12.0+
- npm or yarn

### Backend Setup

```bash
# Navigate to backend
cd construction/customer_booking

# Install dependencies
pip install -r requirements.txt

# Seed demo data
python migrate_demo.py

# Run unified demo
python unified_demo.py

# Start API server (with auto-seeded data)
cd src
uvicorn api.main:app --reload
```

### Frontend Setup

```bash
# Navigate to frontend
cd construction/customer_booking/frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## 📋 Features

### Customer Features
- **Franchise Discovery** - Browse available childcare locations
- **Real-time Availability** - Check capacity and time slots
- **Booking Management** - Create, modify, and cancel reservations
- **Secure Payments** - Stripe integration for payment processing
- **QR Code Generation** - Digital check-in codes for admin scanning
- **Booking Confirmation** - Email confirmations with QR codes

### Admin Features
- **QR Code Scanning** - Quick access to booking sessions
- **Child Check-in/out** - Complete drop-off and pickup workflow
- **Photo Verification** - Parent photo capture for pickup security
- **Overtime Management** - Automatic charge calculation and processing
- **Session Tracking** - Real-time monitoring of active sessions
- **Payment Processing** - Handle additional charges via QR codes

### System Features
- **Event-Driven Architecture** - 7+ domain events for system integration
- **Capacity Management** - Prevent overbooking with real-time capacity tracking
- **Pricing Policies** - Flexible hourly rates with peak hour adjustments
- **Cancellation Policies** - Automated refund processing based on timing
- **Security** - Photo verification and pickup authorization

## 🔄 Complete Workflow

### Customer Journey
1. **Browse Franchises** - View available locations and pricing
2. **Select Date/Time** - Choose preferred drop-off slot
3. **Provide Information** - Enter child and contact details
4. **Process Payment** - Secure payment via Stripe
5. **Receive QR Code** - Digital confirmation for admin scanning

### Admin Workflow
1. **Scan QR Code** - Access booking session details
2. **Check-in Child** - Verify details and capture parent photo
3. **Monitor Session** - Track active drop-offs
4. **Process Overtime** - Calculate and charge additional fees
5. **Check-out Child** - Verify parent identity and complete session

## 🏛️ Domain Model

### Bounded Contexts
- **Customer Booking** - Handles guest bookings, payments, and confirmations
- **Admin Portal** - Manages operational workflows and session tracking
- **Shared Infrastructure** - Common repositories, events, and services

### Key Aggregates
- **Booking Aggregate** - Core booking entity with payment and status management
- **Franchise Aggregate** - Location details, capacity, and operating hours
- **Session Aggregate** - Admin workflow tracking from check-in to completion

### Domain Events
- `BookingCreated` - New booking initiated
- `PaymentProcessed` - Payment successfully completed
- `BookingConfirmed` - QR code generated and confirmation sent
- `SessionStarted` - Admin begins check-in process
- `ChildCheckedIn` - Drop-off completed with photo verification
- `OvertimeApplied` - Additional charges calculated
- `SessionCompleted` - Pickup completed and booking closed

## 📁 Project Structure

```
aws/
├── construction/
│   └── customer_booking/          # Main application
│       ├── src/                   # Backend source code
│       │   ├── domain/           # Domain layer (entities, events, services)
│       │   ├── application/      # Application services and use cases
│       │   ├── infrastructure/   # Repositories and external services
│       │   └── api/             # FastAPI endpoints and controllers
│       ├── frontend/             # Vue.js frontend application
│       │   ├── src/
│       │   │   ├── components/  # Reusable Vue components
│       │   │   ├── views/       # Page-level components
│       │   │   ├── stores/      # Pinia state management
│       │   │   ├── services/    # API integration
│       │   │   └── types/       # TypeScript definitions
│       │   └── package.json
│       ├── demo.py              # Basic demo script
│       ├── unified_demo.py      # Complete workflow demonstration
│       └── requirements.txt
├── inception/                    # Project planning and user stories
└── aidlc/                       # AI development prompts and documentation
```

## 🔌 API Endpoints

### Customer API
- `GET /api/v1/franchises` - List available franchises
- `POST /api/v1/bookings` - Create new booking
- `GET /api/v1/bookings/{id}` - Get booking details
- `POST /api/v1/bookings/{id}/payment` - Process payment
- `DELETE /api/v1/bookings/{id}` - Cancel booking

### Admin API
- `POST /api/v1/admin/sessions` - Start session (QR scan)
- `POST /api/v1/admin/sessions/{id}/checkin` - Check-in child
- `POST /api/v1/admin/sessions/{id}/overtime` - Apply overtime charges
- `POST /api/v1/admin/sessions/{id}/checkout` - Check-out child
- `POST /api/v1/admin/sessions/{id}/complete` - Complete session
- `GET /api/v1/admin/sessions` - List active sessions

## 🧪 Testing

### Run Backend Demo
```bash
cd construction/customer_booking
python unified_demo.py
```

### Test API Endpoints
```bash
cd construction/customer_booking
python test_api.py
```

### Frontend Development
```bash
cd construction/customer_booking/frontend
npm run dev
```

## 📚 Documentation

- [Domain Model](construction/customer_booking/domain_model.md) - Detailed domain design
- [Implementation Summary](construction/customer_booking/IMPLEMENTATION_SUMMARY.md) - Technical implementation details
- [User Stories](inception/overview_user_stories.md) - Complete feature requirements
- [Logical Design](construction/customer_booking/logical_design.md) - System architecture

## 🔮 Future Enhancements

- **Multi-tenant Architecture** - Support multiple franchise chains
- **Mobile Apps** - Native iOS/Android applications
- **Real-time Notifications** - Push notifications for booking updates
- **Advanced Reporting** - Analytics dashboard for franchise owners
- **Integration APIs** - Third-party calendar and payment systems
- **Recurring Bookings** - Subscription-based childcare services

## 🤝 Contributing

This project follows Domain-Driven Design principles and clean architecture patterns. When contributing:

1. Maintain separation between domain, application, and infrastructure layers
2. Use domain events for cross-context communication
3. Follow existing TypeScript and Python coding standards
4. Add tests for new features and bug fixes
5. Update documentation for API changes

## 📄 License

This project is part of the AWS development portfolio and is intended for demonstration purposes.
