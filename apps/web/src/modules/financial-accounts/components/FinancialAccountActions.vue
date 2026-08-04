<template>

    <div class="financial-account-actions">

        <AppButton
            variant="ghost"
            size="sm"
            title="Visualizar detalhes"
            @click="emit('view', account)"
        >

            <AppIcon
                name="eye"
                :size="16"
            />

        </AppButton>

        <AppButton
            variant="ghost"
            size="sm"
            title="Editar conta"
            @click="emit('edit', account)"
        >

            <AppIcon
                name="edit"
                :size="16"
            />

        </AppButton>

        <AppButton
            variant="ghost"
            size="sm"
            title="Excluir conta"
            class="danger"
            @click="emit('delete', account)"
        >

            <AppIcon
                name="delete"
                :size="16"
            />

        </AppButton>

    </div>

</template>

<script setup lang="ts">

/**
 * ============================================================================
 * Financial Account Actions
 * ============================================================================
 *
 * Purpose
 * ============================================================================
 *
 * Renders the available actions for a Financial Account.
 *
 * This component centralizes every row action, allowing the table to remain
 * responsible only for rendering data.
 *
 * ============================================================================
 * Current Actions
 * ============================================================================
 *
 * • View
 *
 * • Edit
 *
 * • Delete
 *
 * ============================================================================
 * Future Evolution
 * ============================================================================
 *
 * This component was intentionally designed so it can later be replaced by
 * a dropdown/context menu without affecting the table implementation.
 *
 * Planned actions:
 *
 * • Duplicate
 *
 * • Activate / Deactivate
 *
 * • Archive
 *
 * • Adjust balance
 *
 * • Transfer
 *
 * • History
 */

import AppButton from "@/shared/components/AppButton.vue";
import AppIcon from "@/shared/components/AppIcon.vue";

import type {

    FinancialAccount,

} from "../types/financial-account";

defineProps<{

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

</script>

<style scoped>

/* ==========================================================================
   Container
========================================================================== */

.financial-account-actions{

    display:flex;

    align-items:center;

    justify-content:center;

    gap:.35rem;

    white-space:nowrap;

}

/* ==========================================================================
   Buttons
========================================================================== */

.financial-account-actions :deep(button){

    width:36px;

    height:36px;

    padding:0;

    border-radius:10px;

    transition:

        background-color .2s,

        color .2s,

        transform .2s;

}

.financial-account-actions :deep(button:hover){

    transform:none;

}

/* ==========================================================================
   View
========================================================================== */

.financial-account-actions :deep(button:nth-child(1):hover){

    background:#eff6ff;

    color:#2563eb;

}

/* ==========================================================================
   Edit
========================================================================== */

.financial-account-actions :deep(button:nth-child(2):hover){

    background:#eff6ff;

    color:#2563eb;

}

/* ==========================================================================
   Delete
========================================================================== */

.financial-account-actions :deep(button.danger:hover){

    background:#fee2e2;

    color:#dc2626;

}

/* ==========================================================================
   Responsive
========================================================================== */

@media (max-width:768px){

    .financial-account-actions{

        gap:.25rem;

    }

    .financial-account-actions :deep(button){

        width:32px;

        height:32px;

    }

}

</style>