<template>
  <v-container class="mt-5">
    <v-card class="mb-4" color="blue-lighten-4" variant="tonal">
      <v-card-title>Statistiques OTP</v-card-title>
      <v-card-text>
        <p><strong>Total OTP :</strong> {{ otps.length }}</p>
        <p v-if="lastOtp"><strong>Dernier créé :</strong> {{ formatDate(lastOtp.createdAt) }}</p>
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-title>
        <h2 class="text-h5">Liste des OTP générés</h2>
      </v-card-title>

      <v-data-table
        :headers="headers"
        :items="otps"
        class="elevation-1"
        :items-per-page="5"
      >
        <template #item.createdAt="{ item }">
          {{ formatDate(item.createdAt) }}
        </template>

        <template #item.actions="{ item }">
          <v-btn icon color="error" @click="deleteOtp(item.id)">
            <v-icon>mdi-delete</v-icon>
          </v-btn>
        </template>

        <template #no-data>
          <v-alert type="info" border="start" color="blue lighten-3">
            Aucun OTP généré pour le moment.
          </v-alert>
        </template>
      </v-data-table>

      <v-card-actions>
        <v-spacer />
        <v-btn to="/" color="primary">Retour à l'accueil</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { useOtpStore } from '../stores/otpStore'
import { computed } from 'vue'

const { getAllOtps, removeOtp } = useOtpStore()
const otps = computed(() => getAllOtps())

const lastOtp = computed(() =>
  otps.value.length > 0
    ? otps.value[otps.value.length - 1]
    : null
)

const headers = [
  { text: 'Identifiant', value: 'id' },
  { text: 'Mot de passe', value: 'value' },
  { text: 'Créé le', value: 'createdAt' },
  { text: 'Actions', value: 'actions', sortable: false },
]

function formatDate(date: Date): string {
  return new Date(date).toLocaleString('fr-FR')
}

function deleteOtp(id: string) {
  removeOtp(id)
}
</script>
