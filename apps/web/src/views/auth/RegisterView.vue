<script setup lang="ts">
import { ref } from "vue";

import {
  BaseButton,
  BaseCard,
  BaseInput,
} from "@/shared/components/base";

const name = ref("");
const email = ref("");
const password = ref("");
const confirmPassword = ref("");

function register() {
  console.log({
    name: name.value,
    email: email.value,
    password: password.value,
    confirmPassword: confirmPassword.value,
  });
}
</script>

<template>
  <BaseCard>

    <template #header>
      <div class="register__header">
        <h2>Criar Conta</h2>

        <p>
          Comece agora a organizar sua vida financeira.
        </p>
      </div>
    </template>

    <form
      class="register__form"
      @submit.prevent="register"
    >

      <BaseInput
        v-model="name"
        label="Nome"
        placeholder="Seu nome completo"
        required
      />

      <BaseInput
        v-model="email"
        label="E-mail"
        type="email"
        placeholder="seu@email.com"
        required
      />

      <BaseInput
        v-model="password"
        label="Senha"
        type="password"
        placeholder="********"
        required
      />

      <BaseInput
        v-model="confirmPassword"
        label="Confirmar Senha"
        type="password"
        placeholder="********"
        required
      />

      <BaseButton
        type="submit"
        block
      >
        Criar Conta
      </BaseButton>

    </form>

    <template #footer>

      <div class="register__footer">

        Já possui uma conta?

        <RouterLink to="/login">
          Entrar
        </RouterLink>

      </div>

    </template>

  </BaseCard>
</template>

<style scoped>

.register__header {
  text-align: center;
}

.register__header h2 {
  margin-bottom: .5rem;
}

.register__header p {
  color: var(--color-text-secondary);
}

.register__form {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  margin-top: 1.5rem;
}

.register__footer {
  text-align: center;
  padding-top: 1rem;
}

.register__footer a {
  margin-left: .25rem;
  text-decoration: none;
  color: var(--color-primary);
  font-weight: 600;
}

</style>