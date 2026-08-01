<script setup lang="ts">
/**
 * =============================================================================
 * Base Select
 * =============================================================================
 *
 * Purpose
 * =============================================================================
 *
 * Reusable select component used throughout the application.
 *
 * Features
 * --------
 *
 * • v-model support
 * • Label
 * • Placeholder
 * • Validation message
 * • Required indicator
 * • Disabled state
 * • Accessibility
 *
 * This component intentionally contains no business logic.
 */

import { computed } from "vue";

export interface SelectOption {

  value: string;

  label: string;

}

interface Props {

  modelValue?: string;

  id?: string;

  name?: string;

  label?: string;

  placeholder?: string;

  options: SelectOption[];

  disabled?: boolean;

  required?: boolean;

  error?: string;

}

const props = withDefaults(
  defineProps<Props>(),
  {
    modelValue: "",
    placeholder: "Select an option",
    disabled: false,
    required: false,
    error: "",
  },
);

const emit = defineEmits<{

  (e: "update:modelValue", value: string): void;

  (e: "blur"): void;

  (e: "focus"): void;

}>();

const value = computed({

  get: () => props.modelValue,

  set: (value: string) =>
    emit(
      "update:modelValue",
      value,
    ),

});
</script>

<template>

<div class="form-group">

    <label
        v-if="label"
        :for="id"
        class="form-label"
    >

        {{ label }}

        <span
            v-if="required"
            class="form-required"
        >
            *
        </span>

    </label>

    <select
        :id="id"
        v-model="value"
        class="form-control"
        :class="{
            'is-invalid': error,
        }"
        :name="name"
        :disabled="disabled"
        :required="required"
        :aria-invalid="!!error"
        :aria-describedby="error ? `${id}-error` : undefined"
        @blur="emit('blur')"
        @focus="emit('focus')"
    >

        <option
            value=""
            disabled
        >
            {{ placeholder }}
        </option>

        <option
            v-for="option in options"
            :key="option.value"
            :value="option.value"
        >
            {{ option.label }}
        </option>

    </select>

    <small
        v-if="error"
        :id="`${id}-error`"
        class="form-error"
    >
        {{ error }}
    </small>

</div>

</template>

<style scoped>

.form-group{

    display:flex;

    flex-direction:column;

    gap:.5rem;

}

.form-label{

    font-weight:600;

    color:var(--color-text);

}

.form-required{

    color:#dc2626;

}

.form-control{

    width:100%;

    padding:.85rem 1rem;

    border:1px solid var(--color-border);

    border-radius:.75rem;

    background:var(--color-surface);

    color:var(--color-text);

    font:inherit;

    transition:border-color .2s;

}

.form-control:focus{

    outline:none;

    border-color:var(--color-primary);

}

.form-control:disabled{

    cursor:not-allowed;

    opacity:.7;

}

.is-invalid{

    border-color:#dc2626;

}

.form-error{

    color:#dc2626;

    font-size:.85rem;

}

</style>