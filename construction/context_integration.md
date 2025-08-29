# Bounded Context Integration

## Context Map

### Customer Booking ↔ Admin Portal Relationship
**Pattern**: Customer-Supplier  
**Direction**: Customer Booking (Upstream) → Admin Portal (Downstream)

## Shared Concepts

### 1. Booking Identity
- **Customer Booking Context**: BookingId (primary)
- **Admin Portal Context**: BookingId (foreign reference)
- **Integration**: Admin Portal references Customer Booking's BookingId

### 2. Franchise Identity  
- **Customer Booking Context**: FranchiseId (primary)
- **Admin Portal Context**: FranchiseId (foreign reference)
- **Integration**: Both contexts share franchise identity

### 3. Money Value Object
- **Shared Implementation**: Both contexts use identical Money value object
- **Currency**: USD (standardized)
- **Precision**: 2 decimal places

## Integration Events

### From Customer Booking to Admin Portal

#### BookingConfirmed → SessionReady
```json
{
  "eventType": "BookingConfirmed",
  "data": {
    "bookingId": "uuid",
    "franchiseId": "uuid",
    "timeSlot": {
      "startDateTime": "2024-01-15T09:00:00Z",
      "endDateTime": "2024-01-15T17:00:00Z"
    },
    "customerInfo": {
      "name": "string",
      "email": "string",
      "phone": "string"
    },
    "childInfo": {
      "name": "string",
      "age": 5,
      "specialNeeds": "string",
      "allergies": "string"
    },
    "bookingReference": {
      "referenceNumber": "uuid",
      "qrCode": "base64-string"
    }
  }
}
```

#### BookingCancelled → SessionCancelled
```json
{
  "eventType": "BookingCancelled",
  "data": {
    "bookingId": "uuid",
    "cancellationTime": "2024-01-01T15:00:00Z",
    "reason": "string"
  }
}
```

### From Admin Portal to Customer Booking

#### AdditionalPaymentRequested → PaymentRequest
```json
{
  "eventType": "AdditionalPaymentRequested",
  "data": {
    "bookingId": "uuid",
    "sessionId": "uuid",
    "additionalAmount": {
      "amount": 25.00,
      "currency": "USD"
    },
    "charges": [
      {
        "type": "overtime",
        "description": "30 minutes overtime",
        "amount": {
          "amount": 25.00,
          "currency": "USD"
        }
      }
    ]
  }
}
```

#### SessionCompleted → BookingFulfilled
```json
{
  "eventType": "SessionCompleted",
  "data": {
    "bookingId": "uuid",
    "sessionId": "uuid",
    "actualStartTime": "2024-01-15T09:05:00Z",
    "actualEndTime": "2024-01-15T17:40:00Z",
    "totalAmount": {
      "amount": 145.00,
      "currency": "USD"
    },
    "incidentReports": [],
    "customerSatisfaction": "satisfied"
  }
}
```

## Anti-Corruption Layers

### Admin Portal ACL
**Purpose**: Protect Admin Portal domain from Customer Booking changes

```python
class CustomerBookingAdapter:
    """Translates Customer Booking events to Admin Portal domain concepts"""
    
    def translate_booking_confirmed(self, event: BookingConfirmedEvent) -> SessionReadyCommand:
        return SessionReadyCommand(
            booking_id=BookingId(event.data.bookingId),
            franchise_id=FranchiseId(event.data.franchiseId),
            scheduled_time=TimeSlot(
                start=event.data.timeSlot.startDateTime,
                end=event.data.timeSlot.endDateTime
            ),
            child_info=ChildInfo(
                name=event.data.childInfo.name,
                age=event.data.childInfo.age,
                special_needs=event.data.childInfo.specialNeeds
            ),
            qr_code=QRCode(event.data.bookingReference.qrCode)
        )
    
    def translate_booking_cancelled(self, event: BookingCancelledEvent) -> CancelSessionCommand:
        return CancelSessionCommand(
            booking_id=BookingId(event.data.bookingId),
            cancellation_time=event.data.cancellationTime
        )
```

### Customer Booking ACL
**Purpose**: Handle Admin Portal integration without coupling

```python
class AdminPortalAdapter:
    """Translates Admin Portal events to Customer Booking domain concepts"""
    
    def translate_additional_payment_request(self, event: AdditionalPaymentRequestedEvent) -> ProcessAdditionalPaymentCommand:
        return ProcessAdditionalPaymentCommand(
            booking_id=BookingId(event.data.bookingId),
            additional_amount=Money(
                amount=event.data.additionalAmount.amount,
                currency=event.data.additionalAmount.currency
            ),
            payment_reason=PaymentReason.OVERTIME
        )
    
    def translate_session_completed(self, event: SessionCompletedEvent) -> CompleteBookingCommand:
        return CompleteBookingCommand(
            booking_id=BookingId(event.data.bookingId),
            actual_service_time=ServiceTime(
                start=event.data.actualStartTime,
                end=event.data.actualEndTime
            ),
            final_amount=Money(
                amount=event.data.totalAmount.amount,
                currency=event.data.totalAmount.currency
            )
        )
```

## Data Synchronization

### Read Models for Integration

#### Customer Booking Read Model (for Admin Portal)
```python
class BookingReadModel:
    booking_id: str
    franchise_id: str
    customer_name: str
    customer_email: str
    child_name: str
    child_age: int
    special_needs: str
    scheduled_start: datetime
    scheduled_end: datetime
    booking_status: str
    qr_code: str
    total_amount: decimal
```

#### Session Read Model (for Customer Booking)
```python
class SessionReadModel:
    session_id: str
    booking_id: str
    actual_start: datetime
    actual_end: datetime
    additional_charges: List[dict]
    incident_reports: List[dict]
    session_status: str
    staff_notes: str
```

## Integration Patterns

### 1. Event-Driven Integration
- **Mechanism**: Domain events published to message bus
- **Technology**: RabbitMQ or AWS EventBridge
- **Reliability**: At-least-once delivery with idempotency
- **Ordering**: Events processed in order per booking

### 2. Saga Pattern for Complex Workflows
**Booking Fulfillment Saga**:
1. BookingConfirmed (Customer Booking)
2. SessionReady (Admin Portal)
3. ChildCheckedIn (Admin Portal)
4. OvertimeChargeApplied (Admin Portal) [if needed]
5. AdditionalPaymentRequested (Admin Portal → Customer Booking)
6. AdditionalPaymentProcessed (Customer Booking)
7. ChildCheckedOut (Admin Portal)
8. SessionCompleted (Admin Portal)
9. BookingFulfilled (Customer Booking)

### 3. Shared Kernel (Minimal)
**Shared Value Objects**:
- Money (amount, currency)
- TimeSlot (start, end, duration)
- ContactInfo (email, phone)

**Implementation**: Shared library package

## Error Handling

### Integration Failures
- **Dead Letter Queue**: Failed events for manual processing
- **Retry Policy**: Exponential backoff with max attempts
- **Circuit Breaker**: Prevent cascade failures
- **Compensation**: Rollback actions for failed sagas

### Data Consistency
- **Eventual Consistency**: Accept temporary inconsistencies
- **Reconciliation**: Periodic sync jobs to fix discrepancies
- **Monitoring**: Alerts for integration failures

## Security Considerations

### Data Privacy
- **PII Handling**: Minimal data sharing between contexts
- **Encryption**: All inter-context communication encrypted
- **Access Control**: Context-specific permissions

### Event Security
- **Message Signing**: Verify event authenticity
- **Payload Encryption**: Sensitive data encrypted in events
- **Audit Trail**: All integration events logged