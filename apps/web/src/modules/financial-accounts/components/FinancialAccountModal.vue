<template>

    <AppModal
        v-model="visible"
        title="Nova Conta Financeira"
        subtitle="Cadastre uma conta para controlar seu patrimônio, fluxo de caixa e investimentos."
    >

        <FinancialAccountForm
            :loading="loading"
            @submit="submit"
            @cancel="close"
        />

    </AppModal>

</template>

<script setup lang="ts">

/**
 * ============================================================================
 * Financial Account Modal
 * ============================================================================
 *
 * Purpose
 * ============================================================================
 *
 * Displays the modal used to create a new Financial Account.
 *
 * This component is intentionally lightweight and delegates all business
 * operations to its parent.
 *
 * Responsibilities
 * ----------------------------------------------------------------------------
 *
 * • Control modal visibility.
 *
 * • Render the FinancialAccountForm.
 *
 * • Emit save requests.
 *
 * • Emit visibility changes.
 *
 * This component contains no business rules.
 */

import { computed } from "vue";

import AppModal
from "@/shared/components/AppModal.vue";

import FinancialAccountForm
from "./FinancialAccountForm.vue";

import type {

    CreateFinancialAccountRequest,

} from "../types/financial-account";

/* ==========================================================================
   Props
========================================================================== */

const props = withDefaults(

    defineProps<{

        modelValue: boolean;

        loading?: boolean;

    }>(),

    {

        loading: false,

    },

);

/* ==========================================================================
   Emits
========================================================================== */

const emit = defineEmits<{

    (

        event: "update:modelValue",

        value: boolean,

    ): void;

    (

        event: "save",

        request: CreateFinancialAccountRequest,

    ): void;

}>();

/* ==========================================================================
   Computed
========================================================================== */

const visible = computed({

    get(): boolean {

        return props.modelValue;

    },

    set(

        value: boolean,

    ): void {

        emit(

            "update:modelValue",

            value,

        );

    },

});

/* ==========================================================================
   Actions
========================================================================== */

function close(): void {

    visible.value = false;

}

function submit(

    request: CreateFinancialAccountRequest,

): void {

    emit(

        "save",

        request,

    );

}

</script>