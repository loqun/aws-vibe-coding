// Mock API responses for development
import type {
  Franchise,
  AvailabilityResponse,
  CreateBookingResponse,
  BookingDetails
} from '@/types/api'

export const mockFranchises: Franchise[] = [
  {
    id: '1',
    name: 'Downtown Kids Care',
    address: '123 Main St',
    city: 'Seattle',
    postal_code: '98101',
    operating_hours: {
      open_time: '08:00',
      close_time: '18:00',
      operating_days: [1, 2, 3, 4, 5]
    },
    pricing: {
      standard_rate: 15.00,
      peak_hour_rate: 22.50,
      currency: 'USD'
    }
  },
  {
    id: '2',
    name: 'Westside Childcare',
    address: '456 Oak Ave',
    city: 'Seattle',
    postal_code: '98102',
    operating_hours: {
      open_time: '07:00',
      close_time: '19:00',
      operating_days: [1, 2, 3, 4, 5, 6]
    },
    pricing: {
      standard_rate: 18.00,
      peak_hour_rate: 25.00,
      currency: 'USD'
    }
  }
]

export const mockAvailability: AvailabilityResponse = {
  franchise_id: '1',
  date: '2024-01-15',
  operating_hours: {
    open: '08:00',
    close: '18:00'
  },
  available_slots: [
    {
      start_time: '09:00',
      end_time: '10:00',
      available_capacity: 5,
      rate: 15.00,
      is_peak_hour: false
    },
    {
      start_time: '10:00',
      end_time: '11:00',
      available_capacity: 3,
      rate: 15.00,
      is_peak_hour: false
    },
    {
      start_time: '15:00',
      end_time: '16:00',
      available_capacity: 2,
      rate: 22.50,
      is_peak_hour: true
    }
  ],
  pricing: {
    standard_rate: 15.00,
    peak_hour_rate: 22.50,
    currency: 'USD'
  }
}