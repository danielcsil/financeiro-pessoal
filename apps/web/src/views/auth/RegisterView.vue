<template>
  <div class="register-view">
    <header class="register-header">
      <h1>Criar conta</h1>

      <p>
        Bem-vindo ao Personal Finance.
        <br />
        Crie sua conta e comece a organizar sua vida financeira.
      </p>
    </header>

    <form
      class="register-form"
      @submit.prevent="onSubmit"
    >
      <div class="form-group">
        <label for="name">
          Nome completo
        </label>

        <input
          id="name"
          v-model="form.name"
          type="text"
          placeholder="Digite seu nome"
          autocomplete="name"
          required
        />
      </div>

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
        <label for="password">
          Senha
        </label>

        <input
          id="password"
          v-model="form.password"
          type="password"
          placeholder="Crie uma senha"
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
          placeholder="Repita sua senha"
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
        {{ loading ? "Criando conta..." : "Criar conta" }}
      </button>
    </form>

    <div class="separator">
      <span>ou</span>
    </div>

    <footer class="register-footer">
      <span>
        Já possui uma conta?
      </span>

      <RouterLink to="/login">
        Entrar
      </RouterLink>
    </footer>
  </div>
</template>

<script setup lang="ts">
import axios from "axios";
import { reactive, ref } from "vue";
import { RouterLink, useRouter } from "vue-router";

import { authService } from "@/modules/auth/services/auth.service";

const router = useRouter();

const loading = ref(false);

const errorMessage = ref("");

const form = reactive({
  name: "",
  email: "",
  password: "",
  passwordConfirmation: "",
  acceptTerms: false,
});

async function onSubmit(): Promise<void> {

  errorMessage.value = "";

  if (form.password !== form.passwordConfirmation) {
    errorMessage.value =
      "As senhas não coincidem.";

    return;
  }

  if (!form.acceptTerms) {
    errorMessage.value =
      "É necessário aceitar os termos de uso.";

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

    await router.push({
      path: "/login",
      query: {
        registered: "true",
      },
    });

  } catch (error: unknown) {

    if (axios.isAxiosError(error)) {

      errorMessage.value =
        error.response?.data?.detail ??
        "Não foi possível criar a conta.";

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
.register-view{
    display:flex;
    flex-direction:column;
}

.register-header{
    margin-bottom:32px;
}

.register-header h1{
    margin:0;
    color:#14304d;
    font-size:2rem;
    font-weight:700;
}

.register-header p{
    margin-top:10px;
    color:#64748b;
    line-height:1.6;
}

.register-form{
    display:flex;
    flex-direction:column;
}

.form-group{
    margin-bottom:20px;
}

label{
    display:block;
    margin-bottom:8px;
    font-weight:600;
    color:#334155;
}

input{
    width:100%;
    padding:14px 16px;
    border:1px solid #dbe3ed;
    border-radius:12px;
    font-size:.95rem;
    transition:border-color .2s,box-shadow .2s;
}

input:focus{
    outline:none;
    border-color:#2563eb;
    box-shadow:0 0 0 4px rgba(37,99,235,.12);
}

.checkbox{
    display:flex;
    align-items:flex-start;
    gap:10px;
    margin-bottom:24px;
}

.checkbox input{
    width:18px;
    height:18px;
    margin-top:3px;
}

.checkbox span{
    color:#475569;
    line-height:1.5;
}

.error-message{
    margin-bottom:22px;
    padding:12px 14px;
    border-radius:10px;
    background:#FEF2F2;
    color:#B91C1C;
    border:1px solid #FECACA;
    font-size:.92rem;
}

.btn-primary{
    width:100%;
    padding:15px;
    border:none;
    border-radius:12px;
    background:linear-gradient(
        135deg,
        #2563eb,
        #1d4ed8
    );
    color:white;
    font-size:1rem;
    font-weight:600;
    cursor:pointer;
    transition:.2s;
}

.btn-primary:hover:not(:disabled){
    transform:translateY(-2px);
    box-shadow:0 14px 26px rgba(37,99,235,.20);
}

.btn-primary:disabled{
    opacity:.7;
    cursor:not-allowed;
}

.separator{
    display:flex;
    align-items:center;
    margin:34px 0 26px;
}

.separator::before,
.separator::after{
    content:"";
    flex:1;
    height:1px;
    background:#E5E7EB;
}

.separator span{
    margin:0 18px;
    color:#94A3B8;
    font-size:.9rem;
}

.register-footer{
    display:flex;
    justify-content:center;
    gap:6px;
    color:#64748b;
    font-size:.95rem;
}

.register-footer a{
    color:#2563eb;
    text-decoration:none;
    font-weight:600;
}

.register-footer a:hover{
    text-decoration:underline;
}
</style>