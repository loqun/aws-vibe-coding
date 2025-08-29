<template>
  <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <!-- Progress indicator -->
    <div class="mb-12">
      <div class="flex items-center justify-between relative">
        <!-- Progress line -->
        <div class="absolute top-4 left-0 w-full h-0.5 bg-slate-200 -z-10"></div>
        <div 
          class="absolute top-4 left-0 h-0.5 bg-gradient-to-r from-blue-500 to-blue-600 transition-all duration-500 -z-10"
          :style="{ width: `${(bookingFlow.currentStep / (steps.length - 1)) * 100}%` }"
        ></div>
        
        <div v-for="(step, index) in steps" :key="index" class="flex flex-col items-center relative">
          <div 
            :class="[
              'flex items-center justify-center w-8 h-8 rounded-full text-sm font-bold transition-all duration-300 bg-white border-2',
              index <= bookingFlow.currentStep 
                ? 'border-blue-500 bg-blue-500 text-white shadow-lg' 
                : 'border-slate-300 text-slate-400'
            ]"
          >
            <svg 
              v-if="index < bookingFlow.currentStep" 
              class="w-4 h-4" 
              fill="currentColor" 
              viewBox="0 0 20 20"
            >
              <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
            </svg>
            <span v-else>{{ index + 1 }}</span>
          </div>
          <span 
            :class="[
              'mt-3 text-sm font-medium text-center max-w-20',
              index <= bookingFlow.currentStep ? 'text-blue-600' : 'text-slate-500'
            ]"
          >
            {{ step }}
          </span>
        </div>
      </div>
    </div>

    <!-- Content area with card styling -->
    <div class="bg-white rounded-3xl shadow-lg border border-slate-100 overflow-hidden">
      <div class="p-8 md:p-12">
        <RouterView />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useBookingFlowStore } from '@/stores/bookingFlow'

const bookingFlow = useBookingFlowStore()

const steps = [
  'Franchise',
  'Date & Time', 
  'Information',
  'Summary',
  'Confirmation'
]
</script>