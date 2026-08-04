<template>

    <button
        :type="type"
        :disabled="disabled || loading"
        class="app-button"
        :class="[
            variant,
            size,
            {
                loading,
                block,
            },
        ]"
    >

        <span
            v-if="loading"
            class="spinner"
        />

        <slot
            v-else
        />

    </button>

</template>

<script setup lang="ts">

withDefaults(

    defineProps<{

        type?:
            | "button"
            | "submit"
            | "reset";

        variant?:
            | "primary"
            | "secondary"
            | "success"
            | "danger"
            | "ghost";

        size?:
            | "sm"
            | "md"
            | "lg";

        loading?: boolean;

        disabled?: boolean;

        block?: boolean;

    }>(),

    {

        type: "button",

        variant: "primary",

        size: "md",

        loading: false,

        disabled: false,

        block: false,

    },

);

</script>

<style scoped>

.app-button{

    display:inline-flex;

    align-items:center;

    justify-content:center;

    gap:.6rem;

    border:none;

    border-radius:14px;

    cursor:pointer;

    font-weight:600;

    transition:.25s;

    white-space:nowrap;

}

.block{

    width:100%;

}

/* =======================================================
   Sizes
======================================================= */

.sm{

    height:38px;

    padding:0 1rem;

    font-size:.85rem;

}

.md{

    height:46px;

    padding:0 1.35rem;

    font-size:.95rem;

}

.lg{

    height:54px;

    padding:0 2rem;

    font-size:1rem;

}

/* =======================================================
   Variants
======================================================= */

.primary{

    background:#2563eb;

    color:white;

}

.primary:hover:not(:disabled){

    background:#1d4ed8;

    transform:translateY(-2px);

}

.secondary{

    background:white;

    color:#334155;

    border:1px solid #cbd5e1;

}

.secondary:hover:not(:disabled){

    background:#f8fafc;

}

.success{

    background:#16a34a;

    color:white;

}

.success:hover:not(:disabled){

    background:#15803d;

}

.danger{

    background:#dc2626;

    color:white;

}

.danger:hover:not(:disabled){

    background:#b91c1c;

}

.ghost{

    background:transparent;

    color:#334155;

}

.ghost:hover:not(:disabled){

    background:#f1f5f9;

}

/* =======================================================
   States
======================================================= */

button:disabled{

    opacity:.6;

    cursor:not-allowed;

    transform:none;

}

.loading{

    pointer-events:none;

}

/* =======================================================
   Spinner
======================================================= */

.spinner{

    width:18px;

    height:18px;

    border:2px solid rgba(255,255,255,.35);

    border-top-color:white;

    border-radius:50%;

    animation:spin .8s linear infinite;

}

.secondary .spinner,

.ghost .spinner{

    border-color:#cbd5e1;

    border-top-color:#2563eb;

}

@keyframes spin{

    to{

        transform:rotate(360deg);

    }

}

</style>