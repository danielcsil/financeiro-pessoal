/**
 * ============================================================================
 * Financial Account API
 * ============================================================================
 *
 * Purpose
 * ============================================================================
 *
 * Encapsulates every HTTP request related to Financial Accounts.
 *
 * This module is the only component that knows how to communicate with the
 * REST API. Higher layers (Services, Composables and Views) remain completely
 * independent from Axios, endpoint URLs and HTTP details.
 *
 * ============================================================================
 * Architecture
 * ============================================================================
 *
 * View
 *      │
 *      ▼
 * Composable
 *      │
 *      ▼
 * Service
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
 * • Execute HTTP requests.
 *
 * • Serialize request payloads.
 *
 * • Deserialize HTTP responses.
 *
 * • Hide endpoint definitions.
 *
 * • Never implement business rules.
 *
 * ============================================================================
 * Design Principles
 * ============================================================================
 *
 * • Single Responsibility.
 *
 * • Stateless.
 *
 * • Infrastructure only.
 *
 * • Framework isolated.
 *
 * • Easy to mock during testing.
 */

import type { AxiosResponse } from "axios";

import http from "@/shared/http/http-client";

import type {
    CreateFinancialAccountRequest,
    FinancialAccount,
    UpdateFinancialAccountRequest,
} from "../types/financial-account";

class FinancialAccountApi {

    /**
     * Base endpoint for Financial Accounts.
     */
    private static readonly BASE_URL =
        "/financial-accounts";

    /**
     * Builds the endpoint URL for a specific account.
     */
    private buildUrl(
        id: string,
    ): string {

        return `${FinancialAccountApi.BASE_URL}/${id}`;

    }

    /**
     * Retrieves every financial account belonging to the authenticated user.
     */
    async list(): Promise<FinancialAccount[]> {

        const response: AxiosResponse<
            FinancialAccount[]
        > = await http.get(
            FinancialAccountApi.BASE_URL,
        );

        return response.data;

    }

    /**
     * Retrieves a single financial account.
     */
    async get(
        id: string,
    ): Promise<FinancialAccount> {

        const response: AxiosResponse<
            FinancialAccount
        > = await http.get(
            this.buildUrl(id),
        );

        return response.data;

    }

    /**
     * Creates a new financial account.
     */
    async create(
        request: CreateFinancialAccountRequest,
    ): Promise<FinancialAccount> {

        const response: AxiosResponse<
            FinancialAccount
        > = await http.post(
            FinancialAccountApi.BASE_URL,
            request,
        );

        return response.data;

    }

    /**
     * Updates an existing financial account.
     */
    async update(
        id: string,
        request: UpdateFinancialAccountRequest,
    ): Promise<FinancialAccount> {

        const response: AxiosResponse<
            FinancialAccount
        > = await http.put(
            this.buildUrl(id),
            request,
        );

        return response.data;

    }

    /**
     * Removes a financial account.
     *
     * This operation is intentionally left commented until the backend
     * exposes the corresponding endpoint.
     *
     * Example:
     *
     * async remove(id: string): Promise<void> {
     *     await http.delete(this.buildUrl(id));
     * }
     */

}

export const financialAccountApi =
    new FinancialAccountApi();