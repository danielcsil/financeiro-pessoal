<script setup lang="ts">
import {
  BaseButton,
  BaseCard,
} from "@/shared/components/base";
</script>

<template>
  <section class="hero">

    <div class="hero__content">

      <span class="hero__badge">
        💰 Controle Financeiro Inteligente
      </span>

      <h1>
        Organize sua vida financeira com inteligência.
      </h1>

      <p>
        Controle receitas, despesas, cartões, investimentos,
        metas financeiras e conte com um assistente baseado em IA
        para tomar melhores decisões.
      </p>

      <div class="hero__actions">

        <BaseButton>
          Começar Agora
        </BaseButton>

        <BaseButton variant="secondary">
          Conhecer Funcionalidades
        </BaseButton>

      </div>

    </div>

  </section>

  <section class="features">

    <BaseCard>

      <template #header>
        <h3>Fluxo de Caixa</h3>
      </template>

      <p>
        Visualize entradas e saídas em tempo real.
      </p>

    </BaseCard>

    <BaseCard>

      <template #header>
        <h3>Cartões</h3>
      </template>

      <p>
        Controle limites, parcelas e vencimentos.
      </p>

    </BaseCard>

    <BaseCard>

      <template #header>
        <h3>Metas</h3>
      </template>

      <p>
        Planeje objetivos financeiros e acompanhe sua evolução.
      </p>

    </BaseCard>

    <BaseCard>

      <template #header>
        <h3>Assistente IA</h3>
      </template>

      <p>
        Receba recomendações personalizadas para melhorar seu fluxo de caixa.
      </p>

    </BaseCard>

  </section>
</template>

<style scoped>

.hero{

    padding:7rem 2rem;

    display:flex;

    justify-content:center;

}

.hero__content{

    max-width:900px;

    text-align:center;

}

.hero__badge{

    display:inline-block;

    padding:.5rem 1rem;

    border-radius:999px;

    background:var(--color-primary);

    color:white;

    margin-bottom:2rem;

}

.hero h1{

    font-size:3.25rem;

    margin-bottom:1.5rem;

    line-height:1.15;

}

.hero p{

    font-size:1.2rem;

    color:var(--color-text-secondary);

    margin-bottom:2.5rem;

}

.hero__actions{

    display:flex;

    justify-content:center;

    gap:1rem;

    flex-wrap:wrap;

}

.features{

    max-width:1200px;

    margin:0 auto;

    padding:2rem;

    display:grid;

    grid-template-columns:repeat(auto-fit,minmax(260px,1fr));

    gap:2rem;

}

.features h3{

    margin-bottom:1rem;

}

.features p{

    color:var(--color-text-secondary);

    line-height:1.6;

}

@media(max-width:768px){

.hero{

padding:4rem 1.5rem;

}

.hero h1{

font-size:2.2rem;

}

}

</style>