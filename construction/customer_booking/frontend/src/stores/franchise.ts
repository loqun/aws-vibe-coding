import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Franchise, AvailabilityResponse } from '@/types/api'
import apiService from '@/services/api'

export const useFranchiseStore = defineStore('franchise', () => {
  const franchises = ref<Franchise[]>([])
  const availability = ref<AvailabilityResponse>()
  const loading = ref(false)
  const error = ref<string>()

  async function fetchFranchises() {
    loading.value = true
    error.value = undefined
    try {
      franchises.value = await apiService.getFranchises()
    } catch (err: any) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }

  async function fetchAvailability(franchiseId: string, date: string) {
    loading.value = true
    error.value = undefined
    try {
      availability.value = await apiService.checkAvailability(franchiseId, date)
    } catch (err: any) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }

  return {
    franchises,
    availability,
    loading,
    error,
    fetchFranchises,
    fetchAvailability
  }
})