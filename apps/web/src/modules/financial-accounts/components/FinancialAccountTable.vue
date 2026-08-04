<template>

    <section class="financial-account-table">

        <div class="table-wrapper">

            <table>

                <thead>

                    <tr>

                        <th class="account-column">
                            Conta
                        </th>

                        <th>
                            Instituição
                        </th>

                        <th>
                            Tipo
                        </th>

                        <th class="text-right">
                            Saldo Atual
                        </th>

                        <th class="text-center">
                            Fluxo
                        </th>

                        <th class="text-center">
                            Patrimônio
                        </th>

                        <th class="text-center">
                            Status
                        </th>

                        <th class="actions-column">
                            Ações
                        </th>

                    </tr>

                </thead>

                <tbody>

                    <FinancialAccountTableRow
                        v-for="account in accounts"
                        :key="account.id"
                        :account="account"
                        @view="emit('view', $event)"
                        @edit="emit('edit', $event)"
                        @delete="emit('delete', $event)"
                    />

                    <tr
                        v-if="accounts.length === 0"
                        class="empty-row"
                    >

                        <td
                            colspan="8"
                        >

                            <div class="empty-state">

                                <h3>

                                    Nenhuma conta encontrada

                                </h3>

                                <p>

                                    Cadastre sua primeira conta financeira
                                    para começar a controlar seu patrimônio.

                                </p>

                            </div>

                        </td>

                    </tr>

                </tbody>

            </table>

        </div>

    </section>

</template>

<script setup lang="ts">

/**
 * ============================================================================
 * Financial Account Table
 * ============================================================================
 *
 * Pure presentation component responsible only for rendering the list of
 * Financial Accounts.
 *
 * Responsibilities
 * ----------------------------------------------------------------------------
 *
 * • Render the table header.
 *
 * • Render FinancialAccountTableRow components.
 *
 * • Display the empty state.
 *
 * • Emit user actions.
 *
 * This component intentionally contains no business rules, pagination,
 * filtering or sorting logic.
 */

import FinancialAccountTableRow
from "./FinancialAccountTableRow.vue";

import type {

    FinancialAccount,

} from "../types/financial-account";

defineProps<{

    accounts: FinancialAccount[];

}>();

const emit = defineEmits<{

    (

        event: "view",

        account: FinancialAccount,

    ): void;

    (

        event: "edit",

        account: FinancialAccount,

    ): void;

    (

        event: "delete",

        account: FinancialAccount,

    ): void;

}>();

</script>

<style scoped>

.financial-account-table{

    display:flex;

    flex-direction:column;

    width:100%;

}

.table-wrapper{

    width:100%;

    overflow-x:auto;

    background:#ffffff;

    border:1px solid #e2e8f0;

    border-radius:18px;

    box-shadow:

        0 8px 24px rgba(15,23,42,.05);

}

/* ==========================================================
   Table
========================================================== */

table{

    width:100%;

    min-width:1180px;

    border-collapse:collapse;

}

/* ==========================================================
   Header
========================================================== */

thead{

    background:#f8fafc;

}

thead tr{

    border-bottom:1px solid #e2e8f0;

}

th{

    padding:1rem 1.25rem;

    font-size:.82rem;

    font-weight:700;

    color:#64748b;

    text-transform:uppercase;

    letter-spacing:.05em;

    white-space:nowrap;

}

.account-column{

    width:340px;

}

.actions-column{

    width:160px;

    text-align:center;

}

.text-right{

    text-align:right;

}

.text-center{

    text-align:center;

}

/* ==========================================================
   Body
========================================================== */

tbody tr{

    transition:

        background-color .2s ease;

}

tbody tr:hover{

    background:#f8fafc;

}

tbody tr:not(:last-child){

    border-bottom:1px solid #edf2f7;

}

/* ==========================================================
   Empty State
========================================================== */

.empty-row td{

    padding:4rem 2rem;

    border:none;

}

.empty-state{

    display:flex;

    flex-direction:column;

    align-items:center;

    justify-content:center;

    gap:1rem;

    text-align:center;

}

.empty-state h3{

    margin:0;

    color:#0f172a;

    font-size:1.4rem;

    font-weight:700;

}

.empty-state p{

    margin:0;

    max-width:460px;

    color:#64748b;

    line-height:1.7;

}

/* ==========================================================
   Scrollbar
========================================================== */

.table-wrapper::-webkit-scrollbar{

    height:10px;

}

.table-wrapper::-webkit-scrollbar-track{

    background:#f1f5f9;

}

.table-wrapper::-webkit-scrollbar-thumb{

    background:#cbd5e1;

    border-radius:999px;

}

.table-wrapper::-webkit-scrollbar-thumb:hover{

    background:#94a3b8;

}

/* ==========================================================
   Sticky Header
========================================================== */

thead th{

    position:sticky;

    top:0;

    z-index:2;

    background:#f8fafc;

}

/* ==========================================================
   Rounded Corners
========================================================== */

thead th:first-child{

    border-top-left-radius:18px;

}

thead th:last-child{

    border-top-right-radius:18px;

}

/* ==========================================================
   Responsive
========================================================== */

@media (max-width:1200px){

    table{

        min-width:1080px;

    }

}

@media (max-width:992px){

    table{

        min-width:960px;

    }

    th{

        padding:.95rem 1rem;

        font-size:.78rem;

    }

}

@media (max-width:768px){

    .table-wrapper{

        border-radius:14px;

    }

    table{

        min-width:900px;

    }

    th{

        padding:.85rem .9rem;

        font-size:.75rem;

    }

}

/* ==========================================================
   Visual Refinements
========================================================== */

.table-wrapper{

    transition:

        box-shadow .2s ease,

        border-color .2s ease;

}

.table-wrapper:hover{

    border-color:#d6dee8;

    box-shadow:

        0 12px 30px rgba(15,23,42,.08);

}

tbody tr:hover td{

    background:#fbfdff;

}

thead th{

    user-select:none;

}

th:last-child,

td:last-child{

    white-space:nowrap;

}

.empty-state{

    padding:1rem;

}

.empty-state h3{

    letter-spacing:-.02em;

}

.empty-state p{

    font-size:.95rem;

}
</style>