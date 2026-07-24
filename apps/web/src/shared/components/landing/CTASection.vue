<template>
  <section class="landing-section cta-section">
    <div class="landing-container">

      <div class="cta-card">

        <span class="section-badge">
          Comece Agora
        </span>

        <h2>
          Organize sua vida financeira hoje mesmo
        </h2>

        <p>
          Pare de controlar suas finanças em várias planilhas e aplicativos.
          Centralize receitas, despesas, cartões, investimentos e metas em uma
          única plataforma inteligente.
        </p>

        <div class="cta-buttons">

          <RouterLink
            to="/register"
            class="btn btn-primary btn-lg"
          >
            Criar Conta Gratuitamente
          </RouterLink>

          <RouterLink
            to="/login"
            class="btn btn-outline btn-lg"
          >
            Já tenho uma conta
          </RouterLink>

        </div>

        <div class="cta-features">

          <div class="feature">
            ✓ Sem cartão de crédito
          </div>

          <div class="feature">
            ✓ Cadastro em menos de 2 minutos
          </div>

          <div class="feature">
            ✓ Seus dados protegidos
          </div>

        </div>

      </div>

    </div>
  </section>
</template>

<script setup lang="ts">
import { RouterLink } from "vue-router";
</script>

<style scoped>

.cta-section{

    background:linear-gradient(
        180deg,
        var(--color-background),
        var(--color-background-secondary)
    );

}

.cta-card{

    padding:5rem 4rem;

    text-align:center;

    border-radius:32px;

    background:linear-gradient(
        135deg,
        var(--color-primary),
        var(--color-primary-dark)
    );

    color:white;

    box-shadow:var(--shadow-xl);

}

.cta-card h2{

    margin:1.5rem 0;

    font-size:clamp(2rem,4vw,3.2rem);

    color:white;

}

.cta-card p{

    max-width:720px;

    margin:0 auto 3rem;

    opacity:.92;

    font-size:1.1rem;

    line-height:1.9;

}

.cta-buttons{

    display:flex;

    justify-content:center;

    gap:1rem;

    flex-wrap:wrap;

    margin-bottom:3rem;

}

.cta-buttons .btn-outline{

    background:white;

    color:var(--color-primary);

}

.cta-buttons .btn-outline:hover{

    background:#F5F7FA;

}

.cta-features{

    display:flex;

    justify-content:center;

    gap:2rem;

    flex-wrap:wrap;

    font-size:.95rem;

    opacity:.95;

}

.feature{

    display:flex;

    align-items:center;

    gap:.5rem;

}

@media(max-width:768px){

.cta-card{

padding:3rem 2rem;

}

.cta-features{

flex-direction:column;

gap:1rem;

}

}

</style>