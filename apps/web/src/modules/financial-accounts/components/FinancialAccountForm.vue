<template>

    <form
        class="account-form"
        @submit.prevent="submit"
    >

        <!-- ==========================================================
             General Information
        =========================================================== -->

        <FinancialAccountSection
            title="Informações Gerais"
            description="Defina as informações principais da conta financeira."
        >

            <div class="grid grid-2">

                <AppInput
                    v-model="form.name"
                    label="Nome da Conta"
                    placeholder="Ex.: Nubank"
                    required
                />

                <AppInput
                    v-model="form.institution"
                    label="Instituição"
                    placeholder="Ex.: Itaú, Nubank..."
                />

            </div>

            <AccountTypeSelector
                v-model="form.accountType"
            />

        </FinancialAccountSection>

        <FinancialAccountDivider />

        <!-- ==========================================================
             Appearance
        =========================================================== -->

        <FinancialAccountSection
            title="Aparência"
            description="Personalize a identificação visual da conta."
        >

            <div class="grid grid-2">

                <ColorPicker
                    v-model="form.color"
                />

                <IconPicker
                    v-model="form.icon"
                />

            </div>

        </FinancialAccountSection>

        <FinancialAccountDivider />

        <!-- ==========================================================
             Initial Balance
        =========================================================== -->

        <FinancialAccountSection
            title="Saldo Inicial"
            description="Informe o saldo disponível nesta conta."
        >

            <CurrencyInput
                v-model="form.initialBalance"
            />

        </FinancialAccountSection>

        <FinancialAccountDivider />

        <!-- ==========================================================
             Participation
        =========================================================== -->

        <FinancialAccountSection
            title="Participação"
            description="Escolha como esta conta participa dos cálculos do sistema."
        >

            <div class="switches">

                <AppSwitch
                    v-model="form.includeInCashFlow"
                    label="Fluxo de Caixa"
                    description="Inclui esta conta nos cálculos de fluxo de caixa."
                />

                <AppSwitch
                    v-model="form.includeInNetWorth"
                    label="Patrimônio"
                    description="Inclui esta conta no patrimônio líquido."
                />

            </div>

        </FinancialAccountSection>

        <!-- ==========================================================
             Footer
        =========================================================== -->

        <footer class="footer">

            <AppButton
                variant="secondary"
                type="button"
                @click="cancel"
            >

                Cancelar

            </AppButton>

            <AppButton
                type="submit"
                :loading="loading"
            >

                Criar Conta

            </AppButton>

        </footer>

    </form>

</template>

<script setup lang="ts">

/**
 * ============================================================================
 * Financial Account Form
 * ============================================================================
 *
 * Purpose
 * ============================================================================
 *
 * Form responsible for collecting the information required to create a
 * Financial Account.
 *
 * This component contains only presentation logic and validation.
 * Persistence is delegated to the parent component.
 */

import { reactive } from "vue";

import AppButton
from "@/shared/components/AppButton.vue";

import AppInput
from "@/shared/components/AppInput.vue";

import AppSwitch
from "@/shared/components/AppSwitch.vue";

import AccountTypeSelector
from "./AccountTypeSelector.vue";

import ColorPicker
from "./ColorPicker.vue";

import CurrencyInput
from "./CurrencyInput.vue";

import FinancialAccountDivider
from "./FinancialAccountDivider.vue";

import FinancialAccountSection
from "./FinancialAccountSection.vue";

import IconPicker
from "./IconPicker.vue";

import {

    AccountType,

} from "../types/financial-account";

import type {

    CreateFinancialAccountRequest,

} from "../types/financial-account";

const props = withDefaults(

    defineProps<{

        loading?: boolean;

    }>(),

    {

        loading: false,

    },

);

const emit = defineEmits<{

    (

        event: "submit",

        request: CreateFinancialAccountRequest,

    ): void;

    (

        event: "cancel",

    ): void;

}>();

