<template>
  <section class="auth-page">
    <div class="auth-card">
      <h1>Entrar</h1>

      <p class="subtitle">
        Informe seu e-mail e senha para acessar sua conta.
      </p>

      <form @submit.prevent="onSubmit">
        <div class="form-group">
          <label for="email">E-mail</label>
          <input
            id="email"
            v-model="form.email"
            type="email"
            autocomplete="email"
            required
          />
        </div>

        <div class="form-group">
          <label for="password">Senha</label>
          <input
            id="password"
            v-model="form.password"
            type="password"
            autocomplete="current-password"
            required
          />
        </div>

        <button
          type="submit"
          class="btn-primary"
        >
          Entrar
        </button>
      </form>
    </div>
  </section>
</template>

<script setup lang="ts">
import { reactive } from "vue";
import { useRouter } from "vue-router";

import { login } from "@/modules/auth/services/auth.service";

const router = useRouter();

const form = reactive({
  email: "",
  password: "",
});

async function onSubmit(): Promise<void> {
  try {
    const response = await login(form);

    localStorage.setItem(
      "access_token",
      response.access_token,
    );

    router.push("/dashboard");
  } catch (error) {
    console.error(error);
    alert("E-mail ou senha inválidos.");
  }
}
</script>

<style scoped>
.auth-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 80px);
  padding: 2rem;
}

.auth-card {
  width: 100%;
  max-width: 460px;
  padding: 2rem;
  border-radius: 12px;
  background: #fff;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

.subtitle {
  margin: 0.5rem 0 2rem;
  color: #666;
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 1rem;
}

.form-group label {
  margin-bottom: 0.4rem;
  font-weight: 600;
}

.form-group input {
  padding: 0.75rem;
  border: 1px solid #d0d7de;
  border-radius: 8px;
}

.btn-primary {
  width: 100%;
  padding: 0.9rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}
</style>