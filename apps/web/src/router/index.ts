import {
  createRouter,
  createWebHistory,
  type RouteRecordRaw,
} from "vue-router";

import LoginView from "@/views/auth/LoginView.vue";
import RegisterView from "@/views/auth/RegisterView.vue";

import {
  AuthLayout,
  DashboardLayout,
  PublicLayout,
} from "@/shared/layouts";

import financialAccountRoutes from "@/modules/financial-accounts/router";

import { authGuard } from "./guards/auth.guard";

/**
 * ============================================================================
 * Application Router
 * ============================================================================
 *
 * The application is divided into three logical areas:
 *
 * • Public
 * • Authentication
 * • Authenticated Dashboard
 *
 * Each business module contributes its own routes, keeping the router modular
 * and easy to evolve.
 */

const routes: RouteRecordRaw[] = [
  // ==========================================================================
  // Public Area
  // ==========================================================================

  {
    path: "/",
    component: PublicLayout,

    children: [
      {
        path: "",
        name: "home",
        component: () => import("@/views/public/HomeView.vue"),
      },
    ],
  },

  // ==========================================================================
  // Authentication
  // ==========================================================================

  {
    path: "/",
    component: AuthLayout,

    children: [
      {
        path: "/login",
        name: "login",
        component: LoginView,
      },

      {
        path: "/register",
        name: "register",
        component: RegisterView,
      },

      {
        path: "forgot-password",
        name: "forgot-password",
        component: () =>
          import("@/views/auth/ForgotPasswordView.vue"),
      },
    ],
  },

  // ==========================================================================
  // Dashboard
  // ==========================================================================

  {
    path: "/dashboard",

    component: DashboardLayout,

    meta: {
      requiresAuth: true,
    },

    children: [
      {
        path: "",

        name: "dashboard",

        component: () =>
          import("@/views/dashboard/DashboardView.vue"),
      },

      // ----------------------------------------------------------------------
      // Financial Accounts Module
      // ----------------------------------------------------------------------

      ...financialAccountRoutes,
    ],
  },

  // ==========================================================================
  // Fallback
  // ==========================================================================

  {
    path: "/:pathMatch(.*)*",
    redirect: "/",
  },
];

/**
 * Main router instance.
 */
const router = createRouter({
  history: createWebHistory(),
  routes,
});

/**
 * Global navigation guard.
 *
 * Responsible for:
 *
 * • Restoring authenticated sessions.
 * • Protecting private routes.
 * • Redirecting anonymous users.
 */
router.beforeEach(authGuard);

export default router;