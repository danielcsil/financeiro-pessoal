<template>
    <section class="summary-grid">
        <article class="summary-card">
            <div class="summary-card__icon summary-card__icon--blue">
                <AppIcon name="wallet" />
            </div>

            <div class="summary-card__content">
                <span class="summary-card__label">
                    Contas Financeiras
                </span>

                <strong class="summary-card__value">
                    {{ accounts.length }}
                </strong>

                <small class="summary-card__description">
                    contas cadastradas
                </small>
            </div>
        </article>

        <article class="summary-card">
            <div class="summary-card__icon summary-card__icon--green">
                <AppIcon name="coins" />
            </div>

            <div class="summary-card__content">
                <span class="summary-card__label">
                    Patrimônio
                </span>

                <strong class="summary-card__value">
                    {{ formatCurrency(totalBalance) }}
                </strong>

                <small class="summary-card__description">
                    saldo consolidado
                </small>
            </div>
        </article>

        <article class="summary-card">
            <div class="summary-card__icon summary-card__icon--purple">
                <AppIcon name="chart-line" />
            </div>

            <div class="summary-card__content">
                <span class="summary-card__label">
                    Fluxo de Caixa
                </span>

                <strong class="summary-card__value">
                    {{ cashFlowAccounts }}
                </strong>

                <small class="summary-card__description">
                    contas incluídas
                </small>
            </div>
        </article>

        <article class="summary-card">
            <div class="summary-card__icon summary-card__icon--orange">
                <AppIcon name="calculator" />
            </div>

            <div class="summary-card__content">
                <span class="summary-card__label">
                    Saldo Médio
                </span>

                <strong class="summary-card__value">
                    {{ formatCurrency(averageBalance) }}
                </strong>

                <small class="summary-card__description">
                    por conta financeira
                </small>
            </div>
        </article>
    </section>
</template>

<script setup lang="ts">
/**
 * ============================================================================
 * Financial Account Summary
 * ============================================================================
 *
 * Displays the main financial indicators related to the user's financial
 * accounts.
 *
 * This component is presentation-only and contains no business logic.
 */

import { computed } from "vue";

import AppIcon from "@/shared/components/AppIcon.vue";

import type {
    FinancialAccount,
} from "../types/financial-account";

const props = defineProps<{
    accounts: FinancialAccount[];
}>();

const totalBalance = computed(() =>
    props.accounts.reduce(
        (total, account) => total + account.currentBalance,
        0,
    ),
);

const averageBalance = computed(() => {
    if (props.accounts.length === 0) {
        return 0;
    }

    return totalBalance.value / props.accounts.length;
});

const cashFlowAccounts = computed(() =>
    props.accounts.filter(
        account => account.includeInCashFlow,
    ).length,
);

function formatCurrency(value: number): string {
    return new Intl.NumberFormat(
        "pt-BR",
        {
            style: "currency",
            currency: "BRL",
        },
    ).format(value);
}
</script>

<style scoped>
.summary-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 1.5rem;
}

.summary-card {
    display: flex;
    align-items: center;
    gap: 1.25rem;

    padding: 1.5rem;

    background: #ffffff;

    border: 1px solid #e2e8f0;
    border-radius: 18px;

    transition: all .2s ease;

    box-shadow:
        0 1px 2px rgba(15, 23, 42, .05),
        0 8px 24px rgba(15, 23, 42, .04);
}

.summary-card:hover {
    transform: translateY(-2px);

    box-shadow:
        0 4px 8px rgba(15,23,42,.08),
        0 16px 32px rgba(15,23,42,.08);
}

.summary-card__icon {
    width: 58px;
    height: 58px;

    border-radius: 16px;

    display: flex;
    align-items: center;
    justify-content: center;

    flex-shrink: 0;
}

.summary-card__icon--blue {
    background: #dbeafe;
    color: #2563eb;
}

.summary-card__icon--green {
    background: #dcfce7;
    color: #16a34a;
}

.summary-card__icon--purple {
    background: #ede9fe;
    color: #7c3aed;
}

.summary-card__icon--orange {
    background: #ffedd5;
    color: #ea580c;
}

.summary-card__content {
    display: flex;
    flex-direction: column;
}

.summary-card__label {
    color: #64748b;
    font-size: .82rem;
    font-weight: 500;
    margin-bottom: .35rem;
}

.summary-card__value {
    color: #0f172a;
    font-size: 1.45rem;
    font-weight: 700;
    line-height: 1.2;
}

.summary-card__description {
    margin-top: .35rem;
    color: #94a3b8;
    font-size: .78rem;
}

@media (max-width: 1200px) {
    .summary-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 768px) {
    .summary-grid {
        grid-template-columns: 1fr;
    }
}
</style>