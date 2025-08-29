<template>
  <div>
    <div class="text-center mb-10">
      <h2 class="text-3xl font-bold text-slate-900 mb-4">Your Information</h2>
      <p class="text-lg text-slate-600 max-w-2xl mx-auto">
        Please provide your contact details and your child's information for a safe and personalized care experience.
      </p>
    </div>
    
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      <!-- Customer Information -->
      <div class="bg-slate-50 rounded-2xl p-6 border border-slate-200">
        <h3 class="text-xl font-semibold text-slate-900 mb-6 flex items-center">
          <svg class="w-5 h-5 mr-2 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
          </svg>
          Parent/Guardian Information
        </h3>
        
        <div class="space-y-4">
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Full Name *</label>
            <input 
              v-model="customerInfo.name"
              type="text" 
              class="w-full rounded-xl border-slate-300 focus:border-primary-500 focus:ring-primary-500 transition-colors"
              placeholder="Enter your full name"
            >
          </div>
          
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Email Address *</label>
            <input 
              v-model="customerInfo.email"
              type="email" 
              class="w-full rounded-xl border-slate-300 focus:border-primary-500 focus:ring-primary-500 transition-colors"
              placeholder="your.email@example.com"
            >
          </div>
          
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Phone Number *</label>
            <input 
              v-model="customerInfo.phone"
              type="tel" 
              class="w-full rounded-xl border-slate-300 focus:border-primary-500 focus:ring-primary-500 transition-colors"
              placeholder="(555) 123-4567"
            >
          </div>
          
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Emergency Contact *</label>
            <input 
              v-model="customerInfo.emergencyContact"
              type="text" 
              class="w-full rounded-xl border-slate-300 focus:border-primary-500 focus:ring-primary-500 transition-colors"
              placeholder="Name and phone number"
            >
          </div>
        </div>
      </div>
      
      <!-- Child Information -->
      <div class="bg-slate-50 rounded-2xl p-6 border border-slate-200">
        <h3 class="text-xl font-semibold text-slate-900 mb-6 flex items-center">
          <svg class="w-5 h-5 mr-2 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
          </svg>
          Child Information
        </h3>
        
        <div class="space-y-4">
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Child's Name *</label>
              <input 
                v-model="childInfo.name"
                type="text" 
                class="w-full rounded-xl border-slate-300 focus:border-primary-500 focus:ring-primary-500 transition-colors"
                placeholder="Child's name"
              >
            </div>
            
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-2">Age *</label>
              <select 
                v-model="childInfo.age"
                class="w-full rounded-xl border-slate-300 focus:border-primary-500 focus:ring-primary-500 transition-colors"
              >
                <option value="">Select age</option>
                <option v-for="age in 12" :key="age" :value="age">{{ age }} years old</option>
              </select>
            </div>
          </div>
          
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Allergies</label>
            <input 
              v-model="childInfo.allergies"
              type="text" 
              class="w-full rounded-xl border-slate-300 focus:border-primary-500 focus:ring-primary-500 transition-colors"
              placeholder="Any food allergies or medical conditions"
            >
          </div>
          
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Pickup Authorization *</label>
            <input 
              v-model="childInfo.pickupAuth"
              type="text" 
              class="w-full rounded-xl border-slate-300 focus:border-primary-500 focus:ring-primary-500 transition-colors"
              placeholder="Who is authorized to pick up your child"
            >
          </div>
          
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-2">Special Instructions</label>
            <textarea 
              v-model="childInfo.instructions"
              rows="3"
              class="w-full rounded-xl border-slate-300 focus:border-primary-500 focus:ring-primary-500 transition-colors resize-none"
              placeholder="Any special care instructions, preferences, or notes"
            ></textarea>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Continue Button -->
    <div class="mt-10 pt-8 border-t border-slate-200">
      <button 
        @click="continueToNext"
        :disabled="!isFormValid"
        class="w-full bg-gradient-to-r from-blue-600 to-blue-700 text-white font-semibold py-4 rounded-xl hover:from-blue-700 hover:to-blue-800 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200"
      >
        Continue to Summary
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useBookingFlowStore } from '@/stores/bookingFlow'

const router = useRouter()
const bookingFlow = useBookingFlowStore()

const customerInfo = ref({
  name: '',
  email: '',
  phone: '',
  emergencyContact: ''
})

const childInfo = ref({
  name: '',
  age: '',
  allergies: '',
  pickupAuth: '',
  instructions: ''
})

const isFormValid = computed(() => {
  return customerInfo.value.name && 
         customerInfo.value.email && 
         customerInfo.value.phone && 
         customerInfo.value.emergencyContact &&
         childInfo.value.name && 
         childInfo.value.age &&
         childInfo.value.pickupAuth
})

function continueToNext() {
  bookingFlow.nextStep()
  router.push('/book/summary')
}
</script>