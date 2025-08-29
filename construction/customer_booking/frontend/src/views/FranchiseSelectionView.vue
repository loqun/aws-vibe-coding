<template>
  <div>
    <div class="text-center mb-10">
      <h2 class="text-3xl font-bold text-slate-900 mb-4">Choose Your Location</h2>
      <p class="text-lg text-slate-600 max-w-2xl mx-auto">
        Select from our trusted franchise locations. Each location offers professional childcare with experienced staff.
      </p>
    </div>
    
    <!-- Mock franchise cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-10">
      <div 
        v-for="franchise in mockFranchises" 
        :key="franchise.id"
        class="group bg-gradient-to-br from-white to-slate-50 rounded-2xl p-6 border-2 border-slate-200 hover:border-blue-300 hover:shadow-xl transition-all duration-300 cursor-pointer transform hover:scale-[1.02]"
        @click="selectFranchise(franchise)"
      >
        <div class="flex items-start justify-between mb-4">
          <div>
            <h3 class="text-xl font-bold text-slate-900 mb-2">{{ franchise.name }}</h3>
            <p class="text-slate-600 flex items-center">
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
              </svg>
              {{ franchise.address }}
            </p>
          </div>
          <div class="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm font-medium">
            Open
          </div>
        </div>
        
        <div class="space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-slate-600 flex items-center">
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
              Hours
            </span>
            <span class="font-medium text-slate-900">{{ franchise.hours }}</span>
          </div>
          
          <div class="flex items-center justify-between">
            <span class="text-slate-600 flex items-center">
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1"></path>
              </svg>
              Rate
            </span>
            <span class="font-bold text-blue-600">${{ franchise.rate }}/hour</span>
          </div>
        </div>
        
        <div class="mt-6 pt-4 border-t border-slate-200">
          <button class="w-full bg-gradient-to-r from-blue-600 to-blue-700 text-white font-semibold py-3 rounded-xl hover:from-blue-700 hover:to-blue-800 transition-all duration-200 group-hover:shadow-lg">
            Select Location
          </button>
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

const mockFranchises = [
  {
    id: '1',
    name: 'Downtown Kids Care',
    address: '123 Main St, Seattle',
    hours: '8:00 AM - 6:00 PM',
    rate: 15
  },
  {
    id: '2',
    name: 'Westside Childcare',
    address: '456 Oak Ave, Seattle',
    hours: '7:00 AM - 7:00 PM',
    rate: 18
  }
]

function selectFranchise(franchise: any) {
  bookingFlow.nextStep()
  router.push('/book/datetime')
}
</script>