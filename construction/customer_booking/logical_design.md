# Customer Booking Unit - Logical Design

## System Architecture Overview

### Architecture Style
**Simplified Microservices with Event-Driven Communication**
- Focus on simplicity and performance
- Minimal service boundaries aligned with domain aggregates
- REST APIs for synchronous operations
- Async events for cross-context integration

### Technology Stack
- **API Framework**: FastAPI (Python) - High performance, auto-documentation
- **Database**: PostgreSQL - ACID compliance for bookings
- **Cache**: Redis - Hot data caching (availability, pricing)
- **Message Queue**: AWS SQS - Simple, managed event publishing
- **Payment**: Stripe API - PCI compliant payment processing
- **Storage**: AWS S3 - QR code and document storage
- **Deployment**: AWS ECS Fargate - Serverless containers

## Service Architecture

### Core Services

#### 1. Booking Service
**Responsibility**: Handle booking lifecycle operations
**Aggregate**: Booking Aggregate
**Database**: PostgreSQL (bookings schema)

**API Endpoints**:
```
POST   /api/v1/bookings              # Create booking
GET    /api/v1/bookings/{id}         # Get booking details
PUT    /api/v1/bookings/{id}         # Modify booking
DELETE /api/v1/bookings/{id}         # Cancel booking
POST   /api/v1/bookings/{id}/payment # Process payment
GET    /api/v1/bookings/{id}/qr      # Get QR code
```

#### 2. Availability Service
**Responsibility**: Check franchise availability and capacity
**Aggregate**: Franchise Aggregate
**Database**: PostgreSQL (franchises schema) + Redis (cache)

**API Endpoints**:
```
GET /api/v1/availability/{franchise_id}        # Check availability
GET /api/v1/availability/{franchise_id}/slots  # Get available slots
GET /api/v1/franchises                         # List franchises
GET /api/v1/franchises/{id}                    # Get franchise details
```

#### 3. Payment Service
**Responsibility**: Handle payment processing and refunds
**Integration**: Stripe API
**Database**: PostgreSQL (payments schema)

**API Endpoints**:
```
POST /api/v1/payments              # Process payment
POST /api/v1/payments/{id}/refund  # Process refund
GET  /api/v1/payments/{id}         # Get payment status
```

## Data Architecture

### Database Design

#### PostgreSQL Schema Structure
```sql
-- Bookings Schema
CREATE TABLE bookings (
    id UUID PRIMARY KEY,
    customer_id UUID NOT NULL,
    franchise_id UUID NOT NULL,
    booking_status VARCHAR(20) NOT NULL,
    start_datetime TIMESTAMP NOT NULL,
    end_datetime TIMESTAMP NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    payment_status VARCHAR(20) NOT NULL,
    reference_number UUID UNIQUE NOT NULL,
    qr_code_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE booking_children (
    id UUID PRIMARY KEY,
    booking_id UUID REFERENCES bookings(id),
    name VARCHAR(100) NOT NULL,
    age INTEGER NOT NULL,
    special_needs TEXT,
    allergies TEXT,
    pickup_authorization TEXT,
    special_instructions TEXT
);

CREATE TABLE customer_info (
    id UUID PRIMARY KEY,
    booking_id UUID REFERENCES bookings(id),
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    emergency_contact VARCHAR(255)
);

-- Franchises Schema
CREATE TABLE franchises (
    id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    city VARCHAR(50) NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    max_capacity INTEGER NOT NULL,
    standard_rate DECIMAL(8,2) NOT NULL,
    peak_hour_rate DECIMAL(8,2) NOT NULL,
    open_time TIME NOT NULL,
    close_time TIME NOT NULL,
    operating_days INTEGER[] NOT NULL, -- [1,2,3,4,5] for Mon-Fri
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Payments Schema
CREATE TABLE payments (
    id UUID PRIMARY KEY,
    booking_id UUID REFERENCES bookings(id),
    stripe_payment_id VARCHAR(100) UNIQUE,
    amount DECIMAL(10,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    payment_method VARCHAR(50) NOT NULL,
    payment_status VARCHAR(20) NOT NULL,
    processed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Redis Caching Strategy
```python
# Cache Keys Pattern
availability:{franchise_id}:{date}     # TTL: 5 minutes
pricing:{franchise_id}                 # TTL: 1 hour  
franchise:{franchise_id}               # TTL: 24 hours
capacity:{franchise_id}:{date}         # TTL: 5 minutes
```

## API Design

### REST API Specification

#### Create Booking
```http
POST /api/v1/bookings
Content-Type: application/json

{
  "franchise_id": "uuid",
  "start_datetime": "2024-01-15T09:00:00Z",
  "end_datetime": "2024-01-15T17:00:00Z",
  "customer_info": {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+1234567890",
    "emergency_contact": "Jane Doe +1234567891"
  },
  "child_info": {
    "name": "Alice Doe",
    "age": 5,
    "special_needs": "None",
    "allergies": "Peanuts",
    "pickup_authorization": "John Doe, Jane Doe",
    "special_instructions": "Likes to draw"
  }
}

Response: 201 Created
{
  "booking_id": "uuid",
  "reference_number": "uuid",
  "total_amount": 120.00,
  "currency": "USD",
  "payment_required": true,
  "payment_url": "https://checkout.stripe.com/..."
}
```

#### Check Availability
```http
GET /api/v1/availability/franchise-id?date=2024-01-15

