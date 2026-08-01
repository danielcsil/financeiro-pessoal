<template>
  <div class="dashboard-layout">
    <!-- ====================================================== -->
    <!-- Sidebar -->
    <!-- ====================================================== -->

    <aside class="sidebar">
      <!-- Logo -->

      <div class="sidebar__header">
        <RouterLink
          to="/dashboard"
          class="sidebar__brand"
        >
          <svg
            class="sidebar__logo"
            viewBox="0 0 32 32"
            xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true"
          >
            <path
              d="M4 28H28"
              stroke="currentColor"
              stroke-width="3"
              stroke-linecap="round"
            />

            <rect
              x="6"
              y="17"
              width="5"
              height="9"
              rx="1.5"
              fill="#60A5FA"
            />

            <rect
              x="13.5"
              y="10"
              width="5"
              height="16"
              rx="1.5"
              fill="#3B82F6"
            />

            <rect
              x="21"
              y="4"
              width="5"
              height="22"
              rx="1.5"
              fill="currentColor"
            />
          </svg>

          <div>
            <h1 class="sidebar__title">
              Personal Finance
            </h1>

            <span class="sidebar__subtitle">
              Gestão Financeira
            </span>
          </div>
        </RouterLink>
      </div>

      <!-- =================================================== -->
      <!-- Menu -->
      <!-- =================================================== -->

      <nav class="sidebar__menu">
        <div class="menu-group">
          <span class="menu-group__title">
            Geral
          </span>

          <RouterLink
            to="/dashboard"
            class="menu-item"
          >
            <span class="menu-item__icon">🏠</span>

            Dashboard
          </RouterLink>
        </div>

        <div class="menu-group">
          <span class="menu-group__title">
            Finanças
          </span>

          <RouterLink
            to="/accounts"
            class="menu-item"
          >
            <span class="menu-item__icon">🏦</span>

            Contas
          </RouterLink>

          <RouterLink
            to="/cards"
            class="menu-item"
          >
            <span class="menu-item__icon">💳</span>

            Cartões
          </RouterLink>

          <RouterLink
            to="/transactions"
            class="menu-item"
          >
            <span class="menu-item__icon">💸</span>

            Transações
          </RouterLink>
        </div>

        <div class="menu-group">
          <span class="menu-group__title">
            Planejamento
          </span>

          <RouterLink
            to="/planning"
            class="menu-item"
          >
            <span class="menu-item__icon">📈</span>

            Fluxo de Caixa
          </RouterLink>

          <RouterLink
            to="/goals"
            class="menu-item"
          >
            <span class="menu-item__icon">🎯</span>

            Metas
          </RouterLink>

          <RouterLink
            to="/reports"
            class="menu-item"
          >
            <span class="menu-item__icon">📊</span>

            Relatórios
          </RouterLink>
        </div>

        <div class="menu-group">
          <span class="menu-group__title">
            Ferramentas
          </span>

          <RouterLink
            to="/assistant"
            class="menu-item"
          >
            <span class="menu-item__icon">🤖</span>

            Assistente IA
          </RouterLink>

          <RouterLink
            to="/settings"
            class="menu-item"
          >
            <span class="menu-item__icon">⚙️</span>

            Configurações
          </RouterLink>
        </div>
      </nav>

      <!-- =================================================== -->
      <!-- Rodapé -->
      <!-- =================================================== -->

      <footer class="sidebar__footer">
        <span>Personal Finance</span>

        <small>Versão 1.0.0</small>
      </footer>
    </aside>

    <!-- ====================================================== -->
    <!-- Conteúdo -->
    <!-- ====================================================== -->

    <div class="content">
      <header class="topbar">
        <div class="topbar__left">
          <h2>
            Bem-vindo, {{ firstName }}
          </h2>

          <p>
            Organize suas finanças e acompanhe seus resultados.
          </p>
        </div>

        <div class="topbar__right">
          <div class="user-info">
            <div class="user-avatar">
              {{ initials }}
            </div>

            <div class="user-details">
              <strong>
                {{ auth.user?.name }}
              </strong>

              <small>
                {{ auth.user?.email }}
              </small>
            </div>
          </div>

          <button
            class="logout-button"
            @click="logout"
          >
            Sair
          </button>
        </div>
      </header>

      <main class="page">
        <RouterView />
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { useRouter } from "vue-router";

