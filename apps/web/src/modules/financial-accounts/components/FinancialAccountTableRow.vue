<template>

    <tr class="table-row">

        <td>

            <div class="account">

                <div
                    class="account-icon"
                    :style="{
                        backgroundColor: account.color + '20',
                        color: account.color,
                    }"
                >

                    <AppIcon
                        :name="account.icon"
                        :size="18"
                    />

                </div>

                <div class="account-content">

                    <strong>
                        {{ account.name }}
                    </strong>

                    <small>
                        {{ account.institution ?? "-" }}
                    </small>

                </div>

            </div>

        </td>

        <td>

            {{ account.institution ?? "-" }}

        </td>

        <td>

            <AppBadge variant="primary">

                {{ accountTypeLabel }}

            </AppBadge>

        </td>

        <td class="text-right balance">

            {{ formattedBalance }}

        </td>

        <td class="text-center">

            <span
                class="flag"
                :class="{
                    enabled: account.includeInCashFlow,
                }"
            >

                <AppIcon
                    :name="
                        account.includeInCashFlow
                            ? 'check'
                            : 'close'
                    "
                    :size="16"
                />

            </span>

        </td>

        <td class="text-center">

            <span
                class="flag"
                :class="{
                    enabled: account.includeInNetWorth,
                }"
            >

                <AppIcon
                    :name="
                        account.includeInNetWorth
                            ? 'check'
                            : 'close'
                    "
                    :size="16"
                />

            </span>

        </td>

        <td class="text-center">

            <AppBadge
                :variant="
                    account.active
                        ? 'success'
                        : 'danger'
                "
            >

                {{ account.active ? "Ativa" : "Inativa" }}

            </AppBadge>

        </td>

        <td class="text-center">

            <FinancialAccountActions
                :account="account"
                @view="emit('view', $event)"
                @edit="emit('edit', $event)"
                @delete="emit('delete', $event)"
            />

        </td>

    </tr>

</template>

<script setup lang="ts">

import { computed } from "vue";

import AppBadge from "@/shared/components/AppBadge.vue";
import AppIcon from "@/shared/components/AppIcon.vue";

import FinancialAccountActions
from "./FinancialAccountActions.vue";

import {

    AccountType,

} from "../types/financial-account";

import type {

    FinancialAccount,

} from "../types/financial-account";

