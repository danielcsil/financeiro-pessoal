<template>
  <section class="auth-page">
    <div class="auth-card">
      <h1>Criar conta</h1>

      <p class="subtitle">
        Preencha os dados abaixo para criar sua conta.
      </p>

      <form @submit.prevent="onSubmit">
        <div class="form-group">
          <label for="name">Nome</label>

          <input
            id="name"
            v-model="form.name"
            type="text"
            autocomplete="name"
            required
          />
        </div>

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
            autocomplete="new-password"
            required
          />
        </div>

        <div class="form-group">
          <label for="passwordConfirmation">
            Confirmar senha
          </label>

          <input
            id="passwordConfirmation"
            v-model="form.passwordConfirmation"
            type="password"
            autocomplete="new-password"
            required
          />
        </div>

        <label class="checkbox">
          <input
            v-model="form.acceptTerms"
            type="checkbox"
          />

          <span>
            Li e aceito os termos de uso.
          </span>
        </label>

        <button
          type="submit"
          class="btn-primary"
          :disabled="loading"
        >
          {{ loading ? "Criando conta..." : "Criar conta" }}
        </button>
      </form>
    </div>
  </section>
</template>

<script setup lang="ts">
import axios from "axios";
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";

import { authService } from "@/modules/auth/services/auth.service";

const router = useRouter();

const loading = ref(false);

const form = reactive({
  name: "",
  email: "",
  password: "",
  passwordConfirmation: "",
  acceptTerms: false,
});

async function onSubmit(): Promise<void> {
  if (form.password !== form.passwordConfirmation) {
    alert("As senhas não coincidem.");
    return;
  }

  if (!form.acceptTerms) {
    alert("É necessário aceitar os termos de uso.");
    return;
  }

  loading.value = true;

  try {
    await authService.register({
      name: form.name,
      email: form.email,
      password: form.password,
      passwordConfirmation: form.passwordConfirmation,
      acceptTerms: form.acceptTerms,
    });

    alert("Conta criada com sucesso!");

    form.name = "";
    form.email = "";
    form.password = "";
    form.passwordConfirmation = "";
    form.acceptTerms = false;

    await router.push("/login");
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      const message =
        error.response?.data?.detail ??
        "Não foi possível criar a conta.";

      alert(message);
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

.checkbox {
  display: flex;
  gap: 0.5rem;
  margin: 1rem 0 1.5rem;
  align-items: flex-start;
}

.btn-primary {
  width: 100%;
  padding: 0.9rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1rem;
  transition:
    opacity 0.2s ease,
    background-color 0.2s ease;
}

.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>