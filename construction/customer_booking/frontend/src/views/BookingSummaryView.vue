<template>
  <div>
    <div class="text-center mb-10">
      <h2 class="text-3xl font-bold text-slate-900 mb-4">Booking Summary</h2>
      <p class="text-lg text-slate-600 max-w-2xl mx-auto">
        Please review your booking details and complete the payment to confirm your reservation.
      </p>
    </div>
    
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- Booking Details -->
      <div class="lg:col-span-2 space-y-6">
        <!-- Location & Time -->
        <div class="bg-slate-50 rounded-2xl p-6 border border-slate-200">
          <h3 class="text-lg font-semibold text-slate-900 mb-4 flex items-center">
            <svg class="w-5 h-5 mr-2 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
            </svg>
            Location & Schedule
          </h3>
          
          <div class="space-y-3">
            <div class="flex justify-between">
              <span class="text-slate-600">Franchise</span>
              <span class="font-medium">Downtown Kids Care</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-600">Date</span>
              <span class="font-medium">January 20, 2024</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-600">Time</span>
              <span class="font-medium">9:00 AM - 11:00 AM</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-600">Duration</span>
              <span class="font-medium">2 hours</span>
            </div>
          </div>
        </div>
        
        <!-- Customer Info -->
        <div class="bg-slate-50 rounded-2xl p-6 border border-slate-200">
          <h3 class="text-lg font-semibold text-slate-900 mb-4 flex items-center">
            <svg class="w-5 h-5 mr-2 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
            </svg>
            Contact Information
          </h3>
          
          <div class="space-y-3">
            <div class="flex justify-between">
              <span class="text-slate-600">Parent/Guardian</span>
              <span class="font-medium">John Doe</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-600">Email</span>
              <span class="font-medium">john@example.com</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-600">Phone</span>
              <span class="font-medium">(555) 123-4567</span>
            </div>
          </div>
        </div>
        
        <!-- Child Info -->
        <div class="bg-slate-50 rounded-2xl p-6 border border-slate-200">
          <h3 class="text-lg font-semibold text-slate-900 mb-4 flex items-center">
            <svg class="w-5 h-5 mr-2 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
            </svg>
            Child Information
          </h3>
          
          <div class="space-y-3">
            <div class="flex justify-between">
              <span class="text-slate-600">Name</span>
              <span class="font-medium">Alice Doe</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-600">Age</span>
              <span class="font-medium">5 years old</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-600">Allergies</span>
              <span class="font-medium">Peanuts</span>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Payment Section -->
      <div class="lg:col-span-1">
        <div class="bg-white rounded-2xl p-6 border-2 border-blue-200 shadow-lg sticky top-8">
          <h3 class="text-lg font-semibold text-slate-900 mb-6">Payment Summary</h3>
          
          <div class="space-y-4 mb-6">
            <div class="flex justify-between">
              <span class="text-slate-600">Childcare (2 hours)</span>
              <span class="font-medium">$30.00</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-600">Service Fee</span>
              <span class="font-medium">$2.50</span>
            </div>
            <div class="border-t border-slate-200 pt-4">
              <div class="flex justify-between text-lg font-bold">
                <span>Total</span>
                <span class="text-blue-600">$32.50</span>
              </div>
            </div>
          </div>
          
          <!-- Mock Payment Form -->
          <div class="space-y-4 mb-6">
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Card Number</label>
              <input 
                type="text" 
                placeholder="1234 5678 9012 3456"
                class="w-full rounded-xl border-slate-300 focus:border-blue-500 focus:ring-blue-500"
              >
            </div>
            
            <div class="grid grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">Expiry</label>
                <input 
                  type="text" 
                  placeholder="MM/YY"
                  class="w-full rounded-xl border-slate-300 focus:border-blue-500 focus:ring-blue-500"
                >
              </div>
              <div>
                <label class="block text-sm font-medium text-slate-700 mb-2">CVC</label>
                <input 
                  type="text" 
                  placeholder="123"
                  class="w-full rounded-xl border-slate-300 focus:border-blue-500 focus:ring-blue-500"
                >
              </div>
            </div>
          </div>
          
          <div class="mb-6">
            <label class="flex items-center">
              <input type="checkbox" class="rounded border-slate-300 text-blue-600 focus:ring-blue-500">
              <span class="ml-2 text-sm text-slate-600">
                I agree to the <a href="#" class="text-blue-600 hover:underline">Terms & Conditions</a>
              </span>
            </label>
          </div>
          
          <button 
            @click="completeBooking"
            class="w-full bg-gradient-to-r from-blue-600 to-blue-700 text-white font-semibold py-4 rounded-xl hover:from-blue-700 hover:to-blue-800 transition-all duration-200 shadow-lg hover:shadow-xl"
          >
            Complete Booking
          </button>
          
          <div class="mt-4 flex items-center justify-center text-sm text-slate-500">
            <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path>
            </svg>
            Secure payment powered by Stripe
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useBookingFlowStore } from '@/stores/bookingFlow'

const router = useRouter()
const bookingFlow = useBookingFlowStore()

function completeBooking() {
  bookingFlow.nextStep()
  router.push('/book/confirmation')
}
</script>