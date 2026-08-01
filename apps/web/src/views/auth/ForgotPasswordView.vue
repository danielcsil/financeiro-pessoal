<template>
  <div class="forgot-password-view">
    <header class="forgot-header">
      <h1>Recuperar senha</h1>

      <p>
        Esqueceu sua senha?
        <br />
        Informe seu e-mail e enviaremos as instruções para redefini-la.
      </p>
    </header>

    <form
      class="forgot-form"
      @submit.prevent="recoverPassword"
    >
      <div class="form-group">
        <label for="email">
          E-mail
        </label>

        <input
          id="email"
          v-model="email"
          type="email"
          placeholder="seu@email.com"
          autocomplete="email"
          required
        />
      </div>

      <div
        v-if="successMessage"
        class="success-message"
      >
        {{ successMessage }}
      </div>

      <button
        class="btn-primary"
        type="submit"
        :disabled="loading"
      >
        {{ loading ? "Enviando..." : "Enviar instruções" }}
      </button>
    </form>

    <div class="separator">
      <span>ou</span>
    </div>

    <footer class="forgot-footer">
      <span>
        Lembrou sua senha?
      </span>

      <RouterLink to="/login">
        Voltar para o login
      </RouterLink>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { RouterLink } from "vue-router";

const email = ref("");

const loading = ref(false);

const successMessage = ref("");

async function recoverPassword(): Promise<void> {
  loading.value = true;

  successMessage.value = "";

  try {
    /**
     * TODO
     *
     * Sprint futura:
     * authService.forgotPassword(email.value)
     */

    await new Promise((resolve) =>
      setTimeout(resolve, 800),
    );

    successMessage.value =
      "Caso exista uma conta vinculada a este e-mail, enviaremos as instruções para recuperação da senha.";

  } finally {

    loading.value = false;

  }
}
</script>

<style scoped>

.forgot-password-view{
    display:flex;
    flex-direction:column;
}

.forgot-header{
    margin-bottom:32px;
}

.forgot-header h1{
    margin:0;
    color:#14304d;
    font-size:2rem;
    font-weight:700;
}

.forgot-header p{
    margin-top:10px;
    color:#64748b;
    line-height:1.6;
}

.forgot-form{
    display:flex;
    flex-direction:column;
}

.form-group{
    margin-bottom:22px;
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

.success-message{

    margin-bottom:20px;

    padding:12px 14px;

    border-radius:10px;

    background:#ECFDF5;

    border:1px solid #A7F3D0;

    color:#065F46;

    line-height:1.5;

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

    box-shadow:0 12px 28px rgba(37,99,235,.22);

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

.forgot-footer{

    display:flex;

    justify-content:center;

    gap:6px;

    font-size:.95rem;

    color:#64748b;

}

.forgot-footer a{

    color:#2563eb;

    text-decoration:none;

    font-weight:600;

}

.forgot-footer a:hover{

    text-decoration:underline;

}

</style>