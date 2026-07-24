<script setup lang="ts">
import AppNavbar from "../components/navigation/AppNavbar.vue";
import AppFooter from "../components/navigation/AppFooter.vue";
</script>

<template>
  <div class="public-layout">

    <AppNavbar />

    <main class="public-layout__content">
      <slot />
    </main>

    <AppFooter />

  </div>
</template>

<style scoped>
.public-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.public-layout__content {
  flex: 1;
}
</style>