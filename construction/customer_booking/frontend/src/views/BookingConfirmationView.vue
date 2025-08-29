<template>
  <div class="text-center">
    <!-- Success Animation -->
    <div class="mb-8">
      <div class="bg-gradient-to-r from-green-500 to-green-600 rounded-full w-20 h-20 flex items-center justify-center mx-auto mb-6 animate-pulse">
        <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path>
        </svg>
      </div>
      
      <h2 class="text-3xl font-bold text-slate-900 mb-4">Booking Confirmed!</h2>
      <p class="text-lg text-slate-600 max-w-2xl mx-auto mb-8">
        Your childcare booking has been successfully created. We've sent a confirmation email with all the details.
      </p>
    </div>
    
    <!-- Booking Details Card -->
    <div class="bg-white rounded-2xl p-8 border-2 border-green-200 shadow-soft max-w-2xl mx-auto mb-8">
      <div class="flex items-center justify-between mb-6">
        <h3 class="text-xl font-semibold text-slate-900">Booking Details</h3>
        <span class="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm font-medium">
          Confirmed
        </span>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-left">
        <div class="space-y-3">
          <div>
            <span class="text-slate-600 text-sm">Booking Reference</span>
            <div class="font-mono font-bold text-lg text-primary-600">BK-2024-001</div>
          </div>
          
          <div>
            <span class="text-slate-600 text-sm">Location</span>
            <div class="font-medium">Downtown Kids Care</div>
            <div class="text-sm text-slate-500">123 Main St, Seattle</div>
          </div>
          
          <div>
            <span class="text-slate-600 text-sm">Child</span>
            <div class="font-medium">Alice Doe (5 years old)</div>
          </div>
        </div>
        
        <div class="space-y-3">
          <div>
            <span class="text-slate-600 text-sm">Date & Time</span>
            <div class="font-medium">January 20, 2024</div>
            <div class="text-sm text-slate-500">9:00 AM - 11:00 AM (2 hours)</div>
          </div>
          
          <div>
            <span class="text-slate-600 text-sm">Total Paid</span>
            <div class="font-bold text-lg text-green-600">$32.50</div>
          </div>
          
          <div>
            <span class="text-slate-600 text-sm">Payment Method</span>
            <div class="font-medium">•••• •••• •••• 3456</div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- QR Code Section -->
    <div class="bg-slate-50 rounded-2xl p-8 border border-slate-200 max-w-md mx-auto mb-8">
      <h3 class="text-lg font-semibold text-slate-900 mb-4">Drop-off QR Code</h3>
      <p class="text-sm text-slate-600 mb-6">
        Show this QR code to staff during drop-off for quick check-in
      </p>
      
      <!-- Mock QR Code -->
      <div class="bg-white p-6 rounded-xl border-2 border-slate-200 inline-block">
        <div class="w-32 h-32 bg-slate-900 rounded-lg flex items-center justify-center">
          <div class="grid grid-cols-8 gap-1">
            <div v-for="i in 64" :key="i" :class="[
              'w-1 h-1 rounded-sm',
              Math.random() > 0.5 ? 'bg-white' : 'bg-slate-900'
            ]"></div>
          </div>
        </div>
      </div>
      
      <p class="text-xs text-slate-500 mt-4">
        QR code is also available in your confirmation email
      </p>
    </div>
    
    <!-- Action Buttons -->
    <div class="flex flex-col sm:flex-row gap-4 justify-center items-center max-w-md mx-auto">
      <button class="w-full sm:w-auto bg-gradient-to-r from-primary-600 to-primary-700 text-white font-semibold px-8 py-3 rounded-xl hover:from-primary-700 hover:to-primary-800 transition-all duration-200">
        Add to Calendar
      </button>
      
      <button class="w-full sm:w-auto bg-white text-slate-700 font-semibold px-8 py-3 rounded-xl border-2 border-slate-200 hover:border-slate-300 hover:bg-slate-50 transition-all duration-200">
        Download Receipt
      </button>
    </div>
    
    <!-- Next Steps -->
    <div class="mt-12 bg-blue-50 rounded-2xl p-6 border border-blue-200 max-w-2xl mx-auto">
      <h3 class="text-lg font-semibold text-slate-900 mb-4">What's Next?</h3>
      <div class="text-left space-y-3">
        <div class="flex items-start">
          <div class="bg-blue-500 rounded-full w-6 h-6 flex items-center justify-center mr-3 mt-0.5">
            <span class="text-white text-xs font-bold">1</span>
          </div>
          <div>
            <div class="font-medium text-slate-900">Arrive 5 minutes early</div>
            <div class="text-sm text-slate-600">This helps with a smooth check-in process</div>
          </div>
        </div>
        
        <div class="flex items-start">
          <div class="bg-blue-500 rounded-full w-6 h-6 flex items-center justify-center mr-3 mt-0.5">
            <span class="text-white text-xs font-bold">2</span>
          </div>
          <div>
            <div class="font-medium text-slate-900">Show your QR code</div>
            <div class="text-sm text-slate-600">Staff will scan it for quick check-in</div>
          </div>
        </div>
        
        <div class="flex items-start">
          <div class="bg-blue-500 rounded-full w-6 h-6 flex items-center justify-center mr-3 mt-0.5">
            <span class="text-white text-xs font-bold">3</span>
          </div>
          <div>
            <div class="font-medium text-slate-900">Enjoy your time</div>
            <div class="text-sm text-slate-600">Your child is in safe, caring hands</div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Return Home -->
    <div class="mt-8">
      <router-link 
        to="/" 
        class="inline-flex items-center text-primary-600 hover:text-primary-700 font-medium"
      >
        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
        </svg>
        Return to Home
      </router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
// Booking confirmation with QR code and next steps
</script>