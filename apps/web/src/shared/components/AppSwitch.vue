<template>

    <label
        class="app-switch"
        :class="{
            disabled,
        }"
    >

        <input
            :checked="modelValue"
            :disabled="disabled"
            type="checkbox"
            @change="onChange"
        >

        <span class="track">

            <span class="thumb"/>

        </span>

        <div class="content">

            <span
                v-if="label"
                class="label"
            >
                {{ label }}
            </span>

            <span
                v-if="description"
                class="description"
            >
                {{ description }}
            </span>

        </div>

    </label>

</template>

<script setup lang="ts">

withDefaults(

    defineProps<{

        modelValue: boolean;

        label?: string;

        description?: string;

        disabled?: boolean;

    }>(),

    {

        disabled: false,

    },

);

const emit = defineEmits<{

    (

        event: "update:modelValue",

        value: boolean,

    ): void;

}>();

function onChange(
    event: Event,
) {

    emit(

        "update:modelValue",

        (event.target as HTMLInputElement).checked,

    );

}

</script>

<style scoped>

.app-switch{

    display:flex;

    align-items:center;

    gap:1rem;

    cursor:pointer;

}

input{

    display:none;

}

.track{

    width:52px;

    height:30px;

    background:#cbd5e1;

    border-radius:999px;

    position:relative;

    transition:.25s;

    flex-shrink:0;

}

.thumb{

    position:absolute;

    top:3px;

    left:3px;

    width:24px;

    height:24px;

    border-radius:50%;

    background:white;

    transition:.25s;

    box-shadow:

        0 2px 8px rgba(0,0,0,.15);

}

input:checked + .track{

    background:#2563eb;

}

input:checked + .track .thumb{

    transform:translateX(22px);

}

.content{

    display:flex;

    flex-direction:column;

    gap:.2rem;

}

.label{

    font-weight:600;

    color:#0f172a;

}

.description{

    color:#64748b;

    font-size:.85rem;

}

.disabled{

    opacity:.6;

    cursor:not-allowed;

}

</style>