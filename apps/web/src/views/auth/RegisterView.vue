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
          <label for="passwordConfirmation">Confirmar senha</label>
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
          <span>Li e aceito os termos de uso.</span>
        </label>

        <button type="submit" class="btn-primary">
          Criar conta
        </button>
      </form>
    </div>
  </section>
</template>

<script setup lang="ts">
import { reactive } from "vue";
import { useRouter } from "vue-router";

import { register } from "@/modules/auth/services/auth.service";

const router = useRouter();

const form = reactive({
  name: "",
  email: "",
  password: "",
  passwordConfirmation: "",
  acceptTerms: false,
});

async function onSubmit(): Promise<void> {
  try {
    await register(form);

    alert("Conta criada com sucesso!");

    router.push("/login");
  } catch (error: any) {
    console.error(error);
    console.error(error.response);

    alert(
      JSON.stringify(
        error.response?.data ?? error.message,
        null,
        2,
      ),
    );
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
}
</style>