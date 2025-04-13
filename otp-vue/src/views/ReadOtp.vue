<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { getOtp, type Otp } from '@/api/otp'

const route = useRoute()
const otp = ref<Otp | null>(null)
const errorMessage = ref('')

onMounted(async () => {
  const id = route.params.id as string
  try {
    const response = await getOtp(id)
    otp.value = response.data
  } catch (err: any) {
    errorMessage.value = err.response?.data?.error || "Erreur lors de la récupération de l'OTP"
  }
})
</script>

<template>
  <v-container class="mt-5">
    <v-card class="pa-5">
      <v-card-title>Consultation du mot de passe</v-card-title>

      <v-alert v-if="errorMessage" type="error" class="mt-4">
        {{ errorMessage }}
      </v-alert>

      <v-alert v-else-if="otp" type="success" class="mt-4">
        🔑 Mot de passe : <code>{{ otp.password }}</code>
      </v-alert>

      <v-btn to="/" color="primary" class="mt-4">↩️ Retour</v-btn>
    </v-card>
  </v-container>
</template>
