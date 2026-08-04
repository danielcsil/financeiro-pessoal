<template>

    <section class="financial-accounts-view">

        <!-- ==========================================================
             Header
        =========================================================== -->

        <header class="page-header">

            <div class="page-header__content">

                <h1>

                    Contas Financeiras

                </h1>

                <p>

                    Gerencie todas as suas contas bancárias,
                    investimentos, carteiras e demais ativos
                    financeiros em um único lugar.

                </p>

            </div>

            <AppButton
                size="lg"
                @click="openCreateModal"
            >

                + Nova Conta

            </AppButton>

        </header>

        <!-- ==========================================================
             Summary
        =========================================================== -->

        <FinancialAccountSummary
            :accounts="store.accounts"
        />

        <!-- ==========================================================
             Toolbar
        =========================================================== -->

        <FinancialAccountToolbar
            @filter="store.setFilters"
        />

        <!-- ==========================================================
             Loading
        =========================================================== -->

        <div
            v-if="store.loading"
            class="loading-container"
        >

            Carregando contas...

        </div>

        <!-- ==========================================================
             Table
        =========================================================== -->

        <FinancialAccountTable

            v-else

            :accounts="store.paginatedAccounts"

            @view="viewAccount"

            @edit="editAccount"

            @delete="deleteAccount"

        />

        <!-- ==========================================================
             Pagination
        =========================================================== -->

        <AppPagination

            v-if="store.filteredAccounts.length"

            v-model:current-page="currentPage"

            v-model:page-size="pageSize"

            :total-items="store.filteredAccounts.length"

        />

        <!-- ==========================================================
             Modal
        =========================================================== -->

        <FinancialAccountModal

            v-model="showModal"

            :loading="store.saving"

            @save="createAccount"

        />

    </section>

</template>

<script setup lang="ts">

/**
 * ============================================================================
 * Financial Accounts View
 * ============================================================================
 *
 * Main page responsible for composing the Financial Accounts module.
 *
 * This component intentionally contains almost no business logic.
 *
 * All module state is centralized inside the Pinia Store.
 */

import {

    onMounted,

    ref,

} from "vue";

import {

    storeToRefs,

} from "pinia";

import AppButton
from "@/shared/components/AppButton.vue";

import AppPagination
from "@/shared/components/AppPagination.vue";

import FinancialAccountSummary
from "../components/FinancialAccountSummary.vue";

import FinancialAccountToolbar
from "../components/FinancialAccountToolbar.vue";

import FinancialAccountTable
from "../components/FinancialAccountTable.vue";

import FinancialAccountModal
from "../components/FinancialAccountModal.vue";

import {

    useFinancialAccountStore,

} from "../stores/financial-account.store";

import type {

    CreateFinancialAccountRequest,

    FinancialAccount,

} from "../types/financial-account";

const store =
    useFinancialAccountStore();

const {

    currentPage,

    pageSize,

} = storeToRefs(store);

const showModal =
    ref(false);

/* ==========================================================================
   Lifecycle
========================================================================== */

onMounted(

    store.load,

);

/* ==========================================================================
   Modal
========================================================================== */

function openCreateModal(): void {

    showModal.value = true;

}

function closeCreateModal(): void {

    showModal.value = false;

}

/* ==========================================================================
   Create
========================================================================== */

async function createAccount(

    request: CreateFinancialAccountRequest,

): Promise<void> {

    try {

        await store.create(

            request,

        );

        closeCreateModal();

    }

    catch (error) {

        console.error(

            "Unable to create financial account.",

            error,

        );

    }

}

/* ==========================================================================
   View
========================================================================== */

function viewAccount(

    account: FinancialAccount,

): void {

    store.selectAccount(

        account,

    );

    console.log(

        "View account:",

        account,

    );

}

/* ==========================================================================
   Edit
========================================================================== */

function editAccount(

    account: FinancialAccount,

): void {

    store.selectAccount(

        account,

    );

    console.log(

        "Edit account:",

        account,

    );

}

/* ==========================================================================
   Delete
========================================================================== */

function deleteAccount(

    account: FinancialAccount,

): void {

    store.selectAccount(

        account,

    );

    console.log(

        "Delete account:",

        account,

    );

}

</script>

<style scoped>

/* ==========================================================================
   Layout
========================================================================== */

.financial-accounts-view{

    display:flex;

    flex-direction:column;

    gap:2rem;

    width:100%;

    padding:2rem;

    background:#f8fafc;

    min-height:100%;

}

/* ==========================================================================
   Header
========================================================================== */

.page-header{

    display:flex;

    justify-content:space-between;

    align-items:flex-start;

    gap:2rem;

}

.page-header__content{

    display:flex;

    flex-direction:column;

    gap:.65rem;

}

.page-header h1{

    margin:0;

    color:#0f172a;

    font-size:2rem;

    font-weight:700;

    letter-spacing:-.02em;

}

.page-header p{

    margin:0;

    max-width:760px;

    color:#64748b;

    line-height:1.7;

    font-size:.98rem;

}

/* ==========================================================================
   Loading
========================================================================== */

.loading-container{

    display:flex;

    justify-content:center;

    align-items:center;

    min-height:320px;

    border:1px solid #e2e8f0;

    border-radius:18px;

    background:#ffffff;

    color:#64748b;

    box-shadow:

        0 10px 24px rgba(15,23,42,.04);

}

/* ==========================================================================
   Component spacing
========================================================================== */

.financial-accounts-view > *{

    width:100%;

}

:deep(.financial-account-summary){

    transition:.25s;

}

:deep(.financial-account-toolbar){

    transition:.25s;

}

:deep(.financial-account-table){

    transition:.25s;

}

:deep(.app-pagination){

    margin-top:.5rem;

}

/* ==========================================================================
   Animation
========================================================================== */

.financial-accounts-view > *{

    animation:

        fadeIn .25s ease;

}

@keyframes fadeIn{

    from{

        opacity:0;

        transform:translateY(8px);

    }

    to{

        opacity:1;

        transform:translateY(0);

    }

}

/* ==========================================================================
   Responsive
========================================================================== */

@media(max-width:1280px){

    .financial-accounts-view{

        padding:1.5rem;

        gap:1.75rem;

    }

}

@media(max-width:992px){

    .financial-accounts-view{

        padding:1.25rem;

        gap:1.5rem;

    }

    .page-header{

        flex-direction:column;

        align-items:flex-start;

        gap:1.5rem;

    }

    .page-header :deep(button){

        width:100%;

    }

    .page-header h1{

        font-size:1.8rem;

    }

}

@media(max-width:768px){

    .financial-accounts-view{

        padding:1rem;

        gap:1.25rem;

    }

    .page-header h1{

        font-size:1.55rem;

    }

    .page-header p{

        font-size:.92rem;

        max-width:100%;

    }

}

@media(max-width:576px){

    .financial-accounts-view{

        padding:.75rem;

    }

}

</style>