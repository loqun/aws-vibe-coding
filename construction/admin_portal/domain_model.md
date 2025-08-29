# Admin Portal Domain Model

## Bounded Context: Admin Portal
**Purpose**: Handle administrative operations including QR workflow, franchise staff operations, management functions, and reporting.

## Aggregates

### 1. BookingSession Aggregate
**Aggregate Root**: BookingSession  
**Invariants**:
- Session must have valid booking reference
- Check-in must precede check-out
- Additional payments must be authorized
- Session completion requires all payments settled

#### Entities
- **BookingSession** (Root)
  - SessionId (Identity)
  - BookingId (from Customer Booking context)
  - SessionStatus
  - CheckInTime, CheckOutTime
  - StaffMemberId
  - AdditionalCharges[]

- **IncidentReport**
  - ReportId (Identity)
  - SessionId
  - ReportType
  - Description
  - ReportedAt
  - StaffMemberId

#### Value Objects
- **ParentPhoto**
  - PhotoData (Base64)
  - CapturedAt
  - StaffMemberId

- **AdditionalCharge**
  - ChargeType (overtime, extras)
  - Amount (Money)
  - Description
  - AppliedAt

- **SessionNotes**
  - Content
  - CreatedBy
  - CreatedAt

### 2. FranchiseOperation Aggregate
**Aggregate Root**: FranchiseOperation  
**Invariants**:
- Capacity settings must be positive
- Operating hours must be valid
- Pricing changes require authorization

#### Entities
- **FranchiseOperation** (Root)
  - OperationId (Identity)
  - FranchiseId
  - OperationalStatus
  - CurrentCapacity
  - StaffOnDuty[]

- **StaffMember**
  - StaffId (Identity)
  - Name
  - Role
  - Permissions[]
  - ActiveSessions[]

#### Value Objects
- **CapacityConfiguration**
  - MaxCapacity
  - CurrentUtilization
  - AvailableSlots

- **OperatingSchedule**
  - DailyHours[]
  - Holidays[]
  - SpecialEvents[]

## Domain Events

### SessionStarted
```json
{
  "eventId": "uuid",
  "eventType": "SessionStarted",
  "aggregateId": "session-id",
  "version": 1,
  "timestamp": "2024-01-15T09:00:00Z",
  "data": {
    "sessionId": "uuid",
    "bookingId": "uuid",
    "staffMemberId": "uuid",
    "qrCodeScanned": "base64-string",
    "sessionStartTime": "2024-01-15T09:00:00Z"
  }
}
```

### ChildCheckedIn
```json
{
  "eventId": "uuid",
  "eventType": "ChildCheckedIn",
  "aggregateId": "session-id",
  "version": 2,
  "timestamp": "2024-01-15T09:05:00Z",
  "data": {
    "sessionId": "uuid",
    "bookingId": "uuid",
    "childInfo": {
      "name": "string",
      "age": 5,
      "specialNeeds": "string"
    },
    "parentPhoto": {
      "photoData": "base64-string",
      "capturedAt": "2024-01-15T09:05:00Z",
      "staffMemberId": "uuid"
    },
    "checkInTime": "2024-01-15T09:05:00Z",
    "staffMemberId": "uuid"
  }
}
```

### OvertimeChargeApplied
```json
{
  "eventId": "uuid",
  "eventType": "OvertimeChargeApplied",
  "aggregateId": "session-id",
  "version": 3,
  "timestamp": "2024-01-15T17:30:00Z",
  "data": {
    "sessionId": "uuid",
    "bookingId": "uuid",
    "overtimeMinutes": 30,
    "additionalCharge": {
      "chargeType": "overtime",
      "amount": {
        "amount": 25.00,
        "currency": "USD"
      },
      "description": "30 minutes overtime",
      "appliedAt": "2024-01-15T17:30:00Z"
    },
    "staffMemberId": "uuid"
  }
}
```

### AdditionalPaymentRequested
```json
{
  "eventId": "uuid",
  "eventType": "AdditionalPaymentRequested",
  "aggregateId": "session-id",
  "version": 4,
  "timestamp": "2024-01-15T17:35:00Z",
  "data": {
    "sessionId": "uuid",
    "bookingId": "uuid",
    "paymentAmount": {
      "amount": 25.00,
      "currency": "USD"
    },
    "paymentQRCode": "base64-string",
    "charges": [
      {
        "chargeType": "overtime",
        "amount": {
          "amount": 25.00,
          "currency": "USD"
        },
        "description": "30 minutes overtime"
      }
    ],
    "staffMemberId": "uuid"
  }
}
```

### ChildCheckedOut
```json
{
  "eventId": "uuid",
  "eventType": "ChildCheckedOut",
  "aggregateId": "session-id",
  "version": 5,
  "timestamp": "2024-01-15T17:40:00Z",
  "data": {
    "sessionId": "uuid",
    "bookingId": "uuid",
    "checkOutTime": "2024-01-15T17:40:00Z",
    "parentIdentityVerified": true,
    "totalSessionDuration": 510,
    "incidentReports": [],
    "sessionNotes": {
      "content": "Child had a great day",
      "createdBy": "uuid",
      "createdAt": "2024-01-15T17:40:00Z"
    },
    "staffMemberId": "uuid"
  }
}
```

### SessionCompleted
```json
{
  "eventId": "uuid",
  "eventType": "SessionCompleted",
  "aggregateId": "session-id",
  "version": 6,
  "timestamp": "2024-01-15T17:45:00Z",
  "data": {
    "sessionId": "uuid",
    "bookingId": "uuid",
    "completedAt": "2024-01-15T17:45:00Z",
    "totalAmount": {
      "amount": 145.00,
      "currency": "USD"
    },
    "allPaymentsSettled": true,
    "receiptGenerated": true,
    "staffMemberId": "uuid"
  }
}
```

