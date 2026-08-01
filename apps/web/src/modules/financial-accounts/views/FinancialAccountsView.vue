<script setup lang="ts">
/**
 * =============================================================================
 * Financial Accounts View
 * =============================================================================
 *
 * Purpose
 * =============================================================================
 *
 * Main screen responsible for managing the user's financial accounts.
 *
 * This component orchestrates the interaction between the UI and the
 * application layer.
 *
 * Responsibilities
 * ----------------
 *
 * • Load financial accounts.
 * • Display the account list.
 * • Open and close the account form.
 * • Create accounts.
 * • Edit accounts.
 *
 * No HTTP communication happens here.
 */

import { computed, onMounted, ref } from "vue";

import BaseButton from "@/shared/components/base/BaseButton.vue";
import BaseModal from "@/shared/components/base/BaseModal.vue";

import FinancialAccountForm
    from "../components/FinancialAccountForm.vue";

import FinancialAccountsList
    from "../components/FinancialAccountsList.vue";

import { useFinancialAccounts }
    from "../composables/useFinancialAccounts";

import type {
    CreateFinancialAccountRequest,
    FinancialAccount,
    UpdateFinancialAccountRequest,
} from "../types/financial-account";

const {
    accounts,
    loading,
    error,
    loadAccounts,
    createAccount,
    updateAccount,
    totalAccounts,
    totalBalance,
} = useFinancialAccounts();

const modalOpen = ref(false);

const selectedAccount =
    ref<FinancialAccount>();

const editing = computed(
    () => selectedAccount.value !== undefined,
);

/**
 * Loads accounts when the page opens.
 */
onMounted(async () => {

    await loadAccounts();

});

/**
 * Opens the creation modal.
 */
function newAccount(): void {

    selectedAccount.value = undefined;

    modalOpen.value = true;

}

/**
 * Opens the edition modal.
 */
function editAccount(
    account: FinancialAccount,
): void {

    selectedAccount.value = account;

    modalOpen.value = true;

}

/**
 * Closes the modal.
 */
function closeModal(): void {

    modalOpen.value = false;

    selectedAccount.value = undefined;

}

/**
 * Persists the account.
 */
async function saveAccount(
    request:
        | CreateFinancialAccountRequest
        | UpdateFinancialAccountRequest,
): Promise<void> {

    if (editing.value) {

        await updateAccount(
            selectedAccount.value!.id,
            request as UpdateFinancialAccountRequest,
        );

    } else {

        await createAccount(
            request as CreateFinancialAccountRequest,
        );

    }

    closeModal();

}
</script>

<template>

<section class="financial-accounts">

    <header class="page-header">

        <div>

            <h1>

                Financial Accounts

            </h1>

            <p>

                Manage all accounts used in your financial planning.

            </p>

        </div>

        <BaseButton
            @click="newAccount"
        >

            New Account

        </BaseButton>

    </header>

    <section class="summary">

        <article class="summary-card">

            <strong>

                {{ totalAccounts }}

            </strong>

            <span>

                Accounts

            </span>

        </article>

        <article class="summary-card">

            <strong>

                {{ totalBalance }}

            </strong>

            <span>

                Total Balance

            </span>

        </article>

    </section>

    <div
        v-if="error"
        class="error"
    >

        {{ error }}

    </div>

    <FinancialAccountsList
        :accounts="accounts"
        :loading="loading"
        @create="newAccount"
        @edit="editAccount"
    />

    <BaseModal
        :open="modalOpen"
        width="700px"
        @close="closeModal"
    >

        <template #header>

            <h2>

                {{
                    editing
                        ? "Edit Account"
                        : "New Financial Account"
                }}

            </h2>

        </template>

        <FinancialAccountForm
            :account="selectedAccount"
            :submitting="loading"
            @submit="saveAccount"
            @cancel="closeModal"
        />

    </BaseModal>

</section>

</template>

<style scoped>

.financial-accounts{

    display:flex;

    flex-direction:column;

    gap:2rem;

}

.page-header{

    display:flex;

    justify-content:space-between;

    align-items:center;

}

.page-header h1{

    margin:0;

}

.page-header p{

    margin-top:.35rem;

    color:var(--color-text-secondary);

}

.summary{

    display:grid;

    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

    gap:1rem;

}

.summary-card{

    background:var(--color-surface);

    border:1px solid var(--color-border);

    border-radius:1rem;

    padding:1.5rem;

    display:flex;

    flex-direction:column;

    gap:.5rem;

}

.summary-card strong{

    font-size:2rem;

    color:var(--color-primary);

}

.error{

    padding:1rem;

    border-radius:.75rem;

    background:#fee2e2;

    color:#991b1b;

}

</style>