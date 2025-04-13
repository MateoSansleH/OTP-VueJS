<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getOtps, type Otp } from '@/api/otp'

const otps = ref([])

const loadOtps = async () => {
  try {
    const response = await getOtps()
    otps.value = response.data
  } catch (err) {
    console.error('Erreur chargement OTPs', err)
  }
}

onMounted(loadOtps)
</script>

<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">Liste des OTP</h1>
    <router-link to="/create" class="bg-green-600 text-white px-4 py-2 rounded mb-4 inline-block">
      ➕ Créer un OTP
    </router-link>
    <ul class="space-y-2">
      <li
        v-for="otp in otps"
        :key="otp.id"
        class="p-2 border rounded hover:bg-gray-100 transition"
      >
        <router-link :to="`/read/${otp.id}`" class="font-mono">
          🔑 {{ otp.id}}
        </router-link>
        <span v-if="otp.used" class="text-red-600 ml-2">(utilisé)</span>
        <span v-if="otp.expired" class="text-gray-400 ml-2">(expiré)</span>
      </li>
    </ul>
  </div>
</template>
