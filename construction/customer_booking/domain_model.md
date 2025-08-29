# Customer Booking Domain Model

## Bounded Context: Customer Booking
**Purpose**: Handle customer-facing booking operations including availability checking, booking creation, payment processing, and booking management.

## Aggregates

### 1. Booking Aggregate
**Aggregate Root**: Booking  
**Invariants**: 
- Booking cannot exceed franchise capacity
- Cannot book in the past
- Payment must be completed before confirmation
- Cancellation must follow policy rules

#### Entities
- **Booking** (Root)
  - BookingId (Identity)
  - CustomerId
  - FranchiseId
  - BookingStatus
  - CreatedAt, UpdatedAt
  - TotalAmount
  - PaymentStatus

#### Value Objects
- **TimeSlot**
  - StartDateTime
  - EndDateTime
  - Duration (hours)

- **CustomerInfo**
  - Name
  - Email
  - Phone
  - EmergencyContact

- **ChildInfo**
  - Name
  - Age
  - SpecialNeeds
  - Allergies
  - PickupAuthorization
  - SpecialInstructions

- **BookingReference**
  - ReferenceNumber (UUID)
  - QRCode (Base64)

- **Money**
  - Amount (decimal)
  - Currency

### 2. Franchise Aggregate
**Aggregate Root**: Franchise  
**Invariants**:
- Operating hours must be valid
- Capacity cannot be negative
- Pricing must be positive

#### Entities
- **Franchise** (Root)
  - FranchiseId (Identity)
  - Name
  - Location
  - ContactInfo
  - OperatingHours
  - MaxCapacity

#### Value Objects
- **OperatingHours**
  - OpenTime
  - CloseTime
  - OperatingDays[]

- **Location**
  - Address
  - City
  - PostalCode
  - Coordinates

- **PricingPolicy**
  - StandardRate (Money)
  - PeakHourRate (Money)
  - HolidayRate (Money)

## Domain Events

### BookingCreated
```json
{
  "eventId": "uuid",
  "eventType": "BookingCreated",
  "aggregateId": "booking-id",
  "version": 1,
  "timestamp": "2024-01-01T10:00:00Z",
  "data": {
    "bookingId": "uuid",
    "customerId": "uuid",
    "franchiseId": "uuid",
    "timeSlot": {
      "startDateTime": "2024-01-15T09:00:00Z",
      "endDateTime": "2024-01-15T17:00:00Z",
      "duration": 8
    },
    "childInfo": {
      "name": "string",
      "age": 5,
      "specialNeeds": "string",
      "allergies": "string"
    },
    "totalAmount": {
      "amount": 120.00,
      "currency": "USD"
    }
  }
}
```

### PaymentProcessed
```json
{
  "eventId": "uuid",
  "eventType": "PaymentProcessed",
  "aggregateId": "booking-id",
  "version": 2,
  "timestamp": "2024-01-01T10:05:00Z",
  "data": {
    "bookingId": "uuid",
    "paymentId": "uuid",
    "amount": {
      "amount": 120.00,
      "currency": "USD"
    },
    "paymentMethod": "credit_card",
    "transactionId": "string"
  }
}
```

### BookingConfirmed
```json
{
  "eventId": "uuid",
  "eventType": "BookingConfirmed",
  "aggregateId": "booking-id",
  "version": 3,
  "timestamp": "2024-01-01T10:05:30Z",
  "data": {
    "bookingId": "uuid",
    "bookingReference": {
      "referenceNumber": "uuid",
      "qrCode": "base64-string"
    },
    "confirmationEmail": "customer@email.com"
  }
}
```

### BookingCancelled
```json
{
  "eventId": "uuid",
  "eventType": "BookingCancelled",
  "aggregateId": "booking-id",
  "version": 4,
  "timestamp": "2024-01-01T15:00:00Z",
  "data": {
    "bookingId": "uuid",
    "cancellationReason": "string",
    "refundAmount": {
      "amount": 100.00,
      "currency": "USD"
    },
    "cancellationPolicy": "24_hour_policy"
  }
}
```

### BookingModified
```json
{
  "eventId": "uuid",
  "eventType": "BookingModified",
  "aggregateId": "booking-id",
  "version": 5,
  "timestamp": "2024-01-01T12:00:00Z",
  "data": {
    "bookingId": "uuid",
    "originalTimeSlot": {
      "startDateTime": "2024-01-15T09:00:00Z",
      "endDateTime": "2024-01-15T17:00:00Z"
    },
    "newTimeSlot": {
      "startDateTime": "2024-01-15T10:00:00Z",
      "endDateTime": "2024-01-15T18:00:00Z"
    },
    "priceDifference": {
      "amount": 15.00,
      "currency": "USD"
    }
  }
}
```

## Domain Services

### AvailabilityService
**Purpose**: Check franchise availability and capacity
**Methods**:
- `checkAvailability(franchiseId, timeSlot): AvailabilityResult`
- `calculateCapacityUtilization(franchiseId, date): CapacityInfo`

### PricingService
**Purpose**: Calculate booking costs based on policies
**Methods**:
- `calculateBookingCost(franchiseId, timeSlot): Money`
- `calculateCancellationRefund(booking, cancellationTime): Money`

### QRCodeService
**Purpose**: Generate QR codes for bookings
**Methods**:
- `generateQRCode(bookingReference): QRCode`
- `validateQRCode(qrCode): BookingReference`

## Policies

### CancellationPolicy
**Rules**:
- 24+ hours before: 100% refund
- 12-24 hours before: 50% refund  
- Less than 12 hours: No refund
- Emergency cancellations: Case by case

### CapacityPolicy
**Rules**:
- Maximum children per time slot based on franchise capacity
- Overbooking prevention
- Peak hour capacity adjustments

### PricingPolicy
**Rules**:
- Standard hourly rates
- Peak hour multipliers (evenings, weekends)
- Holiday premium rates
- Minimum booking duration (1 hour)

## Repositories

### BookingRepository
```python
class BookingRepository:
    def save(self, booking: Booking) -> None
    def find_by_id(self, booking_id: BookingId) -> Optional[Booking]
    def find_by_reference(self, reference: BookingReference) -> Optional[Booking]
    def find_by_customer(self, customer_id: CustomerId) -> List[Booking]
    def find_by_franchise_and_date(self, franchise_id: FranchiseId, date: Date) -> List[Booking]
```

### FranchiseRepository
```python
class FranchiseRepository:
    def save(self, franchise: Franchise) -> None
    def find_by_id(self, franchise_id: FranchiseId) -> Optional[Franchise]
    def find_all_active(self) -> List[Franchise]
```

## Application Services

### BookingApplicationService
**Commands**:
- CreateBookingCommand
- ProcessPaymentCommand
- CancelBookingCommand
- ModifyBookingCommand

### AvailabilityApplicationService
**Queries**:
- CheckAvailabilityQuery
- GetFranchiseInfoQuery

## Implementation Suggestions

### Technology Stack
- **Domain Layer**: Pure Python classes
- **Event Store**: EventStore DB or PostgreSQL with event sourcing
- **Repository**: SQLAlchemy with PostgreSQL
- **Message Bus**: RabbitMQ or AWS SQS
- **Payment**: Stripe API integration
- **QR Codes**: qrcode Python library

### Patterns
- **CQRS**: Separate read/write models
- **Event Sourcing**: For booking aggregate
- **Saga Pattern**: For payment processing workflow
- **Repository Pattern**: Data access abstraction
- **Domain Events**: Async integration between contexts