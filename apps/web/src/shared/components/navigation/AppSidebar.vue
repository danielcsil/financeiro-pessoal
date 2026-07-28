<script setup lang="ts">
import { computed } from "vue";
import { RouterLink, useRoute } from "vue-router";

import { useAuthStore } from "@/modules/auth/stores/auth.store";

interface NavigationItem {
  label: string;
  to: string;
  icon: string;
}

const route = useRoute();
const auth = useAuthStore();

const menu: NavigationItem[] = [
  {
    label: "Dashboard",
    to: "/dashboard",
    icon: "🏠",
  },
  {
    label: "Contas",
    to: "/accounts",
    icon: "🏦",
  },
  {
    label: "Receitas",
    to: "/income",
    icon: "💰",
  },
  {
    label: "Despesas",
    to: "/expenses",
    icon: "💳",
  },
  {
    label: "Cartões",
    to: "/cards",
    icon: "💳",
  },
  {
    label: "Fluxo de Caixa",
    to: "/cash-flow",
    icon: "📈",
  },
  {
    label: "Metas",
    to: "/goals",
    icon: "🎯",
  },
  {
    label: "Relatórios",
    to: "/reports",
    icon: "📊",
  },
  {
    label: "Assistente IA",
    to: "/advisor",
    icon: "🤖",
  },
  {
    label: "Configurações",
    to: "/settings",
    icon: "⚙️",
  },
];

const currentPath = computed(() => route.path);

const user = computed(() => auth.user);

function isActive(path: string) {
  return currentPath.value.startsWith(path);
}
</script>

<template>
  <aside class="sidebar">
    <div class="sidebar__header">
      <h2>Personal Finance</h2>
    </div>

    <nav class="sidebar__menu">
      <RouterLink
        v-for="item in menu"
        :key="item.to"
        :to="item.to"
        class="sidebar__item"
        :class="{ active: isActive(item.to) }"
      >
        <span class="sidebar__icon">
          {{ item.icon }}
        </span>

        <span class="sidebar__label">
          {{ item.label }}
        </span>
      </RouterLink>
    </nav>

    <footer class="sidebar__footer">
      <div class="sidebar__user">
        <strong>{{ user?.name ?? "Usuário" }}</strong>

        <small>
          {{ user?.email ?? "" }}
        </small>
      </div>
    </footer>
  </aside>
</template>

<style scoped>
.sidebar {
  display: flex;
  flex-direction: column;

  width: 280px;
  height: 100vh;

  background: var(--color-surface);
  border-right: 1px solid var(--color-border);

  position: sticky;
  top: 0;
}

.sidebar__header {
  padding: 1.5rem;
  border-bottom: 1px solid var(--color-border);
}

.sidebar__header h2 {
  color: var(--color-primary);
  font-size: 1.25rem;
}

.sidebar__menu {
  flex: 1;

  display: flex;
  flex-direction: column;

  padding: 1rem;
  gap: 0.35rem;

  overflow-y: auto;
}

.sidebar__item {
  display: flex;
  align-items: center;

  gap: 0.9rem;

  padding: 0.85rem 1rem;

  border-radius: 0.75rem;

  color: var(--color-text);

  text-decoration: none;

  transition: 0.2s;
}

.sidebar__item:hover {
  background: var(--color-surface-hover);
}

.sidebar__item.active {
  background: var(--color-primary);
  color: white;
}

.sidebar__icon {
  width: 24px;
  text-align: center;
}

.sidebar__label {
  flex: 1;
}

.sidebar__footer {
  border-top: 1px solid var(--color-border);
  padding: 1.25rem;
}

.sidebar__user {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.sidebar__user strong {
  color: var(--color-text);
  font-size: 0.95rem;
}

.sidebar__user small {
  color: var(--color-text-secondary);
  word-break: break-word;
}

@media (max-width: 1024px) {
  .sidebar {
    display: none;
  }
}
</style>