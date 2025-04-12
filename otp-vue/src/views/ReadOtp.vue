<template>
  <v-container class="mt-5">
    <v-card class="pa-5" v-if="otpValue">
      <v-card-title>Lecture de l'OTP</v-card-title>
      <v-card-text>
        <p><strong>Mot de passe :</strong> {{ otpValue }}</p>
        <v-alert type="info" class="mt-3">
          Ce mot de passe a été supprimé de manière sécurisée après lecture.
        </v-alert>
      </v-card-text>
    </v-card>

    <v-card class="pa-5" v-else>
      <v-card-title>OTP invalide ou déjà lu</v-card-title>
      <v-card-text>
        <v-alert type="error">
          Ce lien n’est plus valable.
        </v-alert>
        <v-btn to="/" color="primary" class="mt-4">Retour à l'accueil</v-btn>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'
import { onMounted, ref } from 'vue'
import { useOtpStore } from '../stores/otpStore'

const route = useRoute()
const { getAllOtps, removeOtp } = useOtpStore()

const otpId = route.params.id as string
const otpValue = ref<string | null>(null)

onMounted(() => {
  const otp = getAllOtps().find(o => o.id === otpId)
  if (otp) {
    otpValue.value = otp.value
    removeOtp(otpId) // ⛔ suppression immédiate
  }
})
</script>
