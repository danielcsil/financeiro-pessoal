<script setup lang="ts">
import { computed, ref } from 'vue'
import { analyzePlan, type PlanAnalysisResponse } from '@/api/financial-planner'

const today = new Date().toISOString().slice(0, 10)
const endOfMonth = `${today.slice(0, 8)}28`
const openingBalance = ref('1000.00')
const result = ref<PlanAnalysisResponse>()
const error = ref('')
const loading = ref(false)

const currency = new Intl.NumberFormat('pt-BR', {
  style: 'currency',
  currency: 'BRL',
})

const minimumBalance = computed(() =>
  result.value ? currency.format(Number(result.value.liquidity.minimum_balance)) : '—',
)

async function runAnalysis() {
  error.value = ''
  loading.value = true
  try {
    result.value = await analyzePlan({
      start_date: today,
      end_date: endOfMonth,
      opening_balance: openingBalance.value,
      transactions: [],
    })
  } catch {
    error.value = 'Inicie a API em http://localhost:8000 e tente novamente.'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <main class="layout">
    <header>
      <p class="eyebrow">FINANCEIRO PESSOAL</p>
      <h1>Planeje antes de decidir.</h1>
      <p class="subtitle">Uma base Vue para visualizar a saúde do seu fluxo de caixa.</p>
    </header>

    <section class="card form-card">
      <label>
        Saldo inicial
        <input v-model="openingBalance" inputmode="decimal" aria-label="Saldo inicial" />
      </label>
      <button :disabled="loading" @click="runAnalysis">
        {{ loading ? 'Analisando…' : 'Analisar planejamento' }}
      </button>
    </section>

    <p v-if="error" class="error">{{ error }}</p>

    <section v-if="result" class="dashboard" aria-live="polite">
      <article class="card metric">
        <span>Saúde financeira</span>
        <strong>{{ result.score.overall }}/100</strong>
      </article>
      <article class="card metric">
        <span>Menor saldo projetado</span>
        <strong>{{ minimumBalance }}</strong>
      </article>
      <article class="card metric">
        <span>Dias com saldo negativo</span>
        <strong>{{ result.liquidity.negative_days }}</strong>
      </article>
      <article class="card summary">
        <span>Diagnóstico</span>
        <p>{{ result.summary }}</p>
      </article>
    </section>

    <section v-else class="empty-state">
      Informe um saldo inicial e execute a primeira análise. Em seguida, esta tela receberá o formulário de lançamentos e os gráficos de projeção.
    </section>
  </main>
</template>
