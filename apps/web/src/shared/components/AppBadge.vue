<template>

    <span
        class="app-badge"
        :class="[
            `app-badge--${variant}`,
            `app-badge--${size}`,
            {
                'app-badge--pill': pill,
            },
        ]"
    >

        <AppIcon
            v-if="icon"
            :name="icon"
            :size="iconSize"
        />

        <slot />

    </span>

</template>

<script setup lang="ts">

/**
 * ============================================================================
 * App Badge
 * ============================================================================
 *
 * Purpose
 * ============================================================================
 *
 * Generic badge component used throughout the application.
 *
 * It provides a consistent visual language for representing statuses,
 * categories, account types, labels and small indicators.
 *
 * ============================================================================
 * Responsibilities
 * ============================================================================
 *
 * • Display contextual information.
 *
 * • Support predefined visual variants.
 *
 * • Optionally display an icon.
 *
 * • Maintain consistent spacing and typography.
 *
 * ============================================================================
 * Design Principles
 * ============================================================================
 *
 * • Stateless.
 *
 * • Fully reusable.
 *
 * • Presentation only.
 *
 * • Accessible.
 */

import { computed } from "vue";

import AppIcon from "./AppIcon.vue";

type BadgeVariant =

    | "primary"
    | "secondary"
    | "success"
    | "danger"
    | "warning"
    | "info"
    | "purple"
    | "neutral";

type BadgeSize =

    | "sm"
    | "md"
    | "lg";

const props = withDefaults(

    defineProps<{

        /**
         * Visual style.
         */
        variant?: BadgeVariant;

        /**
         * Badge size.
         */
        size?: BadgeSize;

        /**
         * Optional icon.
         */
        icon?: string;

        /**
         * Rounded pill.
         */
        pill?: boolean;

    }>(),

    {

        variant: "primary",

        size: "md",

        pill: true,

    },

);

const iconSize = computed(() => {

    switch (props.size) {

        case "sm":
            return 12;

        case "lg":
            return 18;

        default:
            return 14;

    }

});

</script>

<style scoped>

/* ==========================================================================
   Base
========================================================================== */

.app-badge{

    display:inline-flex;

    align-items:center;

    justify-content:center;

    gap:.45rem;

    font-weight:600;

    line-height:1;

    white-space:nowrap;

    user-select:none;

    transition:

        background-color .2s,

        color .2s,

        border-color .2s;

}

.app-badge--pill{

    border-radius:999px;

}

/* ==========================================================================
   Sizes
========================================================================== */

.app-badge--sm{

    min-height:24px;

    padding:.20rem .60rem;

    font-size:.72rem;

}

.app-badge--md{

    min-height:30px;

    padding:.40rem .80rem;

    font-size:.80rem;

}

.app-badge--lg{

    min-height:36px;

    padding:.55rem 1rem;

    font-size:.92rem;

}

/* ==========================================================================
   Primary
========================================================================== */

.app-badge--primary{

    background:#dbeafe;

    color:#1d4ed8;

}

/* ==========================================================================
   Secondary
========================================================================== */

.app-badge--secondary{

    background:#f1f5f9;

    color:#334155;

}

/* ==========================================================================
   Success
========================================================================== */

.app-badge--success{

    background:#dcfce7;

    color:#15803d;

}

/* ==========================================================================
   Danger
========================================================================== */

.app-badge--danger{

    background:#fee2e2;

    color:#b91c1c;

}

/* ==========================================================================
   Warning
========================================================================== */

.app-badge--warning{

    background:#fef3c7;

    color:#b45309;

}

/* ==========================================================================
   Info
========================================================================== */

.app-badge--info{

    background:#cffafe;

    color:#0f766e;

}

/* ==========================================================================
   Purple
========================================================================== */

.app-badge--purple{

    background:#ede9fe;

    color:#6d28d9;

}

/* ==========================================================================
   Neutral
========================================================================== */

.app-badge--neutral{

    background:#f8fafc;

    color:#475569;

    border:1px solid #e2e8f0;

}

</style>