<script setup lang="ts">
  import { RouterView } from "vue-router";
  import AppNavbar from "../components/navigation/AppNavbar.vue";
</script>

<template>
  <div class="public-layout">

    <AppNavbar />

    <main class="public-layout__content">
      <RouterView />
    </main>

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