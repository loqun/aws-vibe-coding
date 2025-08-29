<template>
  <div class="relative">
    <!-- Hero Section -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
      <div class="text-center">
        <div class="mb-8">
          <span class="inline-flex items-center px-4 py-2 rounded-full text-sm font-medium bg-blue-100 text-blue-800 mb-6">
            ✨ Trusted Childcare Services
          </span>
        </div>
        
        <h1 class="text-5xl md:text-6xl font-bold text-slate-900 mb-6 leading-tight">
          Safe & Reliable
          <span class="bg-gradient-to-r from-blue-600 to-purple-500 bg-clip-text text-transparent">
            Childcare
          </span>
        </h1>
        
        <p class="text-xl text-slate-600 mb-12 max-w-3xl mx-auto leading-relaxed">
          Book trusted childcare services at our franchise locations. Professional care, 
          flexible hours, and complete peace of mind for busy parents.
        </p>
        
        <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
          <router-link 
            to="/book/franchise" 
            class="group inline-flex items-center px-8 py-4 bg-gradient-to-r from-blue-600 to-blue-700 text-white font-semibold rounded-2xl hover:from-blue-700 hover:to-blue-800 transform hover:scale-105 transition-all duration-200 shadow-lg hover:shadow-xl"
          >
            <span>Book Now</span>
            <svg class="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
            </svg>
          </router-link>
          
          <router-link 
            to="/lookup" 
            class="inline-flex items-center px-8 py-4 bg-white text-slate-700 font-semibold rounded-2xl border-2 border-slate-200 hover:border-blue-300 hover:bg-slate-50 transition-all duration-200 shadow-md"
          >
            Find My Booking
          </router-link>
        </div>
      </div>
    </div>
    
    <!-- Features Section -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-20">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="group bg-white rounded-3xl p-8 shadow-md hover:shadow-xl transition-all duration-300 border border-slate-100">
          <div class="bg-gradient-to-r from-blue-500 to-blue-600 rounded-2xl w-16 h-16 flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-slate-900 mb-4 text-center">Flexible Hours</h3>
          <p class="text-slate-600 text-center leading-relaxed">Drop off your child during our operating hours with convenient hourly booking options that fit your schedule.</p>
        </div>
        
        <div class="group bg-white rounded-3xl p-8 shadow-md hover:shadow-xl transition-all duration-300 border border-slate-100">
          <div class="bg-gradient-to-r from-green-500 to-green-600 rounded-2xl w-16 h-16 flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-slate-900 mb-4 text-center">Safe & Secure</h3>
          <p class="text-slate-600 text-center leading-relaxed">Licensed caregivers and secure check-in/check-out process with QR codes for complete safety and transparency.</p>
        </div>
        
        <div class="group bg-white rounded-3xl p-8 shadow-md hover:shadow-xl transition-all duration-300 border border-slate-100">
          <div class="bg-gradient-to-r from-purple-500 to-purple-600 rounded-2xl w-16 h-16 flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-slate-900 mb-4 text-center">Easy Payment</h3>
          <p class="text-slate-600 text-center leading-relaxed">Secure online payment with transparent pricing, instant confirmation, and hassle-free booking management.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// Modern home page with improved design
</script>