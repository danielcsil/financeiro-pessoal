<script setup lang="ts">
import { computed, ref } from "vue";
import { RouterLink, useRoute } from "vue-router";

interface MenuItem {
  label: string;
  to: string;
}

const route = useRoute();

const mobileMenuOpen = ref(false);

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

function toggleMenu() {
  mobileMenuOpen.value = !mobileMenuOpen.value;
}

function closeMenu() {
  mobileMenuOpen.value = false;
}

const isAuthenticated = computed(() => false);
</script>

<template>
  <header class="navbar">
    <div class="navbar__container">
      <RouterLink
        to="/"
        class="navbar__brand"
      >
        <span class="navbar__logo">PF</span>
        <span>Personal Finance</span>
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
        <RouterLink
          v-if="!isAuthenticated"
          to="/login"
          class="btn btn-secondary"
        >
          Entrar
        </RouterLink>

        <RouterLink
          v-if="!isAuthenticated"
          to="/register"
          class="btn btn-primary"
        >
          Criar Conta
        </RouterLink>

        <RouterLink
          v-else
          to="/dashboard"
          class="btn btn-primary"
        >
          Dashboard
        </RouterLink>
      </div>
    </div>
  </header>
</template>

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
  font-size: 1.35rem;
  font-weight: 700;

  color: var(--color-primary);

  text-decoration: none;
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

.navbar__toggle {
  display: none;

  border: none;
  background: transparent;

  font-size: 1.6rem;
  cursor: pointer;
}

@media (max-width: 900px) {

  .navbar__container {
    flex-wrap: wrap;
  }

  .navbar__toggle {
    display: block;
  }

  .navbar__menu {
    display: none;

    width: 100%;
    flex-direction: column;
    justify-content: flex-start;

    padding-top: 1rem;
  }

  .navbar__menu--open {
    display: flex;
  }

  .navbar__actions {
    width: 100%;
    justify-content: flex-end;
  }
}
</style>