<template>
  <section class="landing-section modules-section">
    <div class="landing-container">

      <div class="section-header">
        <span class="section-badge">
          Plataforma Completa
        </span>

        <h2>
          Todos os módulos necessários para organizar sua vida financeira
        </h2>

        <p>
          Desenvolvido para centralizar todas as informações financeiras da sua
          família em um único lugar, eliminando planilhas dispersas e controles
          manuais.
        </p>
      </div>

      <div class="modules-grid">

        <div
          v-for="module in modules"
          :key="module.title"
          class="module-card"
        >
          <component
            :is="module.icon"
            :size="32"
            class="module-icon"
          />

          <h3>{{ module.title }}</h3>

          <p>{{ module.description }}</p>
        </div>

      </div>

    </div>
  </section>
</template>

<script setup lang="ts">
import {
  Wallet,
  Receipt,
  CreditCard,
  Landmark,
  PiggyBank,
  Target,
  BarChart3,
  TrendingUp,
  Home,
  Settings,
  Bell,
  BrainCircuit
} from "lucide-vue-next";

const modules = [
  {
    icon: Wallet,
    title: "Fluxo de Caixa",
    description: "Controle diário do saldo e projeções futuras."
  },
  {
    icon: Receipt,
    title: "Receitas",
    description: "Gerencie salários, aluguéis e demais receitas."
  },
  {
    icon: CreditCard,
    title: "Cartões",
    description: "Controle limites, parcelamentos e faturas."
  },
  {
    icon: Landmark,
    title: "Contas Bancárias",
    description: "Acompanhe todas as suas contas em um só lugar."
  },
  {
    icon: PiggyBank,
    title: "Investimentos",
    description: "Monitore patrimônio, aportes e rentabilidade."
  },
  {
    icon: Target,
    title: "Metas",
    description: "Planeje objetivos financeiros e acompanhe a evolução."
  },
  {
    icon: BarChart3,
    title: "Relatórios",
    description: "Indicadores e gráficos para tomada de decisão."
  },
  {
    icon: TrendingUp,
    title: "Patrimônio",
    description: "Visualize sua evolução patrimonial ao longo do tempo."
  },
  {
    icon: Home,
    title: "Financiamentos",
    description: "Controle imóveis, veículos e amortizações."
  },
  {
    icon: BrainCircuit,
    title: "IA Financeira",
    description: "Receba recomendações inteligentes e previsões."
  },
  {
    icon: Bell,
    title: "Alertas",
    description: "Nunca mais esqueça um vencimento importante."
  },
  {
    icon: Settings,
    title: "Configurações",
    description: "Personalize contas, categorias e preferências."
  }
];
</script>

<style scoped>

.modules-section{
  background:var(--color-background-secondary);
}

.section-header{
  max-width:760px;
  margin:0 auto 4rem;
  text-align:center;
}

.modules-grid{

  display:grid;

  grid-template-columns:repeat(4,1fr);

  gap:1.75rem;

}

.module-card{

  padding:2rem;

  background:var(--color-surface);

  border:1px solid var(--color-border);

  border-radius:20px;

  transition:.25s;

}

.module-card:hover{

  transform:translateY(-6px);

  border-color:var(--color-primary);

  box-shadow:var(--shadow-lg);

}

.module-icon{

  color:var(--color-primary);

  margin-bottom:1.5rem;

}

.module-card h3{

  margin-bottom:.75rem;

  color:var(--color-text-primary);

  font-size:1.1rem;

}

.module-card p{

  color:var(--color-text-secondary);

  line-height:1.7;

}

@media(max-width:1200px){

.modules-grid{

grid-template-columns:repeat(3,1fr);

}

}

@media(max-width:900px){

.modules-grid{

grid-template-columns:repeat(2,1fr);

}

}

@media(max-width:600px){

.modules-grid{

grid-template-columns:1fr;

}

}

</style>