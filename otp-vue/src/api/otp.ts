import axios from 'axios'

export interface Otp {
  id: string
  password: string
  created_at: string
  expires_at: string
  used: boolean
}

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
})

export const getOtps = () => api.get<Otp[]>('/otp/')
export const createOtp = (otpData: Partial<Otp>) => api.post<Otp>('/otp/', otpData)
export const getOtp = (id: string) => api.get<Otp>(`/otp/${id}/`)
export const markOtpAsUsed = (id: string) => api.patch<Otp>(`/otp/${id}/`, { used: true })
