/**
 * ============================================================================
 * useFinancialAccounts
 * ============================================================================
 *
 * Purpose
 * ============================================================================
 *
 * Provides the reactive state and operations required by the Financial
 * Accounts module.
 *
 * This composable encapsulates every interaction between the UI and the
 * application service, exposing a simple API for Vue components.
 *
 * Views and components should never communicate directly with services.
 * Instead, they consume this composable.
 *
 * ============================================================================
 * Architecture
 * ============================================================================
 *
 * View
 *      │
 *      ▼
 * useFinancialAccounts
 *      │
 *      ▼
 * FinancialAccountService
 *      │
 *      ▼
 * FinancialAccountApi
 *      │
 *      ▼
 * REST API
 *
 * ============================================================================
 * Responsibilities
 * ============================================================================
 *
 * • Load accounts.
 *
 * • Create accounts.
 *
 * • Update accounts.
 *
 * • Maintain reactive state.
 *
 * • Expose loading indicators.
 *
 * • Expose error information.
 *
 * ============================================================================
 * Design Principles
 * ============================================================================
 *
 * • Reactive.
 *
 * • Stateless business logic.
 *
 * • UI independent.
 *
 * • Reusable across multiple views.
 */

import { computed, ref } from "vue";

import { financialAccountService } from "../services/financial-account.service";

import type {
    CreateFinancialAccountRequest,
    FinancialAccount,
    UpdateFinancialAccountRequest,
} from "../types/financial-account";

const accounts = ref<FinancialAccount[]>([]);

const loading = ref(false);

const error = ref<string | null>(null);

async function loadAccounts(): Promise<void> {

    loading.value = true;

    error.value = null;

    try {

        accounts.value =
            await financialAccountService.list();

    } catch (err) {

        error.value =
            err instanceof Error
                ? err.message
                : "Unable to load financial accounts.";

    } finally {

        loading.value = false;

    }

}

async function createAccount(
    request: CreateFinancialAccountRequest,
): Promise<void> {

    loading.value = true;

    error.value = null;

    try {

        const account =
            await financialAccountService.create(
                request,
            );

        accounts.value.push(
            account,
        );

        accounts.value.sort(
            (a, b) => a.name.localeCompare(
                b.name,
            ),
        );

    } catch (err) {

        error.value =
            err instanceof Error
                ? err.message
                : "Unable to create financial account.";

        throw err;

    } finally {

        loading.value = false;

    }

}

async function updateAccount(
    id: string,
    request: UpdateFinancialAccountRequest,
): Promise<void> {

    loading.value = true;

    error.value = null;

    try {

        const updated =
            await financialAccountService.update(
                id,
                request,
            );

        const index =
            accounts.value.findIndex(
                account => account.id === id,
            );

        if (index >= 0) {

            accounts.value[index] = updated;

            accounts.value.sort(
                (a, b) => a.name.localeCompare(
                    b.name,
                ),
            );

        }

    } catch (err) {

        error.value =
            err instanceof Error
                ? err.message
                : "Unable to update financial account.";

        throw err;

    } finally {

        loading.value = false;

    }

}

const totalAccounts = computed(
    () => accounts.value.length,
);

const totalBalance = computed(
    () =>
        accounts.value.reduce(
            (sum, account) =>
                sum + account.currentBalance,
            0,
        ),
);

export function useFinancialAccounts() {

    return {

        accounts,

        loading,

        error,

        totalAccounts,

        totalBalance,

        loadAccounts,

        createAccount,

        updateAccount,

    };

}