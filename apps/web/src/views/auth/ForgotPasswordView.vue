<script setup lang="ts">
import { ref } from "vue";

import {
  BaseButton,
  BaseCard,
  BaseInput,
} from "@/shared/components/base";

const email = ref("");

function recoverPassword() {
  console.log({
    email: email.value,
  });
}
</script>

<template>
  <BaseCard>
    <template #header>
      <div class="forgot-password__header">
        <h2>Recuperar Senha</h2>

        <p>
          Informe seu e-mail para receber as instruções de redefinição de senha.
        </p>
      </div>
    </template>

    <form
      class="forgot-password__form"
      @submit.prevent="recoverPassword"
    >
      <BaseInput
        v-model="email"
        label="E-mail"
        type="email"
        placeholder="seu@email.com"
        required
      />

      <BaseButton
        type="submit"
        block
      >
        Enviar instruções
      </BaseButton>
    </form>

    <template #footer>
      <div class="forgot-password__footer">
        Lembrou sua senha?

        <RouterLink to="/login">
          Voltar para o login
        </RouterLink>
      </div>
    </template>
  </BaseCard>
</template>

<style scoped>

.forgot-password__header {
  text-align: center;
}

.forgot-password__header h2 {
  margin-bottom: .5rem;
}

.forgot-password__header p {
  color: var(--color-text-secondary);
  line-height: 1.6;
}

.forgot-password__form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.forgot-password__footer {
  text-align: center;
  padding-top: 1rem;
}

.forgot-password__footer a {
  margin-left: .25rem;
  text-decoration: none;
  color: var(--color-primary);
  font-weight: 600;
}

</style>