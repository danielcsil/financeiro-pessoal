import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import RegisterView from "@/views/auth/RegisterView.vue";
import LoginView from "@/views/auth/LoginView.vue";

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