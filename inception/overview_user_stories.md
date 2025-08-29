# Babysitter Drop-off Franchise - User Stories

## Core User Stories

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

## Payment Processing Stories

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

## Booking Management Stories

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



## Admin QR Workflow Stories

### US-011: Scan QR Code for Booking Session
**As an** admin staff member  
**I want to** scan the customer's QR code  
**So that** I can access their booking session details  

**Acceptance Criteria:**
- Provide QR code scanner interface on admin device
- Decode QR code to retrieve booking session link
- Navigate to booking session page automatically
- Display error message for invalid QR codes
- Work offline with cached booking data if needed

### US-012: Check-in Child (Admin)
**As an** admin staff member  
**I want to** check in the child during drop-off  
**So that** the drop-off process is properly documented  

**Acceptance Criteria:**
- Verify booking details at check-in
- Confirm child identity and information
- Take photo of parent/guardian for pickup verification
- Record actual drop-off time
- Update booking status to "child checked in"
- Capture and store photo with booking record securely

### US-013: Check-out Child (Admin)
**As an** admin staff member  
**I want to** check out the child during pickup  
**So that** I can safely release the child and complete the booking  

**Acceptance Criteria:**
- Display complete booking information
- Show original booking time vs actual time
- Calculate overtime charges if applicable
- Display parent photo for identity verification
- Verify customer identity and pickup authorization
- Show child information and special notes
- Display any incident reports or notes from care period
- Record actual pickup time

### US-014: Process Additional Payment via QR
**As an** admin staff member  
**I want to** generate QR code for additional payments  
**So that** customers can pay for overtime or additional services  

**Acceptance Criteria:**
- Calculate additional charges (overtime, extras)
- Generate payment QR code for additional amount
- Display QR code for customer to scan with their device
- Process payment through customer's mobile payment app
- Confirm payment completion before releasing child
- Update booking record with additional payment

### US-015: Complete Booking Session
**As an** admin staff member  
**I want to** complete the booking session after pickup  
**So that** the booking is properly closed in the system  

**Acceptance Criteria:**
- Confirm all payments are completed (including additional charges)
- Add any final notes or observations
- Mark booking as completed in system
- Generate pickup receipt for customer
- Clear booking from active sessions list
- Update franchise capacity for the time slot

## Administrative Management Stories

### US-016: Manage Franchise Capacity
**As an** administrator  
**I want to** manage franchise capacity and availability  
**So that** bookings don't exceed our service capabilities  

**Acceptance Criteria:**
- Set maximum capacity per time slot
- Configure operating hours and days
- Set holiday schedules and closures
- Adjust capacity for special events
- View real-time capacity utilization

### US-017: View Drop-off Reports
**As an** administrator  
**I want to** view booking and operational reports  
**So that** I can monitor franchise performance  

**Acceptance Criteria:**
- Display booking statistics by date range
- Show revenue reports and capacity utilization
- Display customer booking patterns
- Show check-in/check-out logs
- Export reports to CSV/PDF

### US-018: Manage Pricing
**As an** administrator  
**I want to** manage hourly rates and pricing  
**So that** I can adjust pricing based on demand  

**Acceptance Criteria:**
- Set standard hourly rates
- Configure peak hour pricing
- Set holiday and weekend rates
- Apply promotional discounts
- Schedule future pricing changes

## Safety and Compliance Stories

### US-019: Emergency Contact Management
**As an** administrator  
**I want to** manage emergency procedures and contacts  
**So that** we can handle emergencies properly  

**Acceptance Criteria:**
- Maintain emergency contact database
- Record child medical information and allergies
- Document emergency procedures
- Track incident reports
- Notify parents of any incidents

## Future Interface Stories (Not Implemented Initially)

### US-020: Recurring Drop-off Interface
**As a** guest customer  
**I want to** set up recurring drop-off bookings  
**So that** I can have regular childcare services  

**Acceptance Criteria:**
- Interface for setting recurring patterns (weekly, bi-weekly, monthly)
- Ability to specify end date for recurring bookings
- Automatic booking creation based on pattern
- Notification of scheduling conflicts

### US-021: Notification Interface
**As a** guest customer  
**I want to** receive notifications about my bookings  
**So that** I stay informed about my reservations  

**Acceptance Criteria:**
- Interface for notification preferences (email, SMS, in-app)
- Booking confirmation notifications
- Reminder notifications before scheduled drop-off
- Check-in/check-out notifications
- Emergency notifications if needed