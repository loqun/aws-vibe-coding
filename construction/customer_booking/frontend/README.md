# Customer Booking Frontend

A modern Vue 3 + TypeScript frontend application for the babysitter franchise booking system.

## Features

- **Booking Flow**: Complete customer booking workflow from franchise selection to payment confirmation
- **Responsive Design**: Mobile-first design with Tailwind CSS
- **State Management**: Pinia stores for application state
- **Type Safety**: Full TypeScript support
- **Modern UI**: Clean, accessible interface components

## Tech Stack

- Vue 3 with Composition API
- TypeScript
- Pinia for state management
- Vue Router for navigation
- Tailwind CSS for styling
- Axios for API calls
- Stripe Elements for payments
- Vite for build tooling

## Setup Instructions

### Prerequisites
- Node.js 18+ 
- npm or yarn

### Installation

1. Clone the repository and navigate to the frontend directory:
```bash
cd construction/customer_booking/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Copy environment variables:
```bash
cp .env.example .env
```

4. Update `.env` with your configuration:
```env
VITE_API_BASE_URL=http://localhost:8000/api/v1
VITE_STRIPE_PUBLIC_KEY=your_stripe_public_key
VITE_APP_NAME=Babysitter Booking
```

### Development

Start the development server:
```bash
npm run dev
```

The application will be available at `http://localhost:5173`

### Build for Production

```bash
npm run build
```

### Preview Production Build

```bash
npm run preview
```

## Project Structure

```
src/
├── components/          # Reusable UI components
├── views/              # Page components
├── stores/             # Pinia stores
├── services/           # API services
├── types/              # TypeScript interfaces
├── utils/              # Utility functions
├── assets/             # Static assets
└── router/             # Vue Router configuration
```

## User Workflows

### Booking Flow
1. **Franchise Selection** - Choose from available franchise locations
2. **Date & Time Selection** - Pick date and time slots with real-time availability
3. **Information Entry** - Provide customer and child information
4. **Booking Summary** - Review details and process payment
5. **Confirmation** - Receive booking confirmation with QR code

### Booking Management
- Look up existing bookings by reference number
- View booking details and QR codes
- Modify booking dates/times (when available)
- Cancel bookings with refund processing

## API Integration

The frontend integrates with the backend API for:
- Franchise data and availability checking
- Booking creation and management
- Payment processing via Stripe
- QR code generation

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `VITE_API_BASE_URL` | Backend API base URL | `http://localhost:8000/api/v1` |
| `VITE_STRIPE_PUBLIC_KEY` | Stripe publishable key | - |
| `VITE_APP_NAME` | Application name | `Babysitter Booking` |

## Contributing

1. Follow the existing code style and patterns
2. Use TypeScript for all new code
3. Add proper error handling and loading states
4. Ensure responsive design works on all screen sizes
5. Test booking flow end-to-end before submitting

## Troubleshooting

### Common Issues

**Build fails with Tailwind CSS errors:**
- Ensure PostCSS and Tailwind are properly configured
- Check that all Tailwind classes are valid

**API calls fail:**
- Verify `VITE_API_BASE_URL` is correct
- Check that backend server is running
- Ensure CORS is configured on backend

**Stripe integration issues:**
- Verify `VITE_STRIPE_PUBLIC_KEY` is set
- Check Stripe dashboard for test/live mode settings