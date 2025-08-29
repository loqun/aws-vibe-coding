import axios, { type AxiosInstance, type AxiosResponse } from 'axios'
import type {
  Franchise,
  AvailabilityResponse,
  CreateBookingRequest,
  CreateBookingResponse,
  BookingDetails,
  ModifyBookingRequest,
  ModifyBookingResponse,
  CancelBookingResponse,
  PaymentRequest,
  PaymentResponse,
  QRCodeResponse,
  APIError
} from '@/types/api'

class ApiService {
  private api: AxiosInstance

  constructor() {
    this.api = axios.create({
      baseURL: import.meta.env.VITE_API_BASE_URL,
      timeout: 10000,
      headers: {
        'Content-Type': 'application/json'
      }
    })

    this.setupInterceptors()
  }

  private setupInterceptors() {
    this.api.interceptors.response.use(
      (response: AxiosResponse) => response,
      (error) => {
        const apiError: APIError = {
          error_code: error.response?.data?.error_code || 'UNKNOWN_ERROR',
          message: error.response?.data?.message || error.message,
          details: error.response?.data?.details
        }
        return Promise.reject(apiError)
      }
    )
  }

  // Franchise & Availability APIs
  async getFranchises(): Promise<Franchise[]> {
    const response = await this.api.get<Franchise[]>('/franchises')
    return response.data
  }

  async checkAvailability(franchiseId: string, date: string): Promise<AvailabilityResponse> {
    const response = await this.api.get<AvailabilityResponse>(
      `/availability/${franchiseId}?date=${date}`
    )
    return response.data
  }

  // Booking APIs
  async createBooking(bookingData: CreateBookingRequest): Promise<CreateBookingResponse> {
    const response = await this.api.post<CreateBookingResponse>('/bookings', bookingData)
    return response.data
  }

  async getBookingDetails(bookingId: string): Promise<BookingDetails> {
    const response = await this.api.get<BookingDetails>(`/bookings/${bookingId}`)
    return response.data
  }

  async modifyBooking(bookingId: string, changes: ModifyBookingRequest): Promise<ModifyBookingResponse> {
    const response = await this.api.put<ModifyBookingResponse>(`/bookings/${bookingId}`, changes)
    return response.data
  }

  async cancelBooking(bookingId: string): Promise<CancelBookingResponse> {
    const response = await this.api.delete<CancelBookingResponse>(`/bookings/${bookingId}`)
    return response.data
  }

  // Payment APIs
  async processPayment(paymentData: PaymentRequest): Promise<PaymentResponse> {
    const response = await this.api.post<PaymentResponse>('/payments', paymentData)
    return response.data
  }

  async getBookingQRCode(bookingId: string): Promise<QRCodeResponse> {
    const response = await this.api.get<QRCodeResponse>(`/bookings/${bookingId}/qr`)
    return response.data
  }
}

export const apiService = new ApiService()
export default apiService