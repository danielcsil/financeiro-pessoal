<script setup lang="ts">
/**
 * =============================================================================
 * Financial Accounts List
 * =============================================================================
 *
 * Purpose
 * =============================================================================
 *
 * Displays the financial accounts belonging to the authenticated user.
 *
 * This component is intentionally presentation-only.
 *
 * Responsibilities
 * ----------------
 *
 * • Display every financial account.
 *
 * • Show an empty state.
 *
 * • Show a loading state.
 *
 * • Allow editing.
 *
 * Business logic is delegated to the parent component.
 */

import BaseButton from "@/shared/components/base/BaseButton.vue";

import type {
    FinancialAccount,
} from "../types/financial-account";

interface Props {

    accounts: FinancialAccount[];

    loading?: boolean;

}

withDefaults(
    defineProps<Props>(),
    {
        loading: false,
    },
);

const emit = defineEmits<{

    create: [];

    edit: [account: FinancialAccount];

}>();

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

<template>

<section class="accounts-list">

    <!-- ================================================================ -->
    <!-- Loading -->
    <!-- ================================================================ -->

    <div
        v-if="loading"
        class="loading"
    >

        Loading financial accounts...

    </div>

    <!-- ================================================================ -->
    <!-- Empty State -->
    <!-- ================================================================ -->

    <div
        v-else-if="accounts.length === 0"
        class="empty-state"
    >

        <h2>

            No financial accounts yet

        </h2>

        <p>

            Create your first financial account to start managing
            your finances.

        </p>

        <BaseButton
            @click="emit('create')"
        >

            Create Account

        </BaseButton>

    </div>

    <!-- ================================================================ -->
    <!-- Cards -->
    <!-- ================================================================ -->

    <div
        v-else
        class="grid"
    >

        <article
            v-for="account in accounts"
            :key="account.id"
            class="account-card"
        >

            <header>

                <div
                    class="account-color"
                    :style="{
                        background: account.color,
                    }"
                />

                <div class="account-info">

                    <h3>

                        {{ account.name }}

                    </h3>

                    <small>

                        {{ account.institution ?? "No institution" }}

                    </small>

                </div>

            </header>

            <section class="account-body">

                <div class="row">

                    <span>

                        Type

                    </span>

                    <strong>

                        {{ account.accountType }}

                    </strong>

                </div>

                <div class="row">

                    <span>

                        Current Balance

                    </span>

                    <strong>

                        {{
                            formatCurrency(
                                account.currentBalance,
                            )
                        }}

                    </strong>

                </div>

            </section>

            <footer>

                <BaseButton
                    variant="secondary"
                    @click="emit('edit', account)"
                >

                    Edit

                </BaseButton>

            </footer>

        </article>

    </div>

</section>

</template>

<style scoped>

.accounts-list{

    display:flex;

    flex-direction:column;

}

.loading{

    padding:3rem;

    text-align:center;

    color:var(--color-text-secondary);

}

.empty-state{

    display:flex;

    flex-direction:column;

    align-items:center;

    gap:1rem;

    padding:4rem;

    border:2px dashed var(--color-border);

    border-radius:1rem;

}

.empty-state h2{

    margin:0;

}

.empty-state p{

    max-width:500px;

    text-align:center;

    color:var(--color-text-secondary);

}

.grid{

    display:grid;

    grid-template-columns:repeat(auto-fit,minmax(320px,1fr));

    gap:1.5rem;

}

.account-card{

    display:flex;

    flex-direction:column;

    gap:1.5rem;

    padding:1.5rem;

    background:var(--color-surface);

    border:1px solid var(--color-border);

    border-radius:1rem;

    transition:.2s;

}

.account-card:hover{

    transform:translateY(-2px);

    box-shadow:0 12px 30px rgba(0,0,0,.06);

}

.account-card header{

    display:flex;

    align-items:center;

    gap:1rem;

}

.account-color{

    width:18px;

    height:18px;

    border-radius:50%;

    flex-shrink:0;

}

.account-info{

    display:flex;

    flex-direction:column;

}

.account-info h3{

    margin:0;

}

.account-info small{

    color:var(--color-text-secondary);

}

.account-body{

    display:flex;

    flex-direction:column;

    gap:.75rem;

}

.row{

    display:flex;

    justify-content:space-between;

    align-items:center;

}

footer{

    display:flex;

    justify-content:flex-end;

}

</style>