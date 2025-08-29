# Customer Booking Unit - Function Specification

## Overview
This document defines the frontend requirements and API contracts for the Customer Booking unit based on the logical design and user stories.

## API Contracts

### Base Configuration
```typescript
const API_BASE_URL = 'https://api.babysitter-booking.com/v1';
const API_TIMEOUT = 10000; // 10 seconds
```

### Authentication
```typescript
interface AuthHeaders {
  'Authorization': `Bearer ${jwt_token}`;
  'Content-Type': 'application/json';
  'X-API-Key': string;
}
```

## Core API Functions

### 1. Franchise & Availability APIs

#### Get Franchises List
```typescript
interface Franchise {
  id: string;
  name: string;
  address: string;
  city: string;
  postal_code: string;
  operating_hours: {
    open_time: string; // "08:00"
    close_time: string; // "18:00"
    operating_days: number[]; // [1,2,3,4,5]
  };
  pricing: {
    standard_rate: number;
    peak_hour_rate: number;
    currency: string;
  };
}

async function getFranchises(): Promise<Franchise[]> {
  const response = await fetch(`${API_BASE_URL}/franchises`);
  return response.json();
}
```

#### Check Availability
```typescript
interface AvailabilitySlot {
  start_time: string; // "09:00"
  end_time: string; // "10:00"
  available_capacity: number;
  rate: number;
  is_peak_hour: boolean;
}

interface AvailabilityResponse {
  franchise_id: string;
  date: string; // "2024-01-15"
  operating_hours: {
    open: string;
    close: string;
  };
  available_slots: AvailabilitySlot[];
  pricing: {
    standard_rate: number;
    peak_hour_rate: number;
    currency: string;
  };
}

async function checkAvailability(
  franchiseId: string, 
  date: string
): Promise<AvailabilityResponse> {
  const response = await fetch(
    `${API_BASE_URL}/availability/${franchiseId}?date=${date}`
  );
  return response.json();
}
```

### 2. Booking APIs

#### Create Booking
```typescript
interface CustomerInfo {
  name: string;
  email: string;
  phone: string;
  emergency_contact: string;
}

interface ChildInfo {
  name: string;
  age: number;
  special_needs?: string;
  allergies?: string;
  pickup_authorization: string;
  special_instructions?: string;
}

interface CreateBookingRequest {
  franchise_id: string;
  start_datetime: string; // ISO 8601
  end_datetime: string; // ISO 8601
  customer_info: CustomerInfo;
  child_info: ChildInfo;
}

interface CreateBookingResponse {
  booking_id: string;
  reference_number: string;
  total_amount: number;
  currency: string;
  payment_required: boolean;
  payment_url?: string; // Stripe checkout URL
}

async function createBooking(
  bookingData: CreateBookingRequest
): Promise<CreateBookingResponse> {
  const response = await fetch(`${API_BASE_URL}/bookings`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(bookingData)
  });
  return response.json();
}
```

#### Get Booking Details
```typescript
interface BookingDetails {
  booking_id: string;
  reference_number: string;
  franchise_info: {
    name: string;
    address: string;
    phone: string;
  };
  booking_status: 'pending' | 'confirmed' | 'cancelled' | 'completed';
  start_datetime: string;
  end_datetime: string;
  duration_hours: number;
  total_amount: number;
  currency: string;
  payment_status: 'pending' | 'completed' | 'failed' | 'refunded';
  customer_info: CustomerInfo;
  child_info: ChildInfo;
  qr_code_url?: string;
  created_at: string;
}

async function getBookingDetails(bookingId: string): Promise<BookingDetails> {
  const response = await fetch(`${API_BASE_URL}/bookings/${bookingId}`);
  return response.json();
}
```

