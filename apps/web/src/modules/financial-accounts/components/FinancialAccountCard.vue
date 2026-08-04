<template>

    <article
        class="account-card"
        @click="$emit('details', account)"
    >

        <!-- ====================================================== -->
        <!-- Header -->
        <!-- ====================================================== -->

        <header class="header">

            <div
                class="icon"
                :style="{ backgroundColor: account.color }"
            >
                {{ icon }}
            </div>

            <button
                class="menu-button"
                @click.stop="$emit('menu', account)"
            >
                ⋮
            </button>

        </header>

        <!-- ====================================================== -->
        <!-- Body -->
        <!-- ====================================================== -->

        <div class="body">

            <h3>
                {{ account.name }}
            </h3>

            <p
                v-if="account.institution"
                class="institution"
            >
                {{ account.institution }}
            </p>

            <div class="balance">

                {{ formatCurrency(account.currentBalance) }}

            </div>

        </div>

        <!-- ====================================================== -->
        <!-- Footer -->
        <!-- ====================================================== -->

        <footer class="footer">

            <span
                class="badge"
                v-if="account.includeInCashFlow"
            >
                Fluxo de Caixa
            </span>

            <span
                class="badge secondary"
                v-if="account.includeInNetWorth"
            >
                Patrimônio
            </span>

        </footer>

    </article>

</template>

<script setup lang="ts">

import { computed } from "vue";

import type {
    FinancialAccount,
} from "../types/financial-account";

const props = defineProps<{

    account: FinancialAccount;

}>();

defineEmits<{

    (
        event: "details",
        account: FinancialAccount,
    ): void;

    (
        event: "menu",
        account: FinancialAccount,
    ): void;

}>();

const icons: Record<string, string> = {

    wallet: "👛",

    bank: "🏦",

    cash: "💵",

    coins: "🪙",

    chart: "📈",

    "credit-card": "💳",

    "piggy-bank": "🐷",

    building: "🏢",

    safe: "🔐",

};

const icon = computed(() => {

    return icons[
        props.account.icon
    ] ?? "💼";

});

function formatCurrency(
    value: number,
): string {

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

.account-card{

    background:white;

    border-radius:22px;

    padding:1.5rem;

    border:1px solid #e5e7eb;

    display:flex;

    flex-direction:column;

    gap:1.5rem;

    cursor:pointer;

    transition:.25s;

    box-shadow:

        0 10px 30px rgba(15,23,42,.04);

}

.account-card:hover{

    transform:translateY(-6px);

    box-shadow:

        0 25px 50px rgba(15,23,42,.10);

}

.header{

    display:flex;

    justify-content:space-between;

    align-items:center;

}

.icon{

    width:56px;

    height:56px;

    border-radius:18px;

    display:flex;

    align-items:center;

    justify-content:center;

    color:white;

    font-size:1.7rem;

}

.menu-button{

    border:none;

    background:transparent;

    cursor:pointer;

    font-size:1.2rem;

    color:#64748b;

    width:36px;

    height:36px;

    border-radius:10px;

}

.menu-button:hover{

    background:#f1f5f9;

}

.body{

    display:flex;

    flex-direction:column;

    gap:.4rem;

}

.body h3{

    margin:0;

    color:#0f172a;

    font-size:1.2rem;

}

.institution{

    margin:0;

    color:#64748b;

}

.balance{

    margin-top:1rem;

    font-size:2rem;

    font-weight:700;

    color:#0f172a;

}

.footer{

    display:flex;

    flex-wrap:wrap;

    gap:.5rem;

}

.badge{

    padding:.45rem .8rem;

    border-radius:999px;

    background:#dbeafe;

    color:#2563eb;

    font-size:.75rem;

    font-weight:600;

}

.secondary{

    background:#ecfdf5;

    color:#059669;

}

</style>