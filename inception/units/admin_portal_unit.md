# Admin Portal Unit

## Unit Overview
**Purpose:** Handle all administrative operations including QR workflow, franchise staff operations, management functions, reporting, and system configuration.

**Technology:** Web Application (Admin Domain)

**Dependencies:** Requires booking data from Customer Booking Unit

**Team:** Web Developers + Backend Developers

## QR Workflow User Stories

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

## Management User Stories

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

## Unit Interfaces

### Data Imports (from other units):
- Booking data from Customer Booking Unit
- Payment transaction data
- Customer and child information

### Data Exports (to other units):
- Capacity configuration (to Customer Booking Unit)
- Pricing settings (to Customer Booking Unit)
- Operating hours and availability (to Customer Booking Unit)

## Core Capabilities
1. **QR Code Scanning** - Access booking sessions via QR codes
2. **Check-in/Check-out Management** - Complete child drop-off and pickup workflow
3. **Photo Capture** - Parent identity verification system
4. **Additional Payment Processing** - Handle overtime and extra charges
5. **Capacity Management** - Configure franchise operational parameters
6. **Reporting and Analytics** - Business intelligence and operational reports
7. **Pricing Management** - Dynamic pricing configuration
8. **Emergency Management** - Safety and compliance procedures

## Admin Portal Sections
1. **Operations Dashboard** - Active bookings and QR scanning
2. **Management Console** - Capacity, pricing, and configuration
3. **Reports & Analytics** - Business intelligence and insights
4. **Emergency Center** - Safety procedures and incident management