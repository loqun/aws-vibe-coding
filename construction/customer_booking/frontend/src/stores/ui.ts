import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { APIError } from '@/types/api'

export const useUIStore = defineStore('ui', () => {
  const loading = ref(false)
  const errors = ref<APIError[]>([])
  const notifications = ref<{ id: string; message: string; type: 'success' | 'error' | 'info' }[]>([])

  function setLoading(state: boolean) {
    loading.value = state
  }

  function addError(error: APIError) {
    errors.value.push(error)
  }

  function clearErrors() {
    errors.value = []
  }

  function addNotification(message: string, type: 'success' | 'error' | 'info' = 'info') {
    const id = Date.now().toString()
    notifications.value.push({ id, message, type })
    
    setTimeout(() => {
      removeNotification(id)
    }, 5000)
  }

  function removeNotification(id: string) {
    const index = notifications.value.findIndex(n => n.id === id)
    if (index > -1) {
      notifications.value.splice(index, 1)
    }
  }

  return {
    loading,
    errors,
    notifications,
    setLoading,
    addError,
    clearErrors,
    addNotification,
    removeNotification
  }
})