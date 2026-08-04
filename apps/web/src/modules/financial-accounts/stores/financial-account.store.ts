/**
 * ============================================================================
 * Financial Account Store
 * ============================================================================
 *
 * Purpose
 * ============================================================================
 *
 * Centralizes the state and business orchestration of the Financial Accounts
 * module.
 *
 * The Store acts as the single source of truth for the UI, exposing both the
 * persisted data and the presentation state required by the views.
 *
 * Responsibilities
 * ============================================================================
 *
 * • Load financial accounts.
 *
 * • Create and update accounts.
 *
 * • Maintain UI state.
 *
 * • Manage filters.
 *
 * • Manage pagination.
 *
 * • Expose computed collections.
 *
 * This store intentionally contains no HTTP implementation details.
 */

import { defineStore } from "pinia";

import {

    computed,

    ref,

} from "vue";

import { financialAccountService }

    from "../services/financial-account.service";

import type {

    CreateFinancialAccountRequest,

    FinancialAccount,

    UpdateFinancialAccountRequest,

} from "../types/financial-account";

interface FinancialAccountFilters {

    search: string;

    institution: string;

    accountType: string;

    status: string;

}

export const useFinancialAccountStore = defineStore(

    "financial-accounts",

    () => {

        /* ===================================================================
           State
        =================================================================== */

        const accounts =
            ref<FinancialAccount[]>([]);

        const loading =
            ref(false);

        const saving =
            ref(false);

        const error =
            ref<string | null>(null);

        const selectedAccount =
            ref<FinancialAccount | null>(
                null,
            );

        /* ===================================================================
           Filters
        =================================================================== */

        const filters =
            ref<FinancialAccountFilters>({

                search: "",

                institution: "",

                accountType: "",

                status: "",

            });

        /* ===================================================================
           Pagination
        =================================================================== */

        const currentPage =
            ref(1);

        const pageSize =
            ref(10);

        /* ===================================================================
           Computed
        =================================================================== */

        const totalBalance = computed(() =>

            accounts.value.reduce(

                (

                    total,

                    account,

                ) =>

                    total +

                    account.currentBalance,

                0,

            ),

        );

        const activeAccounts = computed(() =>

            accounts.value.filter(

                account =>

                    account.active,

            ),

        );

        const accountCount = computed(() =>

            activeAccounts.value.length,

        );

        const filteredAccounts = computed(() => {

            return accounts.value.filter(

                account => {

                    const search =

                        filters.value.search

                            .trim()

                            .toLowerCase();

                    const matchesSearch =

                        search === "" ||

                        account.name

                            .toLowerCase()

                            .includes(search) ||

                        (

                            account.institution ?? ""

                        )

                            .toLowerCase()

                            .includes(search);

                    const matchesInstitution =

                        filters.value.institution === "" ||

                        (

                            account.institution ?? ""

                        ) ===

                        filters.value.institution;

                    const matchesType =

                        filters.value.accountType === "" ||

                        account.accountType ===

                        filters.value.accountType;

                    const matchesStatus =

                        filters.value.status === "" ||

                        (

                            filters.value.status === "ACTIVE"

                                ? account.active

                                : !account.active

                        );

                    return (

                        matchesSearch &&

                        matchesInstitution &&

                        matchesType &&

                        matchesStatus

                    );

                },

            );

        });

        const paginatedAccounts = computed(() => {

            const start =

                (

                    currentPage.value - 1

                ) *

                pageSize.value;

            return filteredAccounts.value.slice(

                start,

                start + pageSize.value,

            );

        });

        const totalPages = computed(() =>

            Math.max(

                1,

                Math.ceil(

                    filteredAccounts.value.length /

                    pageSize.value,

                ),

            ),

        );

        /* ===================================================================
           Load
        =================================================================== */

        async function load(): Promise<void> {

            loading.value = true;

            error.value = null;

            try {

                accounts.value =
                    await financialAccountService.list();

                sort();

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

        async function refresh(): Promise<void> {

            await load();

        }

        /* ===================================================================
           Create
        =================================================================== */

        async function create(

            request: CreateFinancialAccountRequest,

        ): Promise<FinancialAccount> {

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

        /* ===================================================================
           Update
        =================================================================== */

        async function update(

            id: string,

            request: UpdateFinancialAccountRequest,

        ): Promise<FinancialAccount> {

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

                        account =>

                            account.id === id,

                    );

                if (

                    index >= 0

                ) {

                    accounts.value[index] =

                        updated;

                }

                if (

                    selectedAccount.value?.id === id

                ) {

                    selectedAccount.value =

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

        /* ===================================================================
           State Management
        =================================================================== */

        function selectAccount(

            account: FinancialAccount,

        ): void {

            selectedAccount.value =

                account;

        }

        function clearSelection(): void {

            selectedAccount.value =

                null;

        }

        function setFilters(

            value: FinancialAccountFilters,

        ): void {

            filters.value = value;

            currentPage.value = 1;

        }

        function setCurrentPage(

            page: number,

        ): void {

            currentPage.value =

                Math.min(

                    Math.max(

                        1,

                        page,

                    ),

                    totalPages.value,

                );

        }

        function setPageSize(

            size: number,

        ): void {

            pageSize.value = size;

            currentPage.value = 1;

        }

        /* ===================================================================
           Collection
        =================================================================== */

        function remove(

            id: string,

        ): void {

            accounts.value =

                accounts.value.filter(

                    account =>

                        account.id !== id,

                );

        }

                function findById(

            id: string,

        ): FinancialAccount | undefined {

            return accounts.value.find(

                account =>

                    account.id === id,

            );

        }

        function clear(): void {

            accounts.value = [];

            error.value = null;

            selectedAccount.value = null;

            currentPage.value = 1;

            filters.value = {

                search: "",

                institution: "",

                accountType: "",

                status: "",

            };

        }

        function sort(): void {

            accounts.value.sort(

                (

                    a,

                    b,

                ) =>

                    a.name.localeCompare(

                        b.name,

                    ),

            );

        }

        /* ===================================================================
           Public API
        =================================================================== */

        return {

            /* State */

            accounts,

            loading,

            saving,

            error,

            selectedAccount,

            filters,

            currentPage,

            pageSize,

            /* Computed */

            activeAccounts,

            accountCount,

            totalBalance,

            filteredAccounts,

            paginatedAccounts,

            totalPages,

            /* Actions */

            load,

            refresh,

            create,

            update,

            remove,

            findById,

            selectAccount,

            clearSelection,

            setFilters,

            setCurrentPage,

            setPageSize,

            clear,

        };

    },

);