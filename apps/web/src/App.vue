<script setup lang="ts">
import { ref } from "vue";
import { RouterView } from "vue-router";

import {
  BaseButton,
  BaseCard,
  BaseInput,
} from "./shared/components/base";

const name = ref("");
</script>

<template>
  <div id="app">
    <div class="container py-4">
      <BaseCard>
        <template #header>
          <h2 class="heading-lg">
            Financial Advisor
          </h2>
        </template>

        <BaseInput
          v-model="name"
          label="Seu nome"
          placeholder="Digite seu nome"
        />

        <div class="mt-4">
          <BaseButton>
            Entrar
          </BaseButton>
        </div>

        <template #footer>
          {{ name || "Informe seu nome." }}
        </template>
      </BaseCard>

      <RouterView />
    </div>
  </div>
</template>

<style>
#app {
  min-height: 100vh;
}
</style>