/**
 * ============================================================================
 * Financial Account Service
 * ============================================================================
 *
 * Purpose
 * ============================================================================
 *
 * Implements the application services responsible for managing financial
 * accounts.
 *
 * Unlike the API layer, this service contains the business-oriented
 * operations consumed by the UI.
 *
 * It is responsible for orchestrating API calls and performing any
 * client-side transformations required by the presentation layer.
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
 * • List financial accounts.
 *
 * • Retrieve one account.
 *
 * • Create financial accounts.
 *
 * • Update financial accounts.
 *
 * • Hide infrastructure details from higher layers.
 *
 * ============================================================================
 * Design Principles
 * ============================================================================
 *
 * • Stateless.
 *
 * • No UI logic.
 *
 * • No HTTP implementation details.
 *
 * • Easy to mock during testing.
 */

import { financialAccountApi } from "../api/financial-account.api";

import type {
    CreateFinancialAccountRequest,
    FinancialAccount,
    UpdateFinancialAccountRequest,
} from "../types/financial-account";

class FinancialAccountService {

    /**
     * Retrieves every financial account belonging to the authenticated user.
     */
    async list(): Promise<FinancialAccount[]> {

        const accounts =
            await financialAccountApi.list();

        return accounts.sort(
            (a, b) => a.name.localeCompare(b.name),
        );

    }

    /**
     * Retrieves a financial account.
     */
    async get(
        id: string,
    ): Promise<FinancialAccount> {

        return financialAccountApi.get(
            id,
        );

    }

    /**
     * Creates a new financial account.
     */
    async create(
        request: CreateFinancialAccountRequest,
    ): Promise<FinancialAccount> {

        return financialAccountApi.create(
            request,
        );

    }

    /**
     * Updates an existing financial account.
     */
    async update(
        id: string,
        request: UpdateFinancialAccountRequest,
    ): Promise<FinancialAccount> {

        return financialAccountApi.update(
            id,
            request,
        );

    }

}

export const financialAccountService =
    new FinancialAccountService();