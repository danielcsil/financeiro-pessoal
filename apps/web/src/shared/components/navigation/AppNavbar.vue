<template>
  <header class="navbar">
    <div class="navbar__container">
      <RouterLink
        to="/"
        class="navbar__brand"
      >
        <svg
          class="navbar__logo"
          viewBox="0 0 32 32"
          xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
        >
          <!-- Base -->
          <path
            d="M4 28H28"
            stroke="currentColor"
            stroke-width="3"
            stroke-linecap="round"
          />

          <!-- Barras -->
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

        <span class="navbar__brand-text">
          Personal Finance
        </span>
      </RouterLink>

      <button
        class="navbar__toggle"
        type="button"
        @click="toggleMenu"
        aria-label="Abrir menu"
      >
        ☰
      </button>

      <nav
        class="navbar__menu"
        :class="{ 'navbar__menu--open': mobileMenuOpen }"
      >
        <RouterLink
          v-for="item in menuItems"
          :key="item.to"
          :to="item.to"
          class="navbar__link"
          :class="{ active: route.path === item.to }"
          @click="closeMenu"
        >
          {{ item.label }}
        </RouterLink>
      </nav>

      <div class="navbar__actions">
        <template v-if="!isAuthenticated">
          <RouterLink
            to="/login"
            class="btn btn-outline"
          >
            Entrar
          </RouterLink>

          <RouterLink
            to="/register"
            class="btn btn-primary"
          >
            Criar Conta
          </RouterLink>
        </template>

        <div
          v-else
          class="navbar__authenticated"
        >
          <RouterLink
            to="/dashboard"
            class="btn btn-primary"
            @click="closeMenu"
          >
            Dashboard
          </RouterLink>

          <button
            type="button"
            class="btn btn-outline"
            @click="logout"
          >
            Sair
          </button>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import { RouterLink, useRoute, useRouter } from "vue-router";

import { useAuthStore } from "@/modules/auth/stores/auth.store";

/**
 * Estrutura dos itens do menu principal.
 */
interface MenuItem {
  label: string;
  to: string;
}

const route = useRoute();
const router = useRouter();

/**
 * Store central de autenticação.
 *
 * A Navbar apenas consulta o estado e executa
 * ações disponibilizadas pela AuthStore.
 */
const auth = useAuthStore();

/**
 * Controla a abertura do menu mobile.
 */
const mobileMenuOpen = ref(false);

/**
 * Itens do menu público.
 */
const menuItems: MenuItem[] = [
  {
    label: "Início",
    to: "/",
  },
  {
    label: "Funcionalidades",
    to: "/features",
  },
  {
    label: "Preços",
    to: "/pricing",
  },
  {
    label: "Contato",
    to: "/contact",
  },
];

/**
 * Alterna o estado do menu mobile.
 */
function toggleMenu() {
  mobileMenuOpen.value = !mobileMenuOpen.value;
}

/**
 * Fecha o menu mobile.
 */
function closeMenu() {
  mobileMenuOpen.value = false;
}

/**
 * Indica se existe um usuário autenticado.
 *
 * A Navbar nunca consulta localStorage.
 * Todo o estado vem da AuthStore.
 */
const isAuthenticated = computed(() => auth.isAuthenticated);

/**
 * Encerra a sessão do usuário.
 *
 * Fluxo:
 * 1. Fecha o menu.
 * 2. Remove a sessão através da AuthStore.
 * 3. Redireciona para Login.
 */
async function logout() {
  closeMenu();

  auth.logout();

  await router.replace("/login");
}
</script>

<style scoped>
.navbar {
  position: sticky;
  top: 0;
  z-index: 1000;

  background: var(--color-surface);
  border-bottom: 1px solid var(--color-border);

  backdrop-filter: blur(10px);
}

.navbar__container {
  max-width: 1280px;
  margin: 0 auto;

  display: flex;
  align-items: center;
  justify-content: space-between;

  padding: 1rem 2rem;
  gap: 2rem;
}

.navbar__brand {
  display: flex;
  align-items: center;
  gap: .75rem;

  color: var(--color-primary);
  text-decoration: none;

  flex-shrink: 0;
}

.navbar__logo {
  width: 48px;
  height: 48px;

  display: block;
  flex-shrink: 0;
}

.navbar__brand-text {
  font-size: 1.6rem;
  font-weight: 700;
  line-height: 1;
  white-space: nowrap;
}

.navbar__menu {
  display: flex;
  gap: 1.5rem;
  flex: 1;
  justify-content: center;
}

.navbar__link {
  color: var(--color-text);
  text-decoration: none;
  transition: .2s;
}

.navbar__link:hover {
  color: var(--color-primary);
}

.navbar__link.active {
  color: var(--color-primary);
  font-weight: 600;
}

.navbar__actions {
  display: flex;
  gap: .75rem;
}

.navbar__authenticated {
  display: flex;
  gap: .75rem;
  align-items: center;
}

.navbar__toggle {
  display: none;

  border: none;
  background: transparent;

  font-size: 1.6rem;
  cursor: pointer;
}

@media (max-width: 900px) {

  .navbar__container {
    max-width: 1280px;
    margin: 0 auto;

    display: flex;
    align-items: center;
    justify-content: space-between;

    padding: 1rem 2rem;
    gap: 2rem;
  }

  .navbar__toggle {
    display: block;
  }

  .navbar__menu {
    display: flex;
    gap: 1.5rem;
    flex: 1;
    justify-content: center;
  }

  .navbar__menu--open {
    display: flex;
  }

  .navbar__actions {
    display: flex;
    gap: .75rem;

    margin-left: auto;
    flex-shrink: 0;
  }

  .navbar__authenticated {
    display: flex;
    gap: .75rem;
  }
}
</style>