// src/stores/otpStore.ts
import { ref } from 'vue'

export interface OtpEntry {
  id: string
  value: string
  createdAt: Date
}

const otpList = ref<OtpEntry[]>([])

export function useOtpStore() {
  function addOtp(value: string) {
    const id = btoa(value)
    otpList.value.push({
      id,
      value,
      createdAt: new Date()
    })
    return id
  }

  function getAllOtps() {
    return otpList.value
  }

  function removeOtp(id: string) {
    otpList.value = otpList.value.filter(otp => otp.id !== id)
  }

  return {
    addOtp,
    getAllOtps,
    removeOtp
  }
}
