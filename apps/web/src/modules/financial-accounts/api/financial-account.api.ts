/**
 * ============================================================================
 * Financial Account API
 * ============================================================================
 *
 * Encapsulates every HTTP request related to Financial Accounts.
 */

import type { AxiosResponse } from "axios";

import http from "@/shared/http/http-client";

import type {
    CreateFinancialAccountRequest,
    FinancialAccount,
    UpdateFinancialAccountRequest,
} from "../types/financial-account";

export interface ListFinancialAccountsResponse {

    items: FinancialAccount[];

    total: number;

}

/**
 * Backend representation (snake_case).
 */
interface FinancialAccountResponse {

    id: string;

    user_id: string;

    name: string;

    institution: string | null;

    account_type: string;

    initial_balance: number;

    current_balance: number;

    color: string;

    icon: string;

    include_in_cash_flow: boolean;

    include_in_net_worth: boolean;

    active: boolean;

    created_at: string;

    updated_at: string;

}

interface BackendListFinancialAccountsResponse {

    items: FinancialAccountResponse[];

    total: number;

}

class FinancialAccountApi {

    private static readonly BASE_URL =
        "/financial-accounts";

    private buildUrl(
        id: string,
    ): string {

        return `${FinancialAccountApi.BASE_URL}/${id}`;

    }

    /**
     * Converts backend JSON (snake_case)
     * into frontend model (camelCase).
     */
    private toFinancialAccount(
        account: FinancialAccountResponse,
    ): FinancialAccount {

        return {

            id: account.id,

            userId: account.user_id,

            name: account.name,

            institution: account.institution,

            accountType: account.account_type as FinancialAccount["accountType"],

            initialBalance: account.initial_balance,

            currentBalance: account.current_balance,

            color: account.color,

            icon: account.icon,

            includeInCashFlow:
                account.include_in_cash_flow,

            includeInNetWorth:
                account.include_in_net_worth,

            active: account.active,

            createdAt: account.created_at,

            updatedAt: account.updated_at,

        };

    }

    /**
     * Converts frontend model into backend payload.
     */
    private toCreatePayload(
        request: CreateFinancialAccountRequest,
    ) {

        return {

            name: request.name,

            institution: request.institution,

            account_type: request.accountType.toLowerCase(),

            initial_balance: request.initialBalance,

            color: request.color,

            icon: request.icon,

            include_in_cash_flow:
                request.includeInCashFlow,

            include_in_net_worth:
                request.includeInNetWorth,

        };

    }

    /**
     * Converts frontend model into backend payload.
     */
    private toUpdatePayload(
        request: UpdateFinancialAccountRequest,
    ) {

        return {

            name: request.name,

            institution: request.institution,

            account_type: request.accountType,

            color: request.color,

            icon: request.icon,

            include_in_cash_flow:
                request.includeInCashFlow,

            include_in_net_worth:
                request.includeInNetWorth,

        };

    }

    /**
     * Lists every financial account.
     */
    async list(): Promise<ListFinancialAccountsResponse> {

        const response: AxiosResponse<
            BackendListFinancialAccountsResponse
        > = await http.get(
            FinancialAccountApi.BASE_URL,
        );

        return {

            items: response.data.items.map(

                account => this.toFinancialAccount(
                    account,
                ),

            ),

            total: response.data.total,

        };

    }

    /**
     * Retrieves one financial account.
     */
    async get(
        id: string,
    ): Promise<FinancialAccount> {

        const response: AxiosResponse<
            FinancialAccountResponse
        > = await http.get(
            this.buildUrl(id),
        );

        return this.toFinancialAccount(
            response.data,
        );

    }

    /**
     * Creates a financial account.
     */
    async create(
        request: CreateFinancialAccountRequest,
    ): Promise<FinancialAccount> {

        const response: AxiosResponse<
            FinancialAccountResponse
        > = await http.post(

            FinancialAccountApi.BASE_URL,

            this.toCreatePayload(
                request,
            ),

        );

        return this.toFinancialAccount(
            response.data,
        );

    }

    /**
     * Updates a financial account.
     */
    async update(
        id: string,
        request: UpdateFinancialAccountRequest,
    ): Promise<FinancialAccount> {

        const response: AxiosResponse<
            FinancialAccountResponse
        > = await http.put(

            this.buildUrl(id),

            this.toUpdatePayload(
                request,
            ),

        );

        return this.toFinancialAccount(
            response.data,
        );

    }

}

export const financialAccountApi =
    new FinancialAccountApi();