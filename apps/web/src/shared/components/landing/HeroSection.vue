<template>
  <section class="hero">

    <div class="hero__container">

      <!-- Conteúdo -->
      <div class="hero__content">

        <span class="hero__badge">
          Plataforma completa para gestão financeira
        </span>

        <h1 class="hero__title">
          Personal Finance
        </h1>

        <h2 class="hero__subtitle">
          Minha vida financeira em um único lugar.
        </h2>

        <p class="hero__description">
          Organize receitas, despesas, cartões de crédito,
          financiamentos, patrimônio, investimentos e metas em uma
          única plataforma.

          Tenha uma visão completa da sua situação financeira e
          receba recomendações inteligentes para tomar decisões
          mais conscientes.
        </p>

        <div class="hero__buttons">

          <RouterLink
              to="/register"
              class="btn btn-primary hero__button"
          >
            Começar Agora
          </RouterLink>

          <a
              href="#about"
              class="btn btn-secondary hero__button"
          >
            Conhecer Recursos
          </a>

        </div>

        <div class="hero__metrics">

          <div class="metric-card">

            <span class="metric-card__value">
              100%
            </span>

            <span class="metric-card__label">
              Controle Financeiro
            </span>

          </div>

          <div class="metric-card">

            <span class="metric-card__value">
              IA
            </span>

            <span class="metric-card__label">
              Recomendações Inteligentes
            </span>

          </div>

          <div class="metric-card">

            <span class="metric-card__value">
              Tudo
            </span>

            <span class="metric-card__label">
              Em um único lugar
            </span>

          </div>

        </div>

      </div>

      <!-- Ilustração -->
      <div class="hero__image">

        <div class="hero__image-wrapper">

          <!--
              Substituir posteriormente por:

              hero-finance.svg

              ou

              dashboard-preview.png
          -->

          <img
            src="@/assets/images/hero-init.png"
            alt="Dashboard do Personal Finance"
            class="hero-image"
          />

        </div>

      </div>

    </div>

  </section>
</template>

<script setup lang="ts">
import { RouterLink } from "vue-router";
</script>

<style scoped>

.hero {

    width:100%;
    background:
            linear-gradient(
                    180deg,
                    #ffffff 0%,
                    #f8fafc 100%
            );

    padding-top:80px;
    padding-bottom:80px;

}

.hero__container{

    max-width:1440px;

    margin:auto;

    display:grid;

    grid-template-columns:
            1.1fr
            0.9fr;

    gap:32px;

    align-items:center;

    padding-left:40px;
    padding-right:40px;

}

.hero__badge{

    display:inline-block;

    padding:8px 18px;

    border-radius:999px;

    background:#dbeafe;

    color:#1d4ed8;

    font-weight:600;

    margin-bottom:24px;

}

.hero__title{

    font-size:64px;

    font-weight:800;

    line-height:1.1;

    color:var(--color-text-primary);

}

.hero__subtitle{

    margin-top:20px;

    font-size:34px;

    line-height:1.3;

    color:var(--color-primary);

    font-weight:700;

}

.hero__description{

    margin-top:30px;

    font-size:20px;

    line-height:1.9;

    color:var(--color-text-secondary);

    max-width:720px;

}

.hero__buttons{

    display:flex;

    gap:18px;

    margin-top:42px;

}

.hero__button{

    min-width:190px;

    text-align:center;

}

.hero__metrics{

    display:flex;

    gap:22px;

    margin-top:60px;

    flex-wrap:wrap;

}

.metric-card{

    width:180px;

    background:white;

    border-radius:16px;

    padding:22px;

    box-shadow:
            0 10px 30px rgba(0,0,0,.06);

}

.metric-card__value{

    display:block;

    font-size:30px;

    font-weight:700;

    color:var(--color-primary);

}

.metric-card__label{

    display:block;

    margin-top:10px;

    color:var(--color-text-secondary);

    line-height:1.5;

}

.hero__image{

    display:flex;

    justify-content:flex-end;

    align-items:center;

}

.hero__image-wrapper{

    width:100%;
    
    max-width:900px;

    padding:0;

    background:white;

    border-radius:28px;

    box-shadow:
        0 20px 45px rgba(15,23,42,.08);

}

.hero__image img{

    width:100%;
    height:auto;
    display:block;
    object-fit:contain;
}

@media(max-width:1024px){

.hero__container{

    display:grid;

    grid-template-columns:
        1fr
        1.2fr;

    gap:40px;
}

.hero__content{

    order:2;

}

.hero__image{

    order:1;

}

.hero__title{

    font-size:52px;

}

.hero__subtitle{

    font-size:28px;

}

}

@media(max-width:768px){

.hero{

    padding-top:50px;

    padding-bottom:50px;

}

.hero__container{

    padding-left:20px;
    padding-right:20px;

}

.hero__title{

    font-size:40px;

}

.hero__subtitle{

    font-size:24px;

}

.hero__description{

    font-size:18px;

}

.hero__buttons{

    flex-direction:column;

}

.hero__button{

    width:100%;

}

.hero__metrics{

    justify-content:center;

}

.metric-card{

    width:100%;

}

}

</style>