import { useAuthStore } from "@/modules/auth/stores/auth.store";

/**
 * ============================================================
 * Stores
 * ============================================================
 */

const auth = useAuthStore();
const router = useRouter();

/**
 * ============================================================
 * Computed
 * ============================================================
 */

/**
 * Primeiro nome do usuário.
 *
 * Exemplo:
 * "Daniel Cunha da Silva"
 *
 * retorna:
 *
 * "Daniel"
 */
const firstName = computed((): string => {
  const name = auth.user?.name;

  if (!name) {
    return "Usuário";
  }

  return name.split(" ")[0];
});

/**
 * Iniciais do usuário.
 *
 * Daniel Cunha da Silva
 * ->
 * DS
 */
const initials = computed((): string => {
  const name = auth.user?.name;

  if (!name) {
    return "U";
  }

  const parts = name
    .trim()
    .split(/\s+/)
    .filter(Boolean);

  if (parts.length === 1) {
    return parts[0].substring(0, 1).toUpperCase();
  }

  return (
    parts[0][0] +
    parts[parts.length - 1][0]
  ).toUpperCase();
});

/**
 * Data atual.
 *
 * Exemplo:
 *
 * sábado, 1 de agosto de 2026
 */
const currentDate = computed((): string => {
  return new Intl.DateTimeFormat("pt-BR", {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
  }).format(new Date());
});

/**
 * Saudação dinâmica.
 */
const greeting = computed((): string => {
  const hour = new Date().getHours();

  if (hour < 12) {
    return "Bom dia";
  }

  if (hour < 18) {
    return "Boa tarde";
  }

  return "Boa noite";
});

/**
 * Nome completo.
 */
const fullName = computed(() => auth.user?.name ?? "");

/**
 * Email.
 */
const email = computed(() => auth.user?.email ?? "");

/**
 * ============================================================
 * Actions
 * ============================================================
 */

/**
 * Logout da aplicação.
 */
async function logout(): Promise<void> {
  auth.logout();

  await router.push({
    name: "login",
  });
}
</script>

<style scoped>
.dashboard-layout {
  display: flex;
  min-height: 100vh;
  background: linear-gradient(
    180deg,
    #f8fafc 0%,
    #eef3f8 100%
  );
}

/* ==========================================================
   SIDEBAR
========================================================== */

.sidebar {
  width: 290px;
  background: linear-gradient(
    180deg,
    #0f4c81,
    #0b3d69
  );

  color: white;

  display: flex;
  flex-direction: column;

  box-shadow: 6px 0 18px rgba(0, 0, 0, 0.08);
}

.sidebar__header {
  padding: 28px 24px 20px;
}

.sidebar__brand {
  display: flex;
  align-items: center;
  gap: 16px;

  color: inherit;
  text-decoration: none;
}

.sidebar__logo {
  width: 46px;
  height: 46px;

  flex-shrink: 0;
}

.sidebar__title {
  margin: 0;

  font-size: 1.25rem;
  font-weight: 700;

  line-height: 1.2;
}

.sidebar__subtitle {
  display: block;

  margin-top: 4px;

  font-size: .82rem;

  color: rgba(255,255,255,.75);
}

.sidebar__menu {
  flex: 1;

  overflow-y: auto;

  padding: 0 18px 24px;
}

/* ==========================================================
   MENU GROUP
========================================================== */

.menu-group {
  margin-top: 28px;
}

.menu-group:first-child {
  margin-top: 8px;
}

.menu-group__title {
  display: block;

  margin-bottom: 10px;

  padding-left: 14px;

  font-size: .74rem;

  text-transform: uppercase;

  letter-spacing: 1.2px;

  color: rgba(255,255,255,.55);
}

/* ==========================================================
   MENU ITEM
========================================================== */

.menu-item {
  display: flex;
  align-items: center;

  gap: 14px;

  padding: 13px 14px;

  margin-bottom: 4px;

  border-radius: 12px;

  color: rgba(255,255,255,.88);

  text-decoration: none;

  transition:
    background .20s ease,
    transform .20s ease,
    color .20s ease;
}