#### Modify Booking
```typescript
interface ModifyBookingRequest {
  start_datetime?: string;
  end_datetime?: string;
  child_info?: Partial<ChildInfo>;
}

interface ModifyBookingResponse {
  booking_id: string;
  changes_applied: string[];
  price_difference: number;
  new_total_amount: number;
  additional_payment_required: boolean;
  payment_url?: string;
}

async function modifyBooking(
  bookingId: string,
  changes: ModifyBookingRequest
): Promise<ModifyBookingResponse> {
  const response = await fetch(`${API_BASE_URL}/bookings/${bookingId}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(changes)
  });
  return response.json();
}
```

#### Cancel Booking
```typescript
interface CancelBookingResponse {
  booking_id: string;
  cancellation_confirmed: boolean;
  refund_amount: number;
  refund_policy_applied: string;
  estimated_refund_date: string;
}

async function cancelBooking(bookingId: string): Promise<CancelBookingResponse> {
  const response = await fetch(`${API_BASE_URL}/bookings/${bookingId}`, {
    method: 'DELETE'
  });
  return response.json();
}
```

### 3. Payment APIs

#### Process Payment
```typescript
interface PaymentRequest {
  booking_id: string;
  payment_method_id: string; // Stripe payment method ID
}

interface PaymentResponse {
  payment_id: string;
  status: 'succeeded' | 'requires_action' | 'failed';
  client_secret?: string; // For 3D Secure
  booking_confirmed: boolean;
}

async function processPayment(
  paymentData: PaymentRequest
): Promise<PaymentResponse> {
  const response = await fetch(`${API_BASE_URL}/payments`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(paymentData)
  });
  return response.json();
}
```

#### Get QR Code
```typescript
interface QRCodeResponse {
  booking_id: string;
  qr_code_url: string;
  qr_code_data: string; // Base64 encoded
}

async function getBookingQRCode(bookingId: string): Promise<QRCodeResponse> {
  const response = await fetch(`${API_BASE_URL}/bookings/${bookingId}/qr`);
  return response.json();
}
```

## Frontend Component Requirements

### 1. Franchise Selection Component
```typescript
interface FranchiseSelectionProps {
  onFranchiseSelect: (franchise: Franchise) => void;
}

// Required Features:
// - Display list of available franchises
// - Show franchise details (name, address, hours)
// - Display pricing information
// - Filter by location/distance
```

### 2. Date & Time Selection Component
```typescript
interface DateTimeSelectionProps {
  franchiseId: string;
  onSlotSelect: (startTime: string, endTime: string) => void;
}

// Required Features:
// - Calendar widget for date selection
// - Time slot grid showing availability
// - Real-time capacity updates
// - Pricing display per slot
// - Prevent past date selection
```

### 3. Customer Information Form
```typescript
interface CustomerFormProps {
  onSubmit: (customerInfo: CustomerInfo) => void;
  initialData?: Partial<CustomerInfo>;
}

// Required Features:
// - Form validation (email, phone format)
// - Required field indicators
// - Emergency contact field
// - Auto-save to localStorage
```

### 4. Child Information Form
```typescript
interface ChildFormProps {
  onSubmit: (childInfo: ChildInfo) => void;
  initialData?: Partial<ChildInfo>;
}

// Required Features:
// - Age validation (1-12 years)
// - Special needs text area
// - Allergies checklist + custom input
// - Pickup authorization multi-select
// - Special instructions text area
```

### 5. Booking Summary Component
```typescript
interface BookingSummaryProps {
  bookingData: CreateBookingRequest;
  totalAmount: number;
  onConfirm: () => void;
  onEdit: () => void;
}

// Required Features:
// - Display all booking details
// - Show cost breakdown
// - Edit buttons for each section
// - Terms and conditions checkbox
```

### 6. Payment Component
```typescript
interface PaymentComponentProps {
  bookingId: string;
  amount: number;
  onPaymentSuccess: (paymentId: string) => void;
  onPaymentError: (error: string) => void;
}

// Required Features:
// - Stripe Elements integration
// - Card input validation
// - 3D Secure handling
// - Loading states
// - Error handling
```

### 7. Booking Confirmation Component
```typescript
interface BookingConfirmationProps {
  bookingDetails: BookingDetails;
  qrCodeUrl: string;
}

