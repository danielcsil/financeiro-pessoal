<script setup lang="ts">
import AppNavbar from "../components/navigation/AppNavbar.vue";
import AppSidebar from "../components/navigation/AppSidebar.vue";
</script>

<template>

<div class="dashboard">

    <AppSidebar />

    <div class="dashboard__content">

        <AppNavbar />

        <main class="dashboard__page">

            <slot />

        </main>

    </div>

</div>

</template>

<style scoped>

.dashboard{

display:grid;

grid-template-columns:280px 1fr;

min-height:100vh;

background:var(--color-background);

}

.dashboard__content{

display:flex;

flex-direction:column;

min-width:0;

}

.dashboard__page{

flex:1;

padding:var(--space-6);

overflow:auto;

}

@media(max-width:1024px){

.dashboard{

grid-template-columns:1fr;

}

}

</style>