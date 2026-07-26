<script setup lang="ts">
import { RouterView } from "vue-router";
</script>

<template>
  <div class="auth-layout">
    <div class="auth-layout__left">
      <div class="auth-layout__brand">
        <h1>Personal Finance</h1>

        <p>
          Organize suas finanças, elimine dívidas e alcance seus objetivos.
        </p>
      </div>
    </div>

    <div class="auth-layout__right">
      <div class="auth-layout__card">
        <RouterView />
      </div>
    </div>
  </div>
</template>

<style scoped>
.auth-layout {
  display: grid;
  grid-template-columns: 1fr 520px;
  min-height: 100vh;
}

.auth-layout__left {
  background: linear-gradient(
    135deg,
    var(--color-primary),
    var(--color-secondary)
  );

  display: flex;
  align-items: center;
  justify-content: center;

  padding: var(--space-10);

  color: white;
}

.auth-layout__brand {
  max-width: 500px;
}

.auth-layout__brand h1 {
  font-size: 3rem;
  margin-bottom: var(--space-6);
}

.auth-layout__brand p {
  color: white;
  opacity: 0.9;
}

.auth-layout__right {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-8);
  background: var(--color-background);
}

.auth-layout__card {
  width: 100%;
  max-width: 420px;
}

@media (max-width: 1024px) {
  .auth-layout {
    grid-template-columns: 1fr;
  }

  .auth-layout__left {
    display: none;
  }
}
</style>