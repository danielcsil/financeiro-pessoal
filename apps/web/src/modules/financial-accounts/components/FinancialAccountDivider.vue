<template>

    <div class="divider">

        <span />

    </div>

</template>

<script setup lang="ts">
</script>

<style scoped>

.divider{

    display:flex;

    align-items:center;

    justify-content:center;

    margin:.5rem 0;

}

.divider span{

    display:block;

    width:100%;

    height:1px;

    background:linear-gradient(

        to right,

        transparent,

        #e2e8f0 12%,

        #e2e8f0 88%,

        transparent

    );

}

</style>