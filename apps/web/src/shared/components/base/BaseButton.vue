<script setup lang="ts">
import { computed } from "vue";

interface Props {
  variant?:
    | "primary"
    | "secondary"
    | "outline"
    | "ghost"
    | "success"
    | "danger";

  size?: "sm" | "md" | "lg";

  block?: boolean;

  disabled?: boolean;

  loading?: boolean;

  type?: "button" | "submit" | "reset";
}

const props = withDefaults(defineProps<Props>(), {
  variant: "primary",
  size: "md",
  block: false,
  disabled: false,
  loading: false,
  type: "button",
});

const classes = computed(() => [
  "btn",
  `btn-${props.variant}`,
  `btn-${props.size}`,
  {
    "btn-block": props.block,
    "btn-loading": props.loading,
  },
]);
</script>

<template>
  <button
    :type="type"
    :disabled="disabled || loading"
    :class="classes"
  >
    <slot />
  </button>
</template>