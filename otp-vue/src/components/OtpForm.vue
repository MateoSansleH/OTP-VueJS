<template>
  <v-container class="mt-5">
    <v-card class="pa-5">
      <v-card-title>Créer un OTP</v-card-title>

      <v-text-field
        v-model="password"
        label="Mot de passe"
        outlined
      ></v-text-field>

      <v-btn color="primary" @click="generateLink" class="mt-3">Générer le lien</v-btn>
      <v-btn to="/admin" color="secondary" class="mt-3">Accès Admin</v-btn>

      <transition name="fade">
        <v-alert v-if="generatedLink" type="info" class="mt-4">
          Voici votre lien :<br />
          <code>{{ generatedLink }}</code>
        </v-alert>
      </transition>

      <v-snackbar v-model="showError" color="error" timeout="3000">
        Veuillez entrer un mot de passe !
      </v-snackbar>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { createOtp, type Otp } from '@/api/otp'

const password = ref('')
const generatedLink = ref('')
const showError = ref(false)

async function generateLink() {
  if (!password.value) {
    showError.value = true
    return
  }

  const expiresAt = new Date(Date.now() + 5 * 60 * 1000).toISOString() // expire dans 5 min

  try {
    const response = await createOtp({
      password: password.value,
      expires_at: expiresAt,
    })

    const otp: Otp = response.data
    generatedLink.value = `${window.location.origin}/read/${otp.id}`
  } catch (err) {
    console.error("Erreur lors de l'enregistrement :", err)
    showError.value = true
  }
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 1.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
