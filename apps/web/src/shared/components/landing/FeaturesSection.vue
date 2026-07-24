<template>
    <section class="landing-section features-section">
        <div class="landing-container">

            <div class="section-header">
                <span class="section-badge">
                    Funcionalidades
                </span>

                <h2>
                    Tudo o que você precisa para controlar sua vida financeira
                </h2>

                <p>
                    O Personal Finance reúne em um único ambiente todas as
                    ferramentas necessárias para organizar receitas, despesas,
                    cartões, investimentos, patrimônio e planejamento financeiro.
                </p>
            </div>

            <div class="features-grid">

                <FeatureCard
                    :icon="Wallet"
                    title="Fluxo de Caixa"
                    description="Acompanhe receitas, despesas, saldo diário, projeções futuras e descubra antecipadamente quando haverá falta de dinheiro."
                />

                <FeatureCard
                    :icon="CreditCard"
                    title="Cartões de Crédito"
                    description="Gerencie limites, faturas, parcelamentos e visualize o impacto das compras futuras antes de realizá-las."
                />

                <FeatureCard
                    :icon="Target"
                    title="Metas Financeiras"
                    description="Defina objetivos, acompanhe sua evolução e saiba exatamente quanto falta para atingir cada conquista."
                />

                <FeatureCard
                    :icon="Sparkles"
                    title="Inteligência Artificial"
                    description="Receba recomendações inteligentes para reduzir gastos, reorganizar o orçamento e melhorar sua saúde financeira."
                />

                <FeatureCard
                    :icon="PieChart"
                    title="Patrimônio"
                    description="Visualize a evolução do seu patrimônio, financiamentos, investimentos e patrimônio líquido em gráficos intuitivos."
                />

                <FeatureCard
                    :icon="TrendingUp"
                    title="Investimentos"
                    description="Controle aplicações, rentabilidade, aportes e acompanhe a evolução dos seus investimentos."
                />

            </div>

        </div>
    </section>
</template>

<script setup lang="ts">
import FeatureCard from "./FeatureCard.vue";

import {
    Wallet,
    CreditCard,
    Target,
    Sparkles,
    PieChart,
    TrendingUp
} from "lucide-vue-next";
</script>

<style scoped>

.features-section{
    background:var(--color-background-secondary);
}

.section-header{
    max-width:760px;
    margin:0 auto 4rem;
    text-align:center;
}

.features-grid{

    display:grid;
    grid-template-columns:repeat(3,1fr);

    gap:2rem;
}

@media (max-width:1100px){

    .features-grid{
        grid-template-columns:repeat(2,1fr);
    }

}

@media (max-width:768px){

    .features-grid{
        grid-template-columns:1fr;
    }

}

</style>