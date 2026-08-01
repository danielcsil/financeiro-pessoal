/**
 * ============================================================================
 * Financial Accounts Routes
 * ============================================================================
 *
 * Purpose
 * ============================================================================
 *
 * Declares every route belonging to the Financial Accounts module.
 *
 * Keeping module routes isolated makes the application easier to maintain
 * as new financial modules are introduced.
 *
 * ============================================================================
 * Architecture
 * ============================================================================
 *
 * App Router
 *      │
 *      ▼
 * Module Router
 *      │
 *      ▼
 * FinancialAccountsView
 */

import type { RouteRecordRaw } from "vue-router";

const routes: RouteRecordRaw[] = [
    {
        path: "accounts",

        name: "financial-accounts",

        component: () =>
            import("../views/FinancialAccountsView.vue"),

        meta: {
            requiresAuth: true,
            title: "Financial Accounts",
        },
    },
];

export default routes;