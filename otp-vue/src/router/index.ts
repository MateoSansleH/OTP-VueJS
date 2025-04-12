import { createRouter, createWebHistory } from 'vue-router'
import CreateOtp from '../views/CreateOtp.vue'
import ReadOtp from '../views/ReadOtp.vue'
import Admin from '../views/Admin.vue'

const routes = [
  { path: '/', name: 'CreateOtp', component: CreateOtp },
  { path: '/read/:id', name: 'ReadOtp', component: ReadOtp },
  { path: '/admin', name: 'Admin', component: Admin },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
