<script setup lang="ts">
import { ref } from "vue";

import {
  BaseButton,
  BaseCard,
  BaseInput,
} from "@/shared/components/base";

const email = ref("");
const password = ref("");

function login() {
  console.log({
    email: email.value,
    password: password.value,
  });
}
</script>

<template>
  <BaseCard>

    <template #header>
      <div class="login__header">
        <h2>Entrar</h2>

        <p>
          Acesse sua conta para gerenciar suas finanças.
        </p>
      </div>
    </template>

    <form
      class="login__form"
      @submit.prevent="login"
    >

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

      <div class="login__actions">

        <RouterLink to="/forgot-password">
          Esqueceu sua senha?
        </RouterLink>

      </div>

      <BaseButton
        block
        type="submit"
      >
        Entrar
      </BaseButton>

    </form>

    <template #footer>

      <div class="login__footer">

        Não possui uma conta?

        <RouterLink to="/register">
          Criar conta
        </RouterLink>

      </div>

    </template>

  </BaseCard>
</template>

<style scoped>

.login__header{

text-align:center;

}

.login__header h2{

margin-bottom:.5rem;

}

.login__header p{

color:var(--color-text-secondary);

}

.login__form{

display:flex;

flex-direction:column;

gap:1.5rem;

margin-top:1.5rem;

}

.login__actions{

display:flex;

justify-content:flex-end;

font-size:.9rem;

}

.login__actions a{

text-decoration:none;

color:var(--color-primary);

}

.login__footer{

text-align:center;

padding-top:1rem;

}

.login__footer a{

margin-left:.25rem;

text-decoration:none;

font-weight:600;

color:var(--color-primary);

}

</style>