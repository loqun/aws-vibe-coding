<template>
  <div>
    <div class="text-center mb-10">
      <h2 class="text-3xl font-bold text-slate-900 mb-4">Select Date & Time</h2>
      <p class="text-lg text-slate-600 max-w-2xl mx-auto">
        Choose your preferred date and time slots. All times shown are available with current capacity.
      </p>
    </div>
    
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      <!-- Date Selection -->
      <div>
        <h3 class="text-xl font-semibold text-slate-900 mb-6 flex items-center">
          <svg class="w-5 h-5 mr-2 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
          </svg>
          Select Date
        </h3>
        
        <!-- Mock calendar -->
        <div class="bg-slate-50 rounded-2xl p-6 border border-slate-200">
          <div class="text-center mb-4">
            <h4 class="text-lg font-semibold text-slate-900">January 2024</h4>
          </div>
          
          <div class="grid grid-cols-7 gap-2 mb-4">
            <div v-for="day in ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']" :key="day" class="text-center text-sm font-medium text-slate-600 py-2">
              {{ day }}
            </div>
          </div>
          
          <div class="grid grid-cols-7 gap-2">
            <div v-for="date in mockDates" :key="date.day" 
                 :class="[
                   'text-center py-3 rounded-lg cursor-pointer transition-all duration-200',
                   date.available 
                     ? 'hover:bg-blue-100 hover:text-blue-700' 
                     : 'text-slate-300 cursor-not-allowed',
                   selectedDate === date.day 
                     ? 'bg-blue-600 text-white' 
                     : 'text-slate-700'
                 ]"
                 @click="date.available && selectDate(date.day)">
              {{ date.day }}
            </div>
          </div>
        </div>
      </div>
      
      <!-- Time Selection -->
      <div>
        <h3 class="text-xl font-semibold text-slate-900 mb-6 flex items-center">
          <svg class="w-5 h-5 mr-2 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
          Available Time Slots
        </h3>
        
        <div class="space-y-3">
          <div v-for="slot in mockTimeSlots" :key="slot.time"
               :class="[
                 'flex items-center justify-between p-4 rounded-xl border-2 cursor-pointer transition-all duration-200 transform hover:scale-[1.02]',
                 selectedTime === slot.time
                   ? 'border-blue-500 bg-blue-50'
                   : 'border-slate-200 hover:border-blue-300 hover:bg-slate-50'
               ]"
               @click="selectTime(slot.time)">
            <div>
              <div class="font-semibold text-slate-900">{{ slot.time }}</div>
              <div class="text-sm text-slate-600">{{ slot.capacity }} spots available</div>
            </div>
            <div class="text-right">
              <div class="font-bold text-blue-600">${{ slot.rate }}/hr</div>
              <div :class="[
                'text-xs px-2 py-1 rounded-full',
                slot.capacity > 3 ? 'bg-green-100 text-green-700' : 'bg-yellow-100 text-yellow-700'
              ]">
                {{ slot.capacity > 3 ? 'Available' : 'Limited' }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Duration and Continue -->
    <div class="mt-10 pt-8 border-t border-slate-200">
      <div class="flex items-center justify-between">
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-2">Duration (hours)</label>
          <select v-model="duration" class="rounded-xl border-slate-300 focus:border-blue-500 focus:ring-blue-500 px-3 py-2">
            <option value="1">1 hour</option>
            <option value="2">2 hours</option>
            <option value="4">4 hours</option>
            <option value="8">8 hours</option>
          </select>
        </div>
        
        <div class="text-right">
          <div class="text-sm text-slate-600 mb-1">Estimated Total</div>
          <div class="text-2xl font-bold text-blue-600">${{ estimatedTotal }}</div>
        </div>
      </div>
      
      <button 
        @click="continueToNext"
        :disabled="!selectedDate || !selectedTime"
        class="w-full mt-6 bg-gradient-to-r from-blue-600 to-blue-700 text-white font-semibold py-4 rounded-xl hover:from-blue-700 hover:to-blue-800 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 transform hover:scale-[1.02] active:scale-[0.98]"
      >
        Continue to Information
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

const selectedDate = ref<number>()
const selectedTime = ref<string>()
const duration = ref(2)

const mockDates = Array.from({ length: 31 }, (_, i) => ({
  day: i + 1,
  available: i > 14 && i < 30
}))

const mockTimeSlots = [
  { time: '9:00 AM', capacity: 5, rate: 15 },
  { time: '10:00 AM', capacity: 3, rate: 15 },
  { time: '11:00 AM', capacity: 4, rate: 15 },
  { time: '2:00 PM', capacity: 2, rate: 22.5 },
  { time: '3:00 PM', capacity: 1, rate: 22.5 },
]

const estimatedTotal = computed(() => {
  const slot = mockTimeSlots.find(s => s.time === selectedTime.value)
  return slot ? (slot.rate * duration.value).toFixed(2) : '0.00'
})

function selectDate(day: number) {
  selectedDate.value = day
}

function selectTime(time: string) {
  selectedTime.value = time
}

function continueToNext() {
  bookingFlow.nextStep()
  router.push('/book/information')
}
</script>