// Required Features:
// - Display confirmation details
// - Show QR code for admin scanning
// - Email confirmation button
// - Add to calendar button
// - Print/download receipt
```

### 8. Booking Management Component
```typescript
interface BookingManagementProps {
  bookingId: string;
}

// Required Features:
// - Display current booking status
// - Modify booking button
// - Cancel booking button
// - Cancellation policy display
// - Refund calculator
```

## User Interface Specifications

### 1. Booking Flow Pages

#### Page 1: Franchise Selection
```
Layout: Grid of franchise cards
Elements:
- Franchise name and address
- Operating hours display
- Pricing information
- "Select" button
- Map integration (optional)
```

#### Page 2: Date & Time Selection
```
Layout: Calendar + Time slots grid
Elements:
- Date picker calendar
- Available time slots (hourly grid)
- Capacity indicators (green/yellow/red)
- Pricing per slot
- Duration selector
- "Continue" button
```

#### Page 3: Information Forms
```
Layout: Two-column form layout
Elements:
- Customer info form (left column)
- Child info form (right column)
- Progress indicator
- "Back" and "Continue" buttons
```

#### Page 4: Booking Summary & Payment
```
Layout: Summary + Payment form
Elements:
- Booking details summary
- Cost breakdown
- Payment form (Stripe Elements)
- Terms checkbox
- "Complete Booking" button
```

#### Page 5: Confirmation
```
Layout: Confirmation details + QR code
Elements:
- Booking confirmation message
- QR code display
- Booking details
- Action buttons (email, calendar, print)
```

### 2. Booking Management Pages

#### My Bookings Page
```
Layout: List of bookings with actions
Elements:
- Booking cards with status
- Quick actions (modify, cancel)
- Search/filter options
- Pagination
```

#### Booking Details Page
```
Layout: Detailed view with actions
Elements:
- Complete booking information
- QR code display
- Modification form
- Cancellation options
```

## Error Handling

### API Error Responses
```typescript
interface APIError {
  error_code: string;
  message: string;
  details?: Record<string, any>;
}

// Common Error Codes:
// - FRANCHISE_NOT_AVAILABLE
// - BOOKING_CAPACITY_EXCEEDED
// - PAYMENT_FAILED
// - BOOKING_NOT_FOUND
// - VALIDATION_ERROR
```

### Frontend Error Handling
```typescript
// Error Display Component
interface ErrorDisplayProps {
  error: APIError;
  onRetry?: () => void;
  onDismiss?: () => void;
}

// Global Error Handler
function handleAPIError(error: APIError): void {
  switch (error.error_code) {
    case 'FRANCHISE_NOT_AVAILABLE':
      showNotification('Franchise is not available for selected time');
      break;
    case 'PAYMENT_FAILED':
      showPaymentErrorModal(error.details);
      break;
    default:
      showGenericError(error.message);
  }
}
```

## State Management

### Booking Flow State
```typescript
interface BookingFlowState {
  currentStep: number;
  selectedFranchise?: Franchise;
  selectedDateTime?: {
    start: string;
    end: string;
  };
  customerInfo?: CustomerInfo;
  childInfo?: ChildInfo;
  bookingId?: string;
  paymentStatus?: string;
}
```

### Global App State
```typescript
interface AppState {
  user?: User;
  bookingFlow: BookingFlowState;
  userBookings: BookingDetails[];
  loading: boolean;
  errors: APIError[];
}
```

## Performance Requirements

### Loading States
- API calls: Show loading spinners
- Page transitions: Skeleton screens
- Form submissions: Disable buttons with loading text

### Caching Strategy
- Franchise data: Cache for 1 hour
- Availability data: Cache for 5 minutes
- User bookings: Cache until refresh

### Responsive Design
- Mobile-first approach
- Breakpoints: 320px, 768px, 1024px, 1440px
- Touch-friendly buttons (min 44px)

This function specification provides all the necessary contracts and requirements for building a complete frontend application for the Customer Booking unit.