### IncidentReported
```json
{
  "eventId": "uuid",
  "eventType": "IncidentReported",
  "aggregateId": "session-id",
  "version": 7,
  "timestamp": "2024-01-15T14:30:00Z",
  "data": {
    "sessionId": "uuid",
    "bookingId": "uuid",
    "incidentReport": {
      "reportId": "uuid",
      "reportType": "minor_injury",
      "description": "Small scrape on knee during play",
      "reportedAt": "2024-01-15T14:30:00Z",
      "staffMemberId": "uuid"
    },
    "parentNotified": true
  }
}
```

### CapacityUpdated
```json
{
  "eventId": "uuid",
  "eventType": "CapacityUpdated",
  "aggregateId": "operation-id",
  "version": 1,
  "timestamp": "2024-01-15T08:00:00Z",
  "data": {
    "operationId": "uuid",
    "franchiseId": "uuid",
    "previousCapacity": 20,
    "newCapacity": 25,
    "effectiveDate": "2024-01-16T00:00:00Z",
    "updatedBy": "uuid",
    "reason": "Additional staff hired"
  }
}
```

## Domain Services

### QRScanningService
**Purpose**: Handle QR code scanning and validation
**Methods**:
- `scanQRCode(qrCodeData): BookingReference`
- `validateBookingSession(bookingReference): BookingSessionInfo`

### PhotoCaptureService
**Purpose**: Manage parent photo capture and storage
**Methods**:
- `captureParentPhoto(sessionId, imageData): ParentPhoto`
- `verifyParentIdentity(sessionId, currentPhoto): VerificationResult`

### PaymentQRService
**Purpose**: Generate payment QR codes for additional charges
**Methods**:
- `generatePaymentQR(sessionId, amount): PaymentQRCode`
- `validatePaymentCompletion(paymentQRCode): PaymentStatus`

### ReportingService
**Purpose**: Generate operational reports and analytics
**Methods**:
- `generateDailyReport(franchiseId, date): DailyReport`
- `calculateCapacityUtilization(franchiseId, dateRange): UtilizationReport`

## Policies

### OvertimePolicy
**Rules**:
- Grace period: 15 minutes free
- Overtime rate: 1.5x standard hourly rate
- Minimum overtime charge: 15 minutes
- Maximum overtime allowed: 2 hours

### IncidentReportingPolicy
**Rules**:
- All incidents must be documented
- Parents must be notified immediately for injuries
- Photos required for visible injuries
- Follow-up required within 24 hours

### IdentityVerificationPolicy
**Rules**:
- Parent photo required at check-in
- Visual verification required at check-out
- Authorized pickup persons must be pre-registered
- ID verification for unknown pickup persons

## Repositories

### BookingSessionRepository
```python
class BookingSessionRepository:
    def save(self, session: BookingSession) -> None
    def find_by_id(self, session_id: SessionId) -> Optional[BookingSession]
    def find_by_booking_id(self, booking_id: BookingId) -> Optional[BookingSession]
    def find_active_sessions(self, franchise_id: FranchiseId) -> List[BookingSession]
    def find_by_date_range(self, franchise_id: FranchiseId, start_date: Date, end_date: Date) -> List[BookingSession]
```

### FranchiseOperationRepository
```python
class FranchiseOperationRepository:
    def save(self, operation: FranchiseOperation) -> None
    def find_by_franchise_id(self, franchise_id: FranchiseId) -> Optional[FranchiseOperation]
    def find_by_staff_member(self, staff_id: StaffId) -> Optional[FranchiseOperation]
```

### IncidentReportRepository
```python
class IncidentReportRepository:
    def save(self, report: IncidentReport) -> None
    def find_by_session_id(self, session_id: SessionId) -> List[IncidentReport]
    def find_by_date_range(self, franchise_id: FranchiseId, start_date: Date, end_date: Date) -> List[IncidentReport]
```

## Application Services

### SessionManagementService
**Commands**:
- StartSessionCommand
- CheckInChildCommand
- ApplyOvertimeChargeCommand
- CheckOutChildCommand
- CompleteSessionCommand

### FranchiseManagementService
**Commands**:
- UpdateCapacityCommand
- UpdateOperatingHoursCommand
- UpdatePricingCommand

### ReportingApplicationService
**Queries**:
- GenerateDailyReportQuery
- GetCapacityUtilizationQuery
- GetIncidentReportsQuery

## Integration with Customer Booking Context

### Anti-Corruption Layer
**Purpose**: Translate between contexts and protect domain integrity

```python
class BookingContextAdapter:
    def get_booking_details(self, booking_id: BookingId) -> BookingDetails
    def notify_session_completed(self, booking_id: BookingId, session_summary: SessionSummary) -> None
    def request_additional_payment(self, booking_id: BookingId, amount: Money) -> PaymentRequest
```

## Implementation Suggestions

### Technology Stack
- **Domain Layer**: Pure Python classes
- **Event Store**: EventStore DB or PostgreSQL with event sourcing
- **Repository**: SQLAlchemy with PostgreSQL
- **Photo Storage**: AWS S3 with encryption
- **QR Scanning**: OpenCV or ZXing libraries
- **Real-time Updates**: WebSocket connections
- **Message Bus**: RabbitMQ or AWS SQS

### Patterns
- **CQRS**: Separate operational and reporting models
- **Event Sourcing**: For session aggregate
- **Anti-Corruption Layer**: For integration with Customer Booking context
- **Saga Pattern**: For complex session workflows
- **Observer Pattern**: For real-time dashboard updates