const form = reactive<CreateFinancialAccountRequest>({

    name: "",

    institution: "",

    accountType: AccountType.CHECKING,

    initialBalance: 0,

    color: "#2563EB",

    icon: "wallet",

    includeInCashFlow: true,

    includeInNetWorth: true,

});

function submit(): void {

    if (

        form.name.trim() === ""

    ) {

        return;

    }

    emit(

        "submit",

        {

            ...form,

        },

    );

}

function cancel(): void {

    emit(

        "cancel",

    );

}

function resetForm(): void {

    form.name = "";

    form.institution = "";

    form.accountType =
        AccountType.CHECKING;

    form.initialBalance = 0;

    form.color = "#2563EB";

    form.icon = "wallet";

    form.includeInCashFlow = true;

    form.includeInNetWorth = true;

}

</script>

<style scoped>

/* ==========================================================================
   Form
========================================================================== */

.account-form{

    display:flex;

    flex-direction:column;

    gap:2rem;

    width:100%;

}

/* ==========================================================================
   Grid
========================================================================== */

.grid{

    display:grid;

    gap:1.5rem;

}

.grid-2{

    grid-template-columns:

        repeat(

            2,

            minmax(0,1fr)

        );

}

/* ==========================================================================
   Switches
========================================================================== */

.switches{

    display:flex;

    flex-direction:column;

    gap:1rem;

}

/* ==========================================================================
   Footer
========================================================================== */

.footer{

    display:flex;

    justify-content:flex-end;

    align-items:center;

    gap:1rem;

    margin-top:.5rem;

    padding-top:1.5rem;

    border-top:1px solid #e2e8f0;

}

/* ==========================================================================
   Buttons
========================================================================== */

.footer :deep(button){

    min-width:160px;

}

/* ==========================================================================
   Inputs
========================================================================== */

.account-form :deep(.app-input),

.account-form :deep(.app-select),

.account-form :deep(.currency-input){

    width:100%;

}

/* ==========================================================================
   Sections
========================================================================== */

.account-form :deep(.section){

    gap:1.75rem;

}

.account-form :deep(.section h3){

    color:#0f172a;

}

.account-form :deep(.section p){

    color:#64748b;

}

/* ==========================================================================
   Divider
========================================================================== */

.account-form :deep(hr){

    margin:0;

}

/* ==========================================================================
   Animations
========================================================================== */

.account-form>*{

    animation:

        fadeIn .20s ease;

}

@keyframes fadeIn{

    from{

        opacity:0;

        transform:translateY(4px);

    }

    to{

        opacity:1;

        transform:translateY(0);

    }

}

/* ==========================================================================
   Responsive
========================================================================== */

@media(max-width:992px){

    .grid-2{

        grid-template-columns:1fr;

    }

}

@media(max-width:768px){

    .account-form{

        gap:1.5rem;

    }

    .footer{

        flex-direction:column-reverse;

        align-items:stretch;

    }

    .footer :deep(button){

        width:100%;

    }

}

/* ==========================================================================
   Visual Refinements
========================================================================== */

.account-form{

    padding:.25rem 0;

}

.footer{

    position:sticky;

    bottom:0;

    background:white;

}

.footer::before{

    content:"";

    position:absolute;

    top:-1px;

    left:0;

    right:0;

}

.account-form :deep(.section){

    transition:.2s ease;

}

.account-form :deep(.section:hover){

    transform:translateY(-1px);

}

.account-form :deep(.app-switch){

    padding:.35rem 0;

}

/* ==========================================================================
   Focus
========================================================================== */

.account-form :deep(input:focus),

.account-form :deep(select:focus),

.account-form :deep(textarea:focus){

    transition:

        border-color .2s,

        box-shadow .2s;

}

/* ==========================================================================
   Accessibility
========================================================================== */

.account-form :deep(button:focus-visible),

.account-form :deep(input:focus-visible),

.account-form :deep(select:focus-visible){

    outline:none;

}

</style>