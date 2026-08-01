<script setup lang="ts">
import { computed } from "vue";

import type { FinancialAccount } from "../types/financial-account";

interface Props {
  account: FinancialAccount;
}

const props = defineProps<Props>();

const emit = defineEmits<{
  edit: [];
  details: [];
}>();

const formattedBalance = computed(() =>
  new Intl.NumberFormat("pt-BR", {
    style: "currency",
    currency: "BRL",
  }).format(props.account.currentBalance),
);

const accountType = computed(() =>
  String(props.account.accountType).replace(/_/g, " "),
);
</script>

<template>
  <article class="account-card">

    <div
      class="account-accent"
      :style="{ backgroundColor: account.color }"
    />

    <div class="card-content">

      <header class="card-header">

        <div class="account-icon">
          <i :class="account.icon" />
        </div>

        <div class="account-title">

          <h3>
            {{ account.name }}
          </h3>

          <span v-if="account.institution">
            {{ account.institution }}
          </span>

        </div>

      </header>

      <section class="account-information">

        <div class="information">

          <span class="label">
            Tipo
          </span>

          <strong>
            {{ accountType }}
          </strong>

        </div>

        <div class="information">

          <span class="label">
            Saldo Atual
          </span>

          <strong class="balance">
            {{ formattedBalance }}
          </strong>

        </div>

      </section>

      <footer class="card-footer">

        <span
          v-if="account.includeInCashFlow"
          class="badge"
        >
          Fluxo de Caixa
        </span>

        <span
          v-if="account.includeInNetWorth"
          class="badge"
        >
          Patrimônio
        </span>

      </footer>

      <div class="actions">

        <button
          class="secondary-button"
          @click="emit('details')"
        >
          Detalhes
        </button>

        <button
          class="primary-button"
          @click="emit('edit')"
        >
          Editar
        </button>

      </div>

    </div>

  </article>
</template>

<style scoped>

.account-card {

    display: flex;

    background: var(--color-surface);

    border: 1px solid var(--color-border);

    border-radius: 16px;

    overflow: hidden;

    transition: all .2s ease;
}

.account-card:hover {

    transform: translateY(-3px);

    box-shadow: 0 10px 25px rgba(0,0,0,.08);
}

.account-accent {

    width: 8px;

    flex-shrink: 0;
}

.card-content {

    flex: 1;

    padding: 1.5rem;

    display: flex;

    flex-direction: column;

    gap: 1.25rem;
}

.card-header {

    display: flex;

    gap: 1rem;

    align-items: center;
}

.account-icon {

    width: 48px;

    height: 48px;

    border-radius: 12px;

    display: flex;

    align-items: center;

    justify-content: center;

    background: var(--color-background-secondary);

    font-size: 1.25rem;
}

.account-title {

    display: flex;

    flex-direction: column;
}

.account-title h3 {

    margin: 0;

    font-size: 1.1rem;
}

.account-title span {

    color: var(--color-text-secondary);

    font-size: .9rem;
}

.account-information {

    display: grid;

    grid-template-columns: repeat(2,1fr);

    gap: 1rem;
}

.information {

    display: flex;

    flex-direction: column;

    gap: .25rem;
}

.label {

    font-size: .8rem;

    color: var(--color-text-secondary);
}

.balance {

    font-size: 1.2rem;

    color: var(--color-primary);
}

.card-footer {

    display: flex;

    gap: .5rem;

    flex-wrap: wrap;
}

.badge {

    padding: .3rem .7rem;

    border-radius: 999px;

    background: #e8f1ff;

    color: #2563eb;

    font-size: .75rem;

    font-weight: 600;
}

.actions {

    display: flex;

    justify-content: flex-end;

    gap: .75rem;

    margin-top: auto;
}

.primary-button,
.secondary-button {

    padding: .7rem 1rem;

    border-radius: 8px;

    cursor: pointer;

    font-weight: 600;
}

.primary-button {

    border: none;

    background: var(--color-primary);

    color: white;
}

.secondary-button {

    background: transparent;

    border: 1px solid var(--color-border);
}

</style>