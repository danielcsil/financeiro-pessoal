<template>
  <div class="login-view">
    <header class="login-header">
      <h1>Entrar</h1>

      <p>
        Bem-vindo novamente.
        <br />
        Faça login para acessar sua conta.
      </p>
    </header>

    <form
      class="login-form"
      @submit.prevent="onSubmit"
    >
      <div class="form-group">
        <label for="email">
          E-mail
        </label>

        <input
          id="email"
          v-model="form.email"
          type="email"
          placeholder="seu@email.com"
          autocomplete="email"
          required
        />
      </div>

      <div class="form-group">
        <div class="password-header">
          <label for="password">
            Senha
          </label>

          <RouterLink
            to="/forgot-password"
            class="forgot-password"
          >
            Esqueceu sua senha?
          </RouterLink>
        </div>

        <input
          id="password"
          v-model="form.password"
          type="password"
          placeholder="Digite sua senha"
          autocomplete="current-password"
          required
        />
      </div>

      <div
        v-if="errorMessage"
        class="error-message"
      >
        {{ errorMessage }}
      </div>

      <button
        class="btn-primary"
        type="submit"
        :disabled="loading"
      >
        {{ loading ? "Entrando..." : "Entrar" }}
      </button>
    </form>

    <div class="separator">
      <span>ou</span>
    </div>

    <footer class="login-footer">
      <span>
        Ainda não possui uma conta?
      </span>

      <RouterLink to="/register">
        Criar Conta
      </RouterLink>
    </footer>
  </div>
</template>

<script setup lang="ts">
import axios from "axios";
import { reactive, ref } from "vue";
import { RouterLink, useRouter } from "vue-router";

import { useAuthStore } from "@/modules/auth/stores/auth.store";

const router = useRouter();

const authStore = useAuthStore();

const loading = ref(false);

const errorMessage = ref("");

const form = reactive({
  email: "",
  password: "",
});

async function onSubmit(): Promise<void> {
  errorMessage.value = "";

  loading.value = true;

  try {
    await authStore.login(
      form.email,
      form.password,
    );

    await router.push("/dashboard");
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      errorMessage.value =
        error.response?.data?.detail ??
        "Usuário ou senha inválidos.";
    } else {
      errorMessage.value =
        "Ocorreu um erro inesperado.";
    }

    console.error(error);
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped>
.login-view {
  display: flex;
  flex-direction: column;
}

.login-header {
  margin-bottom: 32px;
}

.login-header h1 {
  margin: 0;

  color: #14304d;

  font-size: 2rem;

  font-weight: 700;
}

.login-header p {
  margin-top: 10px;

  color: #64748b;

  line-height: 1.6;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 22px;
}

.password-header {
  display: flex;

  justify-content: space-between;

  align-items: center;

  margin-bottom: 8px;
}

label {
  display: block;

  font-weight: 600;

  color: #334155;
}

input {
  width: 100%;

  padding: 14px 16px;

  border: 1px solid #dbe3ed;

  border-radius: 12px;

  font-size: .95rem;

  transition:
    border-color .2s,
    box-shadow .2s;
}

input:focus {
  outline: none;

  border-color: #2563eb;

  box-shadow:
    0 0 0 4px rgba(37,99,235,.12);
}

.forgot-password {
  font-size: .9rem;

  color: #2563eb;

  text-decoration: none;

  font-weight: 600;
}

.forgot-password:hover {
  text-decoration: underline;
}

.error-message {
  margin-bottom: 20px;

  padding: 12px;

  border-radius: 10px;

  background: #fef2f2;

  color: #b91c1c;

  border: 1px solid #fecaca;

  font-size: .92rem;
}

.btn-primary {
  width: 100%;

  padding: 15px;

  border: none;

  border-radius: 12px;

  background: linear-gradient(
    135deg,
    #2563eb,
    #1d4ed8
  );

  color: white;

  font-size: 1rem;

  font-weight: 600;

  cursor: pointer;

  transition:
    transform .2s,
    box-shadow .2s;
}

.btn-primary:hover:not(:disabled) {
  transform: translateY(-2px);

  box-shadow:
    0 12px 28px rgba(37,99,235,.22);
}

.btn-primary:disabled {
  opacity: .7;

  cursor: not-allowed;
}

.separator {
  display: flex;

  align-items: center;

  margin: 34px 0 28px;
}

.separator::before,
.separator::after {
  content: "";

  flex: 1;

  height: 1px;

  background: #e5e7eb;
}

.separator span {
  margin: 0 18px;

  color: #94a3b8;

  font-size: .9rem;
}

.login-footer {
  display: flex;

  justify-content: center;

  gap: 6px;

  font-size: .95rem;

  color: #64748b;
}

.login-footer a {
  color: #2563eb;

  text-decoration: none;

  font-weight: 600;
}

.login-footer a:hover {
  text-decoration: underline;
}
</style>