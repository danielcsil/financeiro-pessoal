<script setup lang="ts">
/**
 * =============================================================================
 * Base Button
 * =============================================================================
 *
 * Standard button used across the application.
 *
 * Features
 * --------
 * • Visual variants
 * • Three sizes
 * • Loading state
 * • Disabled state
 * • Full width option
 * • Accessible
 */

import { computed } from "vue";

type Variant =
  | "primary"
  | "secondary"
  | "outline"
  | "ghost"
  | "success"
  | "danger";

type Size =
  | "sm"
  | "md"
  | "lg";

interface Props {
  variant?: Variant;

  size?: Size;

  block?: boolean;

  disabled?: boolean;

  loading?: boolean;

  type?: "button" | "submit" | "reset";
}

const props = withDefaults(
  defineProps<Props>(),
  {
    variant: "primary",
    size: "md",
    block: false,
    disabled: false,
    loading: false,
    type: "button",
  },
);

const emit = defineEmits<{
  click: [event: MouseEvent];
}>();

const classes = computed(() => [
  "btn",
  `btn-${props.variant}`,
  `btn-${props.size}`,
  {
    "btn-block": props.block,
    "btn-loading": props.loading,
  },
]);

function onClick(
  event: MouseEvent,
): void {

  if (
    props.disabled ||
    props.loading
  ) {

    event.preventDefault();

    return;

  }

  emit(
    "click",
    event,
  );

}
</script>

<template>
  <button
    :type="type"
    :disabled="disabled || loading"
    :class="classes"
    :aria-busy="loading"
    @click="onClick"
  >
    <span
      v-if="loading"
      class="btn-spinner"
    />

    <slot />
  </button>
</template>

<style scoped>

.btn{

    display:inline-flex;

    align-items:center;

    justify-content:center;

    gap:.6rem;

    border-radius:.75rem;

    border:none;

    cursor:pointer;

    font-weight:600;

    transition:
        all .2s ease;

}

.btn:hover:not(:disabled){

    transform:translateY(-1px);

}

.btn:disabled{

    opacity:.65;

    cursor:not-allowed;

}

.btn-block{

    width:100%;

}

.btn-sm{

    padding:.55rem 1rem;

    font-size:.85rem;

}

.btn-md{

    padding:.8rem 1.4rem;

}

.btn-lg{

    padding:1rem 1.8rem;

    font-size:1rem;

}

.btn-primary{

    background:var(--color-primary);

    color:white;

}

.btn-secondary{

    background:var(--color-surface);

    color:var(--color-text);

    border:1px solid var(--color-border);

}

.btn-outline{

    background:transparent;

    color:var(--color-primary);

    border:1px solid var(--color-primary);

}

.btn-ghost{

    background:transparent;

    color:var(--color-text);

}

.btn-success{

    background:#16a34a;

    color:white;

}

.btn-danger{

    background:#dc2626;

    color:white;

}

.btn-spinner{

    width:16px;

    height:16px;

    border-radius:50%;

    border:2px solid rgba(255,255,255,.35);

    border-top-color:white;

    animation:spin .7s linear infinite;

}

@keyframes spin{

    from{

        transform:rotate(0deg);

    }

    to{

        transform:rotate(360deg);

    }

}

</style>