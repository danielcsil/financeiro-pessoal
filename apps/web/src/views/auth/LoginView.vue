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
import { reactive, ref } from "vue";
import { useRoute, useRouter } from "vue-router";

import { useAuthStore } from "@/modules/auth/stores/auth.store";

/**
 * Router utilizado para navegação após autenticação.
 */
const router = useRouter();

/**
 * Permite recuperar a rota originalmente solicitada
 * antes do redirecionamento para a tela de login.
 */
const route = useRoute();

/**
 * Store responsável por toda a autenticação da aplicação.
 *
 * A View nunca acessa diretamente:
 * - API
 * - localStorage
 * - JWT
 */
const auth = useAuthStore();

/**
 * Dados informados pelo usuário.
 */
const form = reactive({
  email: "",
  password: "",
});

/**
 * Controla o estado de submissão do formulário.
 *
 * Evita múltiplos cliques enquanto a autenticação
 * está em andamento.
 */
const loading = ref(false);

/**
 * Realiza o processo de autenticação.
 *
 * Fluxo:
 *
 * 1. Delega o login para a AuthStore.
 * 2. A AuthStore autentica na API.
 * 3. Persiste o JWT.
 * 4. Carrega o usuário autenticado.
 * 5. Redireciona para a rota originalmente solicitada
 *    ou para o Dashboard.
 */
async function onSubmit(): Promise<void> {
  loading.value = true;

  try {
    await auth.login(form.email, form.password);

    const redirect =
      typeof route.query.redirect === "string"
        ? route.query.redirect
        : "/dashboard";

    await router.push(redirect);
  } catch (error) {
    console.error(error);
    alert("E-mail ou senha inválidos.");
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

.btn-primary:disabled {
  cursor: not-allowed;
  opacity: 0.7;
}
</style>