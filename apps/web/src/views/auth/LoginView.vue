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
          :disabled="loading"
        >
          {{ loading ? "Entrando..." : "Entrar" }}
        </button>
      </form>
    </div>
  </section>
</template>

<script setup lang="ts">
import axios from "axios";
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";

import { useAuthStore } from "@/modules/auth/stores/auth.store";

const router = useRouter();

const authStore = useAuthStore();

const loading = ref(false);

const form = reactive({
  email: "",
  password: "",
});

async function onSubmit(): Promise<void> {
  loading.value = true;

  try {
    await authStore.login(
      form.email,
      form.password,
    );

    await router.push("/dashboard");
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      alert(
        error.response?.data?.detail ??
          "Usuário ou senha inválidos.",
      );
    } else {
      alert("Ocorreu um erro inesperado.");
    }

    console.error(error);
  } finally {
    loading.value = false;
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
  background: #ffffff;
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
  font-size: 1rem;
}

.btn-primary {
  width: 100%;
  padding: 0.9rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1rem;
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>