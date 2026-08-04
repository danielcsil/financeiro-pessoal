<template>

    <div class="app-select">

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

        <div class="wrapper">

            <select
                :value="modelValue"
                :disabled="disabled"
                @change="onChange"
            >

                <option
                    v-if="placeholder"
                    disabled
                    value=""
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

        </div>

        <small
            v-if="helper && !error"
            class="helper"
        >
            {{ helper }}
        </small>

        <small
            v-if="error"
            class="error"
        >
            {{ error }}
        </small>

    </div>

</template>

<script setup lang="ts">

export interface SelectOption {

    value: string;

    label: string;

}

withDefaults(

    defineProps<{

        modelValue: string;

        options: SelectOption[];

        label?: string;

        placeholder?: string;

        helper?: string;

        error?: string;

        required?: boolean;

        disabled?: boolean;

    }>(),

    {

        placeholder: "",

        helper: "",

        error: "",

        required: false,

        disabled: false,

    },

);

const emit = defineEmits<{

    (

        event: "update:modelValue",

        value: string,

    ): void;

}>();

function onChange(
    event: Event,
) {

    emit(

        "update:modelValue",

        (event.target as HTMLSelectElement).value,

    );

}

</script>

<style scoped>

.app-select{

    display:flex;

    flex-direction:column;

    gap:.5rem;

}

.label{

    font-size:.9rem;

    font-weight:600;

    color:#334155;

}

.required{

    color:#dc2626;

}

.wrapper{

    position:relative;

}

.wrapper::after{

    content:"⌄";

    position:absolute;

    right:1rem;

    top:50%;

    transform:translateY(-50%);

    pointer-events:none;

    color:#64748b;

    font-size:.9rem;

}

select{

    width:100%;

    height:48px;

    padding:0 2.5rem 0 1rem;

    border:1px solid #dbe4f0;

    border-radius:14px;

    background:white;

    color:#0f172a;

    font-size:1rem;

    appearance:none;

    transition:.2s;

}

select:focus{

    outline:none;

    border-color:#2563eb;

    box-shadow:0 0 0 4px rgba(37,99,235,.12);

}

.helper{

    font-size:.82rem;

    color:#64748b;

}

.error{

    font-size:.82rem;

    color:#dc2626;

}

</style>