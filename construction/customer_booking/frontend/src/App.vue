<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50/30 to-indigo-50">
    <header class="sticky top-0 z-50 bg-white/90 backdrop-blur-md shadow-soft border-b border-slate-200/60">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center py-4">
          <router-link to="/" class="flex items-center space-x-3 group">
            <div class="w-11 h-11 bg-gradient-to-br from-primary-500 to-primary-600 rounded-2xl flex items-center justify-center shadow-medium group-hover:shadow-large transform group-hover:scale-105">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
              </svg>
            </div>
            <h1 class="text-2xl font-bold bg-gradient-to-r from-slate-800 to-primary-600 bg-clip-text text-transparent">
              KidsCare
            </h1>
          </router-link>
          
          <nav class="flex items-center space-x-2">
            <router-link 
              to="/" 
              class="btn-ghost"
              active-class="text-primary-600 bg-primary-50"
            >
              Home
            </router-link>
            <router-link 
              to="/lookup" 
              class="btn-ghost"
              active-class="text-primary-600 bg-primary-50"
            >
              Find Booking
            </router-link>
            <router-link 
              to="/book/franchise" 
              class="btn-primary ml-4"
            >
              Book Now
            </router-link>
          </nav>
        </div>
      </div>
    </header>
    
    <main class="animate-in">
      <RouterView />
    </main>
  </div>
</template>

<style scoped>

</style>