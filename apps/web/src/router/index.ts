import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

import {
  PublicLayout,
  AuthLayout,
  DashboardLayout,
} from "@/shared/layouts";

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
        path: "login",
        name: "login",
        component: () => import("@/views/auth/LoginView.vue"),
      },
      {
        path: "register",
        name: "register",
        component: () => import("@/views/auth/RegisterView.vue"),
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
    component: DashboardLayout,
    children: [
      {
        path: "",
        name: "dashboard",
        component: () => import("@/views/dashboard/DashboardView.vue"),
      },
    ],
  },

  {
    path: "/:pathMatch(.*)*",
    redirect: "/",
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;