<script setup lang="ts">
import { computed } from "vue";

import { BaseCard } from "@/shared/components/base";

const currentDate = computed(() =>
  new Intl.DateTimeFormat("pt-BR", {
    dateStyle: "full",
  }).format(new Date())
);

const summary = [
  {
    title: "Saldo Atual",
    value: "R$ 0,00",
    description: "Saldo consolidado das contas.",
  },
  {
    title: "Receitas do Mês",
    value: "R$ 0,00",
    description: "Entradas registradas no mês.",
  },
  {
    title: "Despesas do Mês",
    value: "R$ 0,00",
    description: "Saídas registradas no mês.",
  },
  {
    title: "Fluxo de Caixa",
    value: "R$ 0,00",
    description: "Resultado acumulado do período.",
  },
];

const modules = [
  "Contas",
  "Receitas",
  "Despesas",
  "Cartões",
  "Fluxo de Caixa",
  "Metas",
  "Relatórios",
  "Assistente IA",
];
</script>

<template>
  <div class="dashboard">

    <header class="dashboard__header">
      <div>
        <h1>Dashboard</h1>

        <p>{{ currentDate }}</p>
      </div>
    </header>

    <section class="dashboard__summary">

      <BaseCard
        v-for="item in summary"
        :key="item.title"
      >
        <template #header>
          <h3>{{ item.title }}</h3>
        </template>

        <div class="summary__value">
          {{ item.value }}
        </div>

        <p>
          {{ item.description }}
        </p>

      </BaseCard>

    </section>

    <section class="dashboard__modules">

      <BaseCard
        v-for="module in modules"
        :key="module"
      >
        <template #header>
          <h3>{{ module }}</h3>
        </template>

        <p>
          Módulo em desenvolvimento.
        </p>

      </BaseCard>

    </section>

  </div>
</template>

<style scoped>

.dashboard {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.dashboard__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.dashboard__header h1 {
  margin-bottom: .5rem;
}

.dashboard__header p {
  color: var(--color-text-secondary);
}

.dashboard__summary {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.5rem;
}

.summary__value {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: .75rem;
  color: var(--color-primary);
}

.dashboard__modules {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.5rem;
}

.dashboard__modules p {
  color: var(--color-text-secondary);
}

@media (max-width: 768px) {

  .dashboard__header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

}
</style>