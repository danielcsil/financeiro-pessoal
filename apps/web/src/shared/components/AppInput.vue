<template>

    <div class="app-input">

        <label
            v-if="label"
            class="label"
        >
            {{ label }}

            <span
                v-if="required"
                class="required"
            >
                *
            </span>

        </label>

        <div
            class="input-wrapper"
            :class="{
                error: !!error,
                disabled,
            }"
        >

            <slot
                name="prepend"
            />

            <input
                :model-value="modelValue"
                :type="type"
                :placeholder="placeholder"
                :disabled="disabled"
                :readonly="readonly"
                :autocomplete="autocomplete"
                @input="onInput"
                @blur="$emit('blur')"
                @focus="$emit('focus')"
            >

            <slot
                name="append"
            />

        </div>

        <small
            v-if="helper && !error"
            class="helper"
        >
            {{ helper }}
        </small>

        <small
            v-if="error"
            class="error-message"
        >
            {{ error }}
        </small>

    </div>

</template>

<script setup lang="ts">

withDefaults(

    defineProps<{

        modelValue: string;

        label?: string;

        placeholder?: string;

        helper?: string;

        error?: string;

        required?: boolean;

        disabled?: boolean;

        readonly?: boolean;

        autocomplete?: string;

        type?: string;

    }>(),

    {

        type: "text",

        placeholder: "",

        helper: "",

        error: "",

        autocomplete: "off",

        disabled: false,

        readonly: false,

        required: false,

    },

);

const emit = defineEmits<{

    (
        event: "update:modelValue",
        value: string,
    ): void;

    (
        event: "blur",
    ): void;

    (
        event: "focus",
    ): void;

}>();

function onInput(
    event: Event,
) {

    emit(

        "update:modelValue",

        (event.target as HTMLInputElement).value,

    );

}

</script>

<style scoped>

.app-input{

    display:flex;

    flex-direction:column;

    gap:.5rem;

}

.label{

    font-size:.92rem;

    font-weight:600;

    color:#334155;

}

.required{

    color:#dc2626;

}

.input-wrapper{

    display:flex;

    align-items:center;

    gap:.75rem;

    background:white;

    border:1px solid #dbe4f0;

    border-radius:14px;

    padding:0 .95rem;

    transition:.2s;

}

.input-wrapper:focus-within{

    border-color:#2563eb;

    box-shadow:

        0 0 0 4px rgba(37,99,235,.12);

}

.input-wrapper.error{

    border-color:#dc2626;

}

.input-wrapper.error:focus-within{

    box-shadow:

        0 0 0 4px rgba(220,38,38,.12);

}

.input-wrapper.disabled{

    background:#f8fafc;

    opacity:.7;

}

input{

    flex:1;

    height:48px;

    border:none;

    outline:none;

    background:transparent;

    color:#0f172a;

    font-size:1rem;

}

input::placeholder{

    color:#94a3b8;

}

.helper{

    color:#64748b;

    font-size:.82rem;

}

.error-message{

    color:#dc2626;

    font-size:.82rem;

    font-weight:500;

}

</style>