<script setup lang="ts">
/**
 * =============================================================================
 * Financial Account Form
 * =============================================================================
 *
 * Purpose
 * =============================================================================
 *
 * Reusable form responsible for creating and editing financial accounts.
 *
 * This component is intentionally presentation-oriented and delegates every
 * persistence operation to its parent component.
 *
 * Responsibilities
 * ----------------
 *
 * • Display financial account fields.
 *
 * • Populate the form during edition.
 *
 * • Reset the form during creation.
 *
 * • Validate basic required fields.
 *
 * • Emit submit and cancel events.
 *
 * No HTTP requests or business rules belong here.
 */

import { computed, reactive, watch } from "vue";

import {
    BaseButton,
    BaseInput,
} from "@/shared/components/base";

import BaseCheckbox from "@/shared/components/base/BaseCheckbox.vue";

import BaseSelect from "@/shared/components/base/BaseSelect.vue";

import {
    AccountType,
    type CreateFinancialAccountRequest,
    type FinancialAccount,
} from "../types/financial-account";

interface Props {

    /**
     * Existing account when editing.
     */
    account?: FinancialAccount;

    /**
     * Indicates whether the form is currently submitting.
     */
    submitting?: boolean;

}

const props = withDefaults(
    defineProps<Props>(),
    {
        submitting: false,
    },
);

const emit = defineEmits<{

    submit: [request: CreateFinancialAccountRequest];

    cancel: [];

}>();

const defaultForm = (): CreateFinancialAccountRequest => ({
    name: "",
    institution: null,
    accountType: AccountType.CHECKING,
    initialBalance: 0,
    color: "#2563EB",
    icon: "wallet",
    includeInCashFlow: true,
    includeInNetWorth: true,
});

const form = reactive<CreateFinancialAccountRequest>(
    defaultForm(),
);

const institutionValue = computed<string>({
    get: () => form.institution ?? "",
    set: value => {
        form.institution = value.trim() === ""
            ? null
            : value;
    },
});

const accountTypeValue = computed<string>({
    get: () => form.accountType,
    set: value => {
        form.accountType = value as AccountType;
    },
});

const initialBalanceValue = computed<string>({
    get: () => String(form.initialBalance),
    set: value => {
        const parsed = Number(value);

        form.initialBalance = Number.isFinite(parsed)
            ? parsed
            : 0;
    },
});

/**
 * Synchronizes the form with the selected account.
 */
watch(
    () => props.account,
    account => {

        if (!account) {

            Object.assign(
                form,
                defaultForm(),
            );

            return;

        }

        Object.assign(
            form,
            {
                name: account.name,
                institution: account.institution,
                accountType: account.accountType,
                initialBalance: account.initialBalance,
                color: account.color,
                icon: account.icon,
                includeInCashFlow:
                    account.includeInCashFlow,
                includeInNetWorth:
                    account.includeInNetWorth,
            },
        );

    },
    {
        immediate: true,
    },
);

const accountTypes = computed(() => [

    {
        value: AccountType.CHECKING,
        label: "Checking Account",
    },

    {
        value: AccountType.SAVINGS,
        label: "Savings Account",
    },

    {
        value: AccountType.INVESTMENT,
        label: "Investment Account",
    },

    {
        value: AccountType.CASH,
        label: "Cash",
    },

    {
        value: AccountType.DIGITAL_WALLET,
        label: "Digital Wallet",
    },

    {
        value: AccountType.OTHER,
        label: "Other",
    },

]);

function onSubmit(): void {

    emit(
        "submit",
        {
            ...form,
        },
    );

}
</script>

<template>

<form
    class="financial-account-form"
    @submit.prevent="onSubmit"
>

    <div class="grid">

        <BaseInput
            id="name"
            v-model="form.name"
            label="Account Name"
            placeholder="Checking Account"
            required
        />

        <BaseInput
            id="institution"
            v-model="institutionValue"
            label="Institution"
            placeholder="Bank"
        />

        <BaseSelect
            id="account-type"
            v-model="accountTypeValue"
            label="Account Type"
            :options="accountTypes"
            required
        />

        <BaseInput
            id="initial-balance"
            v-model="initialBalanceValue"
            type="number"
            label="Initial Balance"
        />

        <BaseInput
            id="color"
            v-model="form.color"
            type="color"
            label="Color"
        />

        <BaseInput
            id="icon"
            v-model="form.icon"
            label="Icon"
            placeholder="wallet"
        />

    </div>

    <div class="checkboxes">

        <BaseCheckbox
            v-model="form.includeInCashFlow"
            label="Include in Cash Flow"
            description="This account participates in cash flow calculations."
        />

        <BaseCheckbox
            v-model="form.includeInNetWorth"
            label="Include in Net Worth"
            description="This account contributes to total net worth."
        />

    </div>

    <footer class="actions">

        <BaseButton
            variant="secondary"
            type="button"
            @click="emit('cancel')"
        >
            Cancel
        </BaseButton>

        <BaseButton
            type="submit"
            :loading="submitting"
        >
            {{
                account
                    ? "Save Changes"
                    : "Create Account"
            }}
        </BaseButton>

    </footer>

</form>

</template>

<style scoped>

.financial-account-form{

    display:flex;

    flex-direction:column;

    gap:2rem;

}

.grid{

    display:grid;

    grid-template-columns:repeat(auto-fit,minmax(260px,1fr));

    gap:1.5rem;

}

.checkboxes{

    display:flex;

    flex-direction:column;

    gap:1rem;

}

.actions{

    display:flex;

    justify-content:flex-end;

    gap:1rem;

    padding-top:1.5rem;

    border-top:1px solid var(--color-border);

}

@media (max-width:768px){

    .actions{

        flex-direction:column-reverse;

        align-items:stretch;

    }

}

</style>
