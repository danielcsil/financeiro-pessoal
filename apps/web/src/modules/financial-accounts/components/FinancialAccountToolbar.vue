<template>

    <section class="toolbar">

        <div class="toolbar__search">

            <AppInput
                v-model="filters.search"
                placeholder="Pesquisar por nome, instituição..."
                @update:model-value="emitFilters"
            />

        </div>

        <div class="toolbar__filters">

            <AppSelect
                v-model="filters.accountType"
                placeholder="Tipo"
                :options="accountTypes"
                @update:model-value="emitFilters"
            />

            <AppSelect
                v-model="filters.institution"
                placeholder="Instituição"
                :options="institutionOptions"
                @update:model-value="emitFilters"
            />

            <AppSelect
                v-model="filters.status"
                placeholder="Status"
                :options="statusOptions"
                @update:model-value="emitFilters"
            />

        </div>

        <div class="toolbar__actions">

            <AppButton
                variant="ghost"
                @click="clearFilters"
            >

                Limpar filtros

            </AppButton>

            <AppButton
                @click="emit('create')"
            >

                + Nova Conta

            </AppButton>

        </div>

    </section>

</template>

<script setup lang="ts">

/**
 * ============================================================================
 * Financial Account Toolbar
 * ============================================================================
 *
 * Purpose
 * ============================================================================
 *
 * Provides searching and filtering capabilities for the Financial Accounts
 * module.
 *
 * This component is intentionally presentation-only and delegates all business
 * rules to the parent View.
 *
 * ============================================================================
 * Responsibilities
 * ============================================================================
 *
 * • Search accounts.
 *
 * • Filter by account type.
 *
 * • Filter by institution.
 *
 * • Filter by status.
 *
 * • Notify filter changes.
 *
 * • Request creation of a new account.
 */

import { reactive } from "vue";

import AppButton from "@/shared/components/AppButton.vue";
import AppInput from "@/shared/components/AppInput.vue";
import AppSelect from "@/shared/components/AppSelect.vue";

export interface FinancialAccountFilters {

    search: string;

    accountType: string;

    institution: string;

    status: string;

}

const emit = defineEmits<{

    (

        event: "filter",

        filters: FinancialAccountFilters,

    ): void;

    (

        event: "create",

    ): void;

}>();

const filters = reactive<FinancialAccountFilters>({

    search: "",

    accountType: "",

    institution: "",

    status: "",

});

const accountTypes = [

    {
        label: "Todos os tipos",
        value: "",
    },

    {
        label: "Conta Corrente",
        value: "CHECKING",
    },

    {
        label: "Poupança",
        value: "SAVINGS",
    },

    {
        label: "Carteira",
        value: "CASH",
    },

    {
        label: "Carteira Digital",
        value: "DIGITAL_WALLET",
    },

    {
        label: "Investimento",
        value: "INVESTMENT",
    },

    {
        label: "Outras",
        value: "OTHER",
    },

];

const institutionOptions = [

    {
        label: "Todas",
        value: "",
    },

];

const statusOptions = [

    {
        label: "Todos",
        value: "",
    },

    {
        label: "Ativas",
        value: "ACTIVE",
    },

    {
        label: "Inativas",
        value: "INACTIVE",
    },

];

function emitFilters(): void {

    emit(

        "filter",

        {

            ...filters,

        },

    );

}

function clearFilters(): void {

    filters.search = "";

    filters.accountType = "";

    filters.institution = "";

    filters.status = "";

    emitFilters();

}

</script>

<style scoped>

/* ==========================================================================
   Toolbar
========================================================================== */

.toolbar{

    display:flex;

    align-items:center;

    justify-content:space-between;

    gap:1.5rem;

    padding:1.5rem;

    background:white;

    border:1px solid #e2e8f0;

    border-radius:18px;

    box-shadow:

        0 8px 20px rgba(15,23,42,.04);

}

/* ==========================================================================
   Search
========================================================================== */

.toolbar__search{

    flex:1;

    min-width:320px;

}

.toolbar__search :deep(input){

    height:46px;

}

/* ==========================================================================
   Filters
========================================================================== */

.toolbar__filters{

    display:flex;

    align-items:center;

    gap:1rem;

}

.toolbar__filters > *{

    min-width:180px;

}

/* ==========================================================================
   Actions
========================================================================== */

.toolbar__actions{

    display:flex;

    align-items:center;

    gap:.75rem;

}

/* ==========================================================================
   Ghost Button
========================================================================== */

.toolbar__actions :deep(.ghost){

    color:#475569;

}

/* ==========================================================================
   Responsive
========================================================================== */

@media (max-width:1200px){

    .toolbar{

        flex-wrap:wrap;

    }

    .toolbar__search{

        width:100%;

        min-width:100%;

    }

    .toolbar__filters{

        flex:1;

        flex-wrap:wrap;

    }

}

@media (max-width:992px){

    .toolbar{

        flex-direction:column;

        align-items:stretch;

    }

    .toolbar__filters{

        display:grid;

        grid-template-columns:

            repeat(

                auto-fit,

                minmax(180px,1fr)

            );

    }

    .toolbar__actions{

        justify-content:flex-end;

    }

}

@media (max-width:768px){

    .toolbar{

        padding:1rem;

    }

    .toolbar__filters{

        grid-template-columns:1fr;

    }

    .toolbar__actions{

        width:100%;

        flex-direction:column;

    }

    .toolbar__actions > *{

        width:100%;

    }

}

/* ==========================================================================
   Visual Refinements
========================================================================== */

.toolbar__search{

    position:relative;

}

.toolbar__filters :deep(select){

    height:46px;

}

.toolbar__filters :deep(.app-select){

    width:100%;

}

.toolbar__search :deep(input),

.toolbar__filters :deep(select){

    transition:

        border-color .2s,

        box-shadow .2s;

}

.toolbar__search :deep(input:focus),

.toolbar__filters :deep(select:focus){

    border-color:#2563eb;

    box-shadow:

        0 0 0 4px rgba(37,99,235,.12);

}

.toolbar__actions{

    white-space:nowrap;

}

.toolbar__actions :deep(button){

    min-width:150px;

}

/* ==========================================================================
   Large Screens
========================================================================== */

@media (min-width:1600px){

    .toolbar{

        gap:2rem;

    }

    .toolbar__filters{

        gap:1.25rem;

    }

}

/* ==========================================================================
   Accessibility
========================================================================== */

.toolbar :deep(button:focus-visible),

.toolbar :deep(input:focus-visible),

.toolbar :deep(select:focus-visible){

    outline:none;

}

/* ==========================================================================
   End
========================================================================== */

</style>