.menu-item:hover {
  background: rgba(255,255,255,.10);

  color: white;

  transform: translateX(4px);
}

.menu-item.router-link-active {
  background: rgba(255,255,255,.16);

  color: white;

  font-weight: 600;

  box-shadow: inset 3px 0 0 #60A5FA;
}

.menu-item__icon {
  width: 22px;

  text-align: center;

  font-size: 1.05rem;
}

/* ==========================================================
   SIDEBAR FOOTER
========================================================== */

.sidebar__footer {
  padding: 20px 24px;

  border-top: 1px solid rgba(255,255,255,.08);

  display: flex;
  flex-direction: column;
  gap: 4px;

  font-size: .8rem;

  color: rgba(255,255,255,.75);
}

/* ==========================================================
   CONTENT
========================================================== */

.content {
  flex: 1;

  display: flex;
  flex-direction: column;

  min-width: 0;
}

/* ==========================================================
   TOPBAR
========================================================== */

.topbar {
  height: 88px;

  background: white;

  display: flex;
  justify-content: space-between;
  align-items: center;

  padding: 0 36px;

  border-bottom: 1px solid #e6ebf2;
}

.topbar__left h2 {
  margin: 0;

  font-size: 1.55rem;

  color: #1f2d3d;
}

.topbar__left p {
  margin: 5px 0 0;

  color: #6b7280;

  font-size: .92rem;
}

.topbar__right {
  display: flex;
  align-items: center;
  gap: 26px;
}

/* ==========================================================
   USER
========================================================== */

.user-info {
  display: flex;
  align-items: center;
  gap: 14px;
}

.user-avatar {
  width: 50px;
  height: 50px;

  border-radius: 50%;

  display: flex;
  justify-content: center;
  align-items: center;

  background: linear-gradient(
    135deg,
    #2563eb,
    #3b82f6
  );

  color: white;

  font-weight: 700;

  font-size: .95rem;

  box-shadow: 0 4px 12px rgba(37,99,235,.25);
}

.user-details {
  display: flex;
  flex-direction: column;
}

.user-details strong {
  color: #1f2937;

  font-size: .95rem;
}

.user-details small {
  color: #6b7280;

  font-size: .82rem;
}

/* ==========================================================
   LOGOUT
========================================================== */

.logout-button {
  border: none;

  border-radius: 10px;

  padding: 10px 22px;

  background: #2563eb;

  color: white;

  cursor: pointer;

  font-weight: 600;

  transition: .2s;
}

.logout-button:hover {
  background: #1d4ed8;

  transform: translateY(-1px);

  box-shadow: 0 6px 18px rgba(37,99,235,.20);
}

/* ==========================================================
   PAGE
========================================================== */

.page {
  flex: 1;

  padding: 36px;

  overflow-y: auto;
}

/* ==========================================================
   SCROLLBAR
========================================================== */

.sidebar__menu::-webkit-scrollbar {
  width: 6px;
}

.sidebar__menu::-webkit-scrollbar-thumb {
  background: rgba(255,255,255,.20);

  border-radius: 10px;
}

/* ==========================================================
   RESPONSIVIDADE
========================================================== */

@media (max-width: 1200px) {

  .sidebar {
    width: 250px;
  }

}

@media (max-width: 900px) {

  .dashboard-layout {
    flex-direction: column;
  }

  .sidebar {
    width: 100%;
  }

  .sidebar__menu {
    display: flex;
    flex-direction: row;

    overflow-x: auto;

    gap: 12px;

    padding-bottom: 18px;
  }

  .menu-group {
    min-width: 220px;
  }

  .sidebar__footer {
    display: none;
  }

  .topbar {
    flex-direction: column;

    align-items: flex-start;

    height: auto;

    padding: 24px;
  }

  .topbar__right {
    margin-top: 18px;

    width: 100%;

    justify-content: space-between;
  }

}

@media (max-width: 600px) {

  .page {
    padding: 18px;
  }

  .topbar {
    padding: 18px;
  }

  .topbar__left h2 {
    font-size: 1.25rem;
  }

  .user-details {
    display: none;
  }

}
</style>