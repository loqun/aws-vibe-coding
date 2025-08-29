# Customer Booking Unit

## Unit Overview
**Purpose:** Handle all customer-facing booking operations including availability checking, booking creation, payment processing, and booking management.

**Technology:** Web Application (Customer Domain)

**Dependencies:** None (can be built independently)

**Team:** Frontend + Backend Web Developers

## User Stories

### US-001: Check Franchise Availability
**As a** guest customer  
**I want to** check if the babysitter franchise is available for my desired date and time  
**So that** I can plan to drop off my child  

**Acceptance Criteria:**
- Display franchise operating hours
- Show available time slots in 1-hour intervals
- Display current capacity status
- Prevent selection of past dates/times
- Show pricing per hour

### US-002: Select Drop-off Date and Time
**As a** guest customer  
**I want to** select a specific date and time for dropping off my child  
**So that** I can book a time slot at the franchise  

**Acceptance Criteria:**
- Provide calendar interface for date selection
- Show available time slots in 1-hour intervals
- Display franchise capacity for selected date/time
- Prevent overbooking beyond franchise capacity
- Show total cost for selected duration

### US-003: Provide Child Information
**As a** guest customer  
**I want to** provide my child's information during booking  
**So that** the franchise can properly care for my child  

**Acceptance Criteria:**
- Capture child's name and age
- Record any special needs or allergies
- Capture emergency contact information
- Record pickup authorization details
- Allow special instructions or notes

### US-004: Create Drop-off Booking
**As a** guest customer  
**I want to** create a booking for dropping off my child  
**So that** I can secure a time slot at the franchise  

**Acceptance Criteria:**
- Allow selection of date, time, and duration
- Capture customer contact information
- Record child information and special requirements
- Calculate total cost based on duration and hourly rate
- Generate booking confirmation number

### US-005: Process Payment
**As a** guest customer  
**I want to** pay for my drop-off booking  
**So that** I can confirm my reservation  

**Acceptance Criteria:**
- Accept credit/debit card payments
- Display booking summary with child details and total cost
- Process payment securely
- Send payment confirmation
- Update booking status to confirmed upon successful payment

### US-006: View Booking Confirmation
**As a** guest customer  
**I want to** receive booking confirmation details  
**So that** I have proof of my reservation and drop-off instructions  

**Acceptance Criteria:**
- Display booking confirmation with all details
- Show franchise location and contact information
- Display date, time, duration, and total cost
- Show child information and special instructions
- Provide booking reference number and drop-off procedures
- Generate QR code for admin scanning
- Send confirmation email with QR code attached

### US-007: Cancel Drop-off Booking
**As a** guest customer  
**I want to** cancel my drop-off booking  
**So that** I can get a refund if my plans change  

**Acceptance Criteria:**
- Allow cancellation using booking reference number
- Display cancellation policy and refund amount
- Process refund according to cancellation policy
- Send cancellation confirmation
- Update booking status to cancelled

### US-008: Modify Drop-off Booking
**As a** guest customer  
**I want to** modify my existing drop-off booking  
**So that** I can adjust the time or duration if needed  

**Acceptance Criteria:**
- Allow modification using booking reference number
- Check franchise availability for new time/date
- Verify capacity for modified booking
- Calculate price difference for changes
- Process additional payment or refund as needed

## Unit Interfaces

### Data Exports (to other units):
- Booking data (for admin operations)
- Capacity utilization data (for franchise management)
- Payment transaction data (for reporting)

### Data Imports (from other units):
- Franchise capacity settings
- Pricing configuration
- Operating hours and availability

## Core Capabilities
1. **Availability Management** - Real-time capacity checking
2. **Booking Creation** - Complete booking workflow
3. **Payment Processing** - Secure payment handling
4. **Booking Management** - Cancellation and modification
5. **QR Code Generation** - For admin workflow integration
6. **Email Notifications** - Booking confirmations and updates