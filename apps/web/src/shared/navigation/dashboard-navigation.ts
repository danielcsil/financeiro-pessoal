/**
 * ============================================================================
 * Dashboard Navigation
 * ============================================================================
 *
 * Purpose
 * ============================================================================
 *
 * Defines the navigation structure displayed inside the authenticated area
 * of the application.
 *
 * Every business module contributes one or more navigation entries,
 * allowing the dashboard menu to remain centralized and consistent.
 *
 * ============================================================================
 * Design Principles
 * ============================================================================
 *
 * • Single source of truth for dashboard navigation.
 *
 * • Independent from Vue components.
 *
 * • Easy to extend as new modules are introduced.
 */

export interface NavigationItem {

    /**
     * Route name registered in Vue Router.
     */
    route: string;

    /**
     * Text displayed to the user.
     */
    label: string;

    /**
     * Icon identifier.
     *
     * The current implementation uses icon names.
     * Future versions may migrate to HeroIcons, Lucide or FontAwesome.
     */
    icon: string;

    /**
     * Determines whether the item should appear in the menu.
     */
    enabled: boolean;

}

export const dashboardNavigation: NavigationItem[] = [

    {
        route: "dashboard",
        label: "Dashboard",
        icon: "layout-dashboard",
        enabled: true,
    },

    {
        route: "financial-accounts",
        label: "Financial Accounts",
        icon: "wallet",
        enabled: true,
    },

    {
        route: "transactions",
        label: "Transactions",
        icon: "receipt",
        enabled: false,
    },

    {
        route: "credit-cards",
        label: "Credit Cards",
        icon: "credit-card",
        enabled: false,
    },

    {
        route: "financial-goals",
        label: "Goals",
        icon: "target",
        enabled: false,
    },

    {
        route: "investments",
        label: "Investments",
        icon: "chart-line",
        enabled: false,
    },

    {
        route: "reports",
        label: "Reports",
        icon: "bar-chart",
        enabled: false,
    },

    {
        route: "advisor",
        label: "AI Advisor",
        icon: "sparkles",
        enabled: false,
    },

];