const props = defineProps<{

    account: FinancialAccount;

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

const formattedBalance = computed(() =>

    new Intl.NumberFormat(

        "pt-BR",

        {

            style: "currency",

            currency: "BRL",

        },

    ).format(

        props.account.currentBalance,

    ),

);

const accountTypeLabel = computed(() => {

    switch (props.account.accountType) {

        case AccountType.CHECKING:
            return "Conta Corrente";

        case AccountType.SAVINGS:
            return "Poupança";

        case AccountType.INVESTMENT:
            return "Investimento";

        case AccountType.CASH:
            return "Carteira";

        case AccountType.DIGITAL_WALLET:
            return "Carteira Digital";

        case AccountType.OTHER:
            return "Outra";

        default:
            return props.account.accountType;

    }

});

</script>

<style scoped>

/* ==========================================================
   Table Row
========================================================== */

.table-row{

    transition:

        background .2s ease,

        transform .15s ease;

}

.table-row:hover{

    background:#f8fafc;

}

/* ==========================================================
   Cells
========================================================== */

td{

    padding:1rem 1.25rem;

    vertical-align:middle;

    border-bottom:1px solid #edf2f7;

    color:#334155;

    font-size:.95rem;

}

.text-right{

    text-align:right;

}

.text-center{

    text-align:center;

}

/* ==========================================================
   Account
========================================================== */

.account{

    display:flex;

    align-items:center;

    gap:1rem;

}

.account-icon{

    width:46px;

    height:46px;

    border-radius:14px;

    display:flex;

    align-items:center;

    justify-content:center;

    flex-shrink:0;

}

.account-content{

    display:flex;

    flex-direction:column;

    gap:.20rem;

}

.account-content strong{

    font-size:.96rem;

    color:#0f172a;

    font-weight:700;

}

.account-content small{

    color:#94a3b8;

    font-size:.75rem;

    font-family:monospace;

    word-break:break-all;

}

/* ==========================================================
   Balance
========================================================== */

.balance{

    font-weight:700;

    color:#0f172a;

    white-space:nowrap;

}

/* ==========================================================
   Account Type
========================================================== */

.type-badge{

    display:inline-flex;

    align-items:center;

    justify-content:center;

    padding:.35rem .75rem;

    border-radius:999px;

    background:#eff6ff;

    color:#2563eb;

    font-size:.78rem;

    font-weight:600;

    white-space:nowrap;

}

/* ==========================================================
   Flags
========================================================== */

.flag{

    display:inline-flex;

    align-items:center;

    justify-content:center;

    width:30px;

    height:30px;

    border-radius:999px;

    background:#fee2e2;

    color:#dc2626;

}

.flag.enabled{

    background:#dcfce7;

    color:#16a34a;

}

/* ==========================================================
   Status
========================================================== */

.status{

    display:inline-flex;

    align-items:center;

    justify-content:center;

    padding:.40rem .90rem;

    border-radius:999px;

    font-size:.80rem;

    font-weight:600;

    white-space:nowrap;

}

.status.active{

    background:#dcfce7;

    color:#15803d;

}

.status.inactive{

    background:#fee2e2;

    color:#b91c1c;

}

/* ==========================================================
   Actions
========================================================== */

.actions{

    display:flex;

    justify-content:center;

    align-items:center;

    gap:.35rem;

}

.actions :deep(button){

    width:36px;

    height:36px;

    padding:0;

    border-radius:10px;

}

.actions :deep(button:hover){

    transform:none;

    background:#eff6ff;

}

.actions :deep(button:first-child:hover){

    color:#2563eb;

}

.actions :deep(button:last-child:hover){

    color:#dc2626;

}

/* ==========================================================
   Responsive
========================================================== */

@media (max-width:1200px){

    td{

        padding:.9rem 1rem;

    }

    .account{

        gap:.85rem;

    }

    .account-icon{

        width:42px;

        height:42px;

    }

    .account-content strong{

        font-size:.92rem;

    }

    .balance{

        font-size:.92rem;

    }

}

@media (max-width:992px){

    td{

        padding:.85rem .9rem;

        font-size:.9rem;

    }

    .account{

        min-width:220px;

    }

    .account-content{

        min-width:140px;

    }

    .account-content small{

        max-width:160px;

        overflow:hidden;

        text-overflow:ellipsis;

        white-space:nowrap;

    }

    .actions{

        gap:.25rem;

    }

}

@media (max-width:768px){

    .account{

        gap:.75rem;

    }

    .account-icon{

        width:38px;

        height:38px;

        border-radius:12px;

    }

    .type-badge{

        font-size:.72rem;

        padding:.30rem .60rem;

    }

    .status{

        font-size:.72rem;

        padding:.35rem .70rem;

    }

    .flag{

        width:26px;

        height:26px;

    }

    .actions :deep(button){

        width:32px;

        height:32px;

    }

}

@media (max-width:576px){

    td{

        padding:.75rem;

    }

    .account-content strong{

        font-size:.88rem;

    }

    .balance{

        font-size:.88rem;

    }

}

/* ==========================================================
   Visual refinements
========================================================== */

.table-row:hover .account-content strong{

    color:#2563eb;

}

.table-row:hover .account-icon{

    transform:scale(1.05);

    transition:.2s ease;

}

.account-icon{

    transition:

        transform .2s ease,

        background-color .2s ease;

}

.balance{

    letter-spacing:.02em;

}

.type-badge,

.status,

.flag{

    user-select:none;

}

.actions{

    white-space:nowrap;

}

</style>