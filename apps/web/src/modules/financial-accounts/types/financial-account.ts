/**
 * ============================================================================
 * Financial Account Types
 * ============================================================================
 *
 * Purpose
 * ============================================================================
 *
 * Defines the TypeScript models shared by the Financial Accounts module.
 *
 * These interfaces represent the data exchanged between the frontend and the
 * REST API, serving as the single source of truth for the module.
 *
 * Keeping these types centralized avoids duplicated interfaces across
 * components, composables and services.
 *
 * ============================================================================
 * Architecture
 * ============================================================================
 *
 *                  REST API
 *                      │
 *                      ▼
 *             FinancialAccount
 *                      │
 *      ┌───────────────┼───────────────┐
 *      ▼               ▼               ▼
 *   Services      Composables     Components
 *
 * ============================================================================
 * Design Principles
 * ============================================================================
 *
 * • Shared across the entire module.
 *
 * • Immutable whenever possible.
 *
 * • Mirrors the REST API contract.
 *
 * • Contains no business logic.
 */

/**
 * Represents a financial account.
 */
export interface FinancialAccount {

    /**
     * Unique account identifier.
     */
    readonly id: string;

    /**
     * Account owner identifier.
     */
    readonly userId: string;

    /**
     * Account name.
     */
    name: string;

    /**
     * Financial institution.
     */
    institution: string | null;

    /**
     * Account type.
     */
    accountType: AccountType;

    /**
     * Initial account balance.
     */
    initialBalance: number;

    /**
     * Current account balance.
     */
    currentBalance: number;

    /**
     * Color used throughout the UI.
     */
    color: string;

    /**
     * Icon identifier.
     */
    icon: string;

    /**
     * Indicates whether the account participates in cash flow calculations.
     */
    includeInCashFlow: boolean;

    /**
     * Indicates whether the account contributes to the user's net worth.
     */
    includeInNetWorth: boolean;

    /**
     * Indicates whether the account is active.
     */
    active: boolean;

    /**
     * Account creation timestamp.
     */
    createdAt: string;

    /**
     * Last update timestamp.
     */
    updatedAt: string;

}

/**
 * Response returned by GET /financial-accounts.
 */
export interface ListFinancialAccountsResponse {

    /**
     * Financial accounts belonging to the authenticated user.
     */
    items: FinancialAccount[];

    /**
     * Total number of accounts.
     */
    total: number;

}

/**
 * Supported financial account types.
 *
 * This enum mirrors the values exposed by the backend.
 */
export enum AccountType {

    CHECKING = "CHECKING",

    SAVINGS = "SAVINGS",

    INVESTMENT = "INVESTMENT",

    CASH = "CASH",

    DIGITAL_WALLET = "DIGITAL_WALLET",

    OTHER = "OTHER",

}

/**
 * Payload used to create a new financial account.
 */
export interface CreateFinancialAccountRequest {

    name: string;

    institution: string;

    accountType: AccountType;

    initialBalance: number;

    color: string;

    icon: string;

    includeInCashFlow: boolean;

    includeInNetWorth: boolean;

}

/**
 * Payload used to update an existing financial account.
 */
export interface UpdateFinancialAccountRequest {

    name: string;

    institution: string;

    accountType: AccountType;

    color: string;

    icon: string;

    includeInCashFlow: boolean;

    includeInNetWorth: boolean;

}