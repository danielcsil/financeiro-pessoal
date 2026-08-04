<template>

    <section class="account-grid">

        <FinancialAccountCard
            v-for="account in accounts"
            :key="account.id"
            :account="account"
            @details="$emit('details', $event)"
            @menu="$emit('menu', $event)"
        />

    </section>

</template>

<script setup lang="ts">

import FinancialAccountCard
from "./FinancialAccountCard.vue";

import type {
    FinancialAccount,
} from "../types/financial-account";

defineProps<{

    accounts: FinancialAccount[];

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

</script>

<style scoped>

.account-grid{

    display:grid;

    gap:1.75rem;

    grid-template-columns:
        repeat(
            auto-fill,
            minmax(340px,1fr)
        );

    align-items:start;

}

@media (max-width:1024px){

    .account-grid{

        grid-template-columns:
            repeat(
                auto-fill,
                minmax(300px,1fr)
            );

    }

}

@media (max-width:768px){

    .account-grid{

        grid-template-columns:1fr;

        gap:1rem;

    }

}

</style>