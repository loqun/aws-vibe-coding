import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type { Franchise, CustomerInfo, ChildInfo } from '@/types/api'

export const useBookingFlowStore = defineStore('bookingFlow', () => {
  const currentStep = ref(0)
  const selectedFranchise = ref<Franchise>()
  const selectedDateTime = ref<{ start: string; end: string }>()
  const customerInfo = ref<CustomerInfo>()
  const childInfo = ref<ChildInfo>()
  const bookingId = ref<string>()
  const paymentStatus = ref<string>()

  const totalSteps = 5
  const isComplete = computed(() => currentStep.value >= totalSteps)

  function nextStep() {
    if (currentStep.value < totalSteps) {
      currentStep.value++
    }
  }

  function prevStep() {
    if (currentStep.value > 0) {
      currentStep.value--
    }
  }

  function setFranchise(franchise: Franchise) {
    selectedFranchise.value = franchise
  }

  function setDateTime(dateTime: { start: string; end: string }) {
    selectedDateTime.value = dateTime
  }

  function setCustomerInfo(info: CustomerInfo) {
    customerInfo.value = info
  }

  function setChildInfo(info: ChildInfo) {
    childInfo.value = info
  }

  function setBookingId(id: string) {
    bookingId.value = id
  }

  function reset() {
    currentStep.value = 0
    selectedFranchise.value = undefined
    selectedDateTime.value = undefined
    customerInfo.value = undefined
    childInfo.value = undefined
    bookingId.value = undefined
    paymentStatus.value = undefined
  }

  return {
    currentStep,
    selectedFranchise,
    selectedDateTime,
    customerInfo,
    childInfo,
    bookingId,
    paymentStatus,
    totalSteps,
    isComplete,
    nextStep,
    prevStep,
    setFranchise,
    setDateTime,
    setCustomerInfo,
    setChildInfo,
    setBookingId,
    reset
  }
})