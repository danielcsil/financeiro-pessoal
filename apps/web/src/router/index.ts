import { createRouter, createWebHistory, type RouteRecordRaw } from "vue-router";

import RegisterView from "@/views/auth/RegisterView.vue";
import LoginView from "@/views/auth/LoginView.vue";

import {
  PublicLayout,
  AuthLayout,
  DashboardLayout,
} from "@/shared/layouts";

import { authGuard } from "./guards/auth.guard";

/**
 * Definição das rotas da aplicação.
 *
 * A aplicação utiliza Layouts para separar as áreas:
 * - PublicLayout: páginas públicas
 * - AuthLayout: autenticação
 * - DashboardLayout: área autenticada
 */
const routes: RouteRecordRaw[] = [
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
        component: () => import("@/views/auth/ForgotPasswordView.vue"),
      },
    ],
  },

  {
    path: "/dashboard",

    /**
     * Todas as rotas filhas deste layout exigem autenticação.
     */
    meta: {
      requiresAuth: true,
    },

    component: DashboardLayout,

    children: [
      {
        path: "",
        name: "dashboard",
        component: () => import("@/views/dashboard/DashboardView.vue"),
      },
    ],
  },

  /**
   * Redireciona qualquer rota inexistente para a Home.
   */
  {
    path: "/:pathMatch(.*)*",
    redirect: "/",
  },
];

/**
 * Instância principal do Vue Router.
 */
const router = createRouter({
  history: createWebHistory(),
  routes,
});

/**
 * Guard global responsável por:
 * - restaurar a sessão;
 * - proteger rotas privadas;
 * - redirecionar usuários não autenticados.
 */
router.beforeEach(authGuard);

export default router;