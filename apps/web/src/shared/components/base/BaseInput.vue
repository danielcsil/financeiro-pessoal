<script setup lang="ts">
/**
 * ============================================================================
 * Base Input
 * ============================================================================
 *
 * Reusable text input component used throughout the application.
 *
 * Features
 * --------
 * • v-model
 * • Label
 * • Validation message
 * • Required indicator
 * • Prefix/Suffix slots
 * • Accessibility
 */

import { computed } from "vue";

interface Props {

  modelValue?: string | number;

  id?: string;

  name?: string;

  label?: string;

  placeholder?: string;

  type?: string;

  autocomplete?: string;

  maxlength?: number;

  disabled?: boolean;

  readonly?: boolean;

  required?: boolean;

  error?: string;

}

const props = withDefaults(
  defineProps<Props>(),
  {
    modelValue: "",
    type: "text",
    placeholder: "",
    autocomplete: "off",
    disabled: false,
    readonly: false,
    required: false,
    error: "",
  },
);

const emit = defineEmits<{

  (e: "update:modelValue", value: string): void;

  (e: "blur"): void;

  (e: "focus"): void;

  (e: "enter"): void;

}>();

const value = computed({

  get: () => String(props.modelValue),

  set: (value: string) =>
    emit(
      "update:modelValue",
      value,
    ),

});

function onKeydown(
  event: KeyboardEvent,
): void {

  if (event.key === "Enter") {

    emit("enter");

  }

}
</script>

<template>

<div class="form-group">

    <label
        v-if="label"
        class="form-label"
        :for="id"
    >

        {{ label }}

        <span
            v-if="required"
            class="form-required"
        >
            *
        </span>

    </label>

    <div
        class="input-wrapper"
        :class="{
            'has-error': error,
        }"
    >

        <slot name="prepend" />

        <input
            :id="id"
            v-model="value"
            class="form-control"
            :type="type"
            :name="name"
            :placeholder="placeholder"
            :autocomplete="autocomplete"
            :maxlength="maxlength"
            :readonly="readonly"
            :disabled="disabled"
            :required="required"
            :aria-invalid="!!error"
            :aria-describedby="error ? `${id}-error` : undefined"
            @blur="emit('blur')"
            @focus="emit('focus')"
            @keydown="onKeydown"
        >

        <slot name="append" />

    </div>

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

    gap:.45rem;

}

.form-label{

    font-weight:600;

    color:var(--color-text);

}

.form-required{

    color:#dc2626;

}

.input-wrapper{

    display:flex;

    align-items:center;

    gap:.5rem;

    border:1px solid var(--color-border);

    border-radius:.75rem;

    padding:0 .75rem;

    background:var(--color-surface);

    transition:border-color .2s;

}

.input-wrapper:focus-within{

    border-color:var(--color-primary);

}

.input-wrapper.has-error{

    border-color:#dc2626;

}

.form-control{

    flex:1;

    border:none;

    outline:none;

    background:transparent;

    padding:.85rem 0;

    font:inherit;

}

.form-control:disabled{

    cursor:not-allowed;

    opacity:.7;

}

.form-error{

    color:#dc2626;

    font-size:.85rem;

}

</style>