/**
 * ============================================================================
 * useFinancialAccounts
 * ============================================================================
 *
 * Centraliza toda a lógica do módulo de Contas Financeiras.
 */

import { computed, ref } from "vue";

import { financialAccountService } from "../services/financial-account.service";

import type {
    CreateFinancialAccountRequest,
    FinancialAccount,
    UpdateFinancialAccountRequest,
} from "../types/financial-account";

export function useFinancialAccounts() {

    const accounts =
        ref<FinancialAccount[]>([]);

    const loading =
        ref(false);

    const saving =
        ref(false);

    const error =
        ref<string | null>(null);

    const totalBalance = computed(() =>

        accounts.value.reduce(

            (sum, account) =>

                sum + account.currentBalance,

            0,

        ),

    );

    const accountCount = computed(() =>

        accounts.value.length,

    );

    async function load() {

        loading.value = true;

        error.value = null;

        try {

            accounts.value =
                await financialAccountService.list();

        }

        catch (err) {

            console.error(err);

            error.value =
                "Não foi possível carregar as contas.";

        }

        finally {

            loading.value = false;

        }

    }

    async function create(
        request: CreateFinancialAccountRequest,
    ) {

        saving.value = true;

        error.value = null;

        try {

            const account =
                await financialAccountService.create(
                    request,
                );

            accounts.value.push(
                account,
            );

            sort();

            return account;

        }

        catch (err) {

            console.error(err);

            error.value =
                "Não foi possível criar a conta.";

            throw err;

        }

        finally {

            saving.value = false;

        }

    }

    async function update(
        id: string,
        request: UpdateFinancialAccountRequest,
    ) {

        saving.value = true;

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

                accounts.value[index] =
                    updated;

            }

            sort();

            return updated;

        }

        catch (err) {

            console.error(err);

            error.value =
                "Não foi possível atualizar a conta.";

            throw err;

        }

        finally {

            saving.value = false;

        }

    }

    function findById(
        id: string,
    ) {

        return accounts.value.find(

            account => account.id === id,

        );

    }

    function sort() {

        accounts.value.sort(

            (a, b) =>

                a.name.localeCompare(
                    b.name,
                ),

        );

    }

    function clearError() {

        error.value = null;

    }

    return {

        accounts,

        loading,

        saving,

        error,

        accountCount,

        totalBalance,

        load,

        create,

        update,

        findById,

        clearError,

    };

}