// Store state interfaces
import type { Franchise, BookingDetails, CustomerInfo, ChildInfo, APIError } from './api'

export interface BookingFlowState {
  currentStep: number
  selectedFranchise?: Franchise
  selectedDateTime?: {
    start: string
    end: string
  }
  customerInfo?: CustomerInfo
  childInfo?: ChildInfo
  bookingId?: string
  paymentStatus?: string
}

export interface AppState {
  bookingFlow: BookingFlowState
  userBookings: BookingDetails[]
  loading: boolean
  errors: APIError[]
}