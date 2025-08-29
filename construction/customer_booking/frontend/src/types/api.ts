// API Response/Request interfaces based on functional specification

export interface Franchise {
  id: string
  name: string
  address: string
  city: string
  postal_code: string
  operating_hours: {
    open_time: string
    close_time: string
    operating_days: number[]
  }
  pricing: {
    standard_rate: number
    peak_hour_rate: number
    currency: string
  }
}

export interface AvailabilitySlot {
  start_time: string
  end_time: string
  available_capacity: number
  rate: number
  is_peak_hour: boolean
}

export interface AvailabilityResponse {
  franchise_id: string
  date: string
  operating_hours: {
    open: string
    close: string
  }
  available_slots: AvailabilitySlot[]
  pricing: {
    standard_rate: number
    peak_hour_rate: number
    currency: string
  }
}

export interface CustomerInfo {
  name: string
  email: string
  phone: string
  emergency_contact: string
}

export interface ChildInfo {
  name: string
  age: number
  special_needs?: string
  allergies?: string
  pickup_authorization: string
  special_instructions?: string
}

export interface CreateBookingRequest {
  franchise_id: string
  start_datetime: string
  end_datetime: string
  customer_info: CustomerInfo
  child_info: ChildInfo
}

export interface CreateBookingResponse {
  booking_id: string
  reference_number: string
  total_amount: number
  currency: string
  payment_required: boolean
  payment_url?: string
}

export interface BookingDetails {
  booking_id: string
  reference_number: string
  franchise_info: {
    name: string
    address: string
    phone: string
  }
  booking_status: 'pending' | 'confirmed' | 'cancelled' | 'completed'
  start_datetime: string
  end_datetime: string
  duration_hours: number
  total_amount: number
  currency: string
  payment_status: 'pending' | 'completed' | 'failed' | 'refunded'
  customer_info: CustomerInfo
  child_info: ChildInfo
  qr_code_url?: string
  created_at: string
}

export interface ModifyBookingRequest {
  start_datetime?: string
  end_datetime?: string
  child_info?: Partial<ChildInfo>
}

export interface ModifyBookingResponse {
  booking_id: string
  changes_applied: string[]
  price_difference: number
  new_total_amount: number
  additional_payment_required: boolean
  payment_url?: string
}

export interface CancelBookingResponse {
  booking_id: string
  cancellation_confirmed: boolean
  refund_amount: number
  refund_policy_applied: string
  estimated_refund_date: string
}

export interface PaymentRequest {
  booking_id: string
  payment_method_id: string
}

export interface PaymentResponse {
  payment_id: string
  status: 'succeeded' | 'requires_action' | 'failed'
  client_secret?: string
  booking_confirmed: boolean
}

export interface QRCodeResponse {
  booking_id: string
  qr_code_url: string
  qr_code_data: string
}

export interface APIError {
  error_code: string
  message: string
  details?: Record<string, any>
}