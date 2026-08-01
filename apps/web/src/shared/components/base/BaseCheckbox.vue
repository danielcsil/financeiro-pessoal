<script setup lang="ts">
/**
 * =============================================================================
 * Base Checkbox
 * =============================================================================
 *
 * Purpose
 * =============================================================================
 *
 * Reusable checkbox component used throughout the application.
 *
 * Features
 * --------
 *
 * • v-model support
 * • Label
 * • Description
 * • Disabled state
 * • Validation message
 * • Accessible
 *
 * This component intentionally contains no business logic.
 */

import { computed } from "vue";

interface Props {

    modelValue?: boolean;

    id?: string;

    name?: string;

    label?: string;

    description?: string;

    disabled?: boolean;

    error?: string;

}

const props = withDefaults(
    defineProps<Props>(),
    {
        modelValue: false,
        disabled: false,
        error: "",
    },
);

const emit = defineEmits<{

    (e: "update:modelValue", value: boolean): void;

    (e: "change", value: boolean): void;

}>();

const checked = computed({

    get: () => props.modelValue,

    set: (value: boolean) => {

        emit(
            "update:modelValue",
            value,
        );

        emit(
            "change",
            value,
        );

    },

});
</script>

<template>

<label
    class="checkbox"
    :class="{
        'checkbox--disabled': disabled,
    }"
>

    <input
        :id="id"
        v-model="checked"
        class="checkbox__input"
        type="checkbox"
        :name="name"
        :disabled="disabled"
        :aria-invalid="!!error"
    >

    <span class="checkbox__control" />

    <div class="checkbox__content">

        <span
            v-if="label"
            class="checkbox__label"
        >
            {{ label }}
        </span>

        <span
            v-if="description"
            class="checkbox__description"
        >
            {{ description }}
        </span>

        <small
            v-if="error"
            class="checkbox__error"
        >
            {{ error }}
        </small>

    </div>

</label>

</template>

<style scoped>

.checkbox{

    display:flex;

    align-items:flex-start;

    gap:.85rem;

    cursor:pointer;

}

.checkbox--disabled{

    opacity:.6;

    cursor:not-allowed;

}

.checkbox__input{

    display:none;

}

.checkbox__control{

    width:20px;

    height:20px;

    flex-shrink:0;

    border:2px solid var(--color-border);

    border-radius:6px;

    margin-top:2px;

    transition:all .2s;

    position:relative;

    background:var(--color-surface);

}

.checkbox__input:checked + .checkbox__control{

    background:var(--color-primary);

    border-color:var(--color-primary);

}

.checkbox__input:checked + .checkbox__control::after{

    content:"✓";

    position:absolute;

    inset:0;

    display:flex;

    justify-content:center;

    align-items:center;

    color:white;

    font-size:.8rem;

    font-weight:bold;

}

.checkbox__content{

    display:flex;

    flex-direction:column;

    gap:.2rem;

}

.checkbox__label{

    font-weight:600;

    color:var(--color-text);

}

.checkbox__description{

    color:var(--color-text-secondary);

    font-size:.88rem;

}

.checkbox__error{

    color:#dc2626;

    font-size:.82rem;

}

</style>