Response: 200 OK
{
  "franchise_id": "uuid",
  "date": "2024-01-15",
  "operating_hours": {
    "open": "08:00",
    "close": "18:00"
  },
  "available_slots": [
    {
      "start_time": "09:00",
      "end_time": "10:00",
      "available_capacity": 5,
      "rate": 15.00
    }
  ],
  "pricing": {
    "standard_rate": 15.00,
    "peak_hour_rate": 22.50,
    "currency": "USD"
  }
}
```

## Event Architecture

### Event Publishing Strategy
**Pattern**: Fire-and-forget async events via AWS SQS
**Purpose**: Notify Admin Portal of booking changes

### Event Types
```json
// BookingCreated Event
{
  "event_type": "BookingCreated",
  "event_id": "uuid",
  "timestamp": "2024-01-01T10:00:00Z",
  "source": "customer-booking-service",
  "data": {
    "booking_id": "uuid",
    "franchise_id": "uuid",
    "start_datetime": "2024-01-15T09:00:00Z",
    "end_datetime": "2024-01-15T17:00:00Z",
    "customer_email": "john@example.com",
    "child_name": "Alice Doe"
  }
}

// PaymentProcessed Event
{
  "event_type": "PaymentProcessed", 
  "event_id": "uuid",
  "timestamp": "2024-01-01T10:05:00Z",
  "source": "customer-booking-service",
  "data": {
    "booking_id": "uuid",
    "payment_id": "uuid",
    "amount": 120.00,
    "currency": "USD"
  }
}

// BookingCancelled Event
{
  "event_type": "BookingCancelled",
  "event_id": "uuid", 
  "timestamp": "2024-01-01T15:00:00Z",
  "source": "customer-booking-service",
  "data": {
    "booking_id": "uuid",
    "cancellation_reason": "Customer request",
    "refund_amount": 100.00
  }
}
```

## Performance Architecture

### Caching Strategy
1. **Availability Cache**: 5-minute TTL for real-time availability
2. **Franchise Cache**: 24-hour TTL for franchise details
3. **Pricing Cache**: 1-hour TTL for pricing information

### Database Optimization
```sql
-- Performance Indexes
CREATE INDEX idx_bookings_franchise_date ON bookings(franchise_id, start_datetime);
CREATE INDEX idx_bookings_status ON bookings(booking_status);
CREATE INDEX idx_bookings_reference ON bookings(reference_number);
CREATE INDEX idx_franchises_active ON franchises(is_active);
```

### API Performance
- **Response Time Target**: < 200ms for availability checks
- **Throughput Target**: 1000 requests/minute per service
- **Connection Pooling**: PostgreSQL connection pool (10-20 connections)
- **Rate Limiting**: 100 requests/minute per IP

## Security Architecture

### Authentication & Authorization
```python
# JWT Token Structure
{
  "sub": "customer_id",
  "iat": 1640995200,
  "exp": 1640998800,
  "scope": ["booking:create", "booking:read", "booking:update"]
}
```

### Data Protection
- **PCI Compliance**: No card data stored (Stripe handles)
- **Data Encryption**: AES-256 for sensitive data at rest
- **API Security**: HTTPS only, API key authentication
- **Input Validation**: Pydantic models for request validation

### Security Headers
```python
# FastAPI Security Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
```

## Deployment Architecture

### Container Strategy
```dockerfile
# Dockerfile (simplified)
FROM python:3.11-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### AWS ECS Configuration
```yaml
# ECS Task Definition (simplified)
family: customer-booking-service
cpu: 512
memory: 1024
containers:
  - name: booking-api
    image: customer-booking:latest
    portMappings:
      - containerPort: 8000
        protocol: tcp
    environment:
      - DATABASE_URL: postgresql://...
      - REDIS_URL: redis://...
      - STRIPE_SECRET_KEY: sk_...
```

### Infrastructure Components
- **Load Balancer**: AWS ALB with health checks
- **Auto Scaling**: Target 70% CPU utilization
- **Database**: AWS RDS PostgreSQL (Multi-AZ)
- **Cache**: AWS ElastiCache Redis
- **Queue**: AWS SQS for event publishing
- **Storage**: AWS S3 for QR codes and documents

## Monitoring & Observability

### Health Checks
```python
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "database": await check_db_connection(),
        "cache": await check_redis_connection(),
        "timestamp": datetime.utcnow()
    }
```

### Metrics & Logging
- **Application Metrics**: Prometheus + Grafana
- **Logging**: Structured JSON logs to CloudWatch
- **Tracing**: AWS X-Ray for request tracing
- **Alerts**: CloudWatch alarms for errors and latency

## Error Handling & Resilience

### Circuit Breaker Pattern
```python
# External service calls with circuit breaker
@circuit_breaker(failure_threshold=5, timeout=30)
async def call_stripe_api(payment_data):
    # Stripe API call with fallback
    pass
```

### Retry Strategy
- **Database**: 3 retries with exponential backoff
- **External APIs**: 2 retries with 1s delay
- **Queue Publishing**: 5 retries with exponential backoff

### Graceful Degradation
- **Cache Miss**: Fallback to database query
- **Payment Service Down**: Queue payment for later processing
- **Event Publishing Failure**: Log and retry asynchronously

## Integration Patterns

### Admin Portal Integration
**Pattern**: Event-driven integration via SQS
**Anti-Corruption Layer**: Event adapters to translate domain events

### Payment Integration
**Pattern**: Adapter pattern for Stripe API
**Fallback**: Queue payments for retry on failure

### QR Code Generation
**Service**: Internal QR service using qrcode library
**Storage**: S3 with CDN for fast access

This logical design provides a simple, performant, and scalable foundation for the Customer Booking unit while maintaining clean architecture principles and domain-driven design patterns.