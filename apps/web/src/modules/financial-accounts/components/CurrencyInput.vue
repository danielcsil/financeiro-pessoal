<template>
    <div class="currency-input">

        <span class="prefix">
            R$
        </span>

        <input
            ref="inputRef"
            :value="displayValue"
            type="text"
            inputmode="decimal"
            placeholder="0,00"
            @input="onInput"
            @blur="onBlur"
        />

    </div>
</template>

<script setup lang="ts">
import {
    computed,
    ref,
} from "vue";

const props = defineProps<{
    modelValue: number;
}>();

const emit = defineEmits<{
    (
        event: "update:modelValue",
        value: number,
    ): void;
}>();

const inputRef =
    ref<HTMLInputElement>();

const displayValue = computed(() => {

    return new Intl.NumberFormat(
        "pt-BR",
        {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2,
        },
    ).format(
        props.modelValue ?? 0,
    );

});

function onInput(
    event: Event,
) {

    const input =
        event.target as HTMLInputElement;

    const digits =
        input.value.replace(/\D/g, "");

    const value =
        Number(digits) / 100;

    emit(
        "update:modelValue",
        value,
    );

}

function onBlur() {

    if (!inputRef.value) {
        return;
    }

    inputRef.value.value =
        displayValue.value;

}
</script>

<style scoped>

.currency-input {

    display: flex;

    align-items: center;

    gap: .75rem;

    border: 1px solid #dbe4f0;

    border-radius: 14px;

    padding: .95rem 1rem;

    background: white;

    transition: .2s;

}

.currency-input:focus-within {

    border-color: #2563eb;

    box-shadow: 0 0 0 4px rgba(37,99,235,.12);

}

.prefix {

    color: #2563eb;

    font-weight: 700;

    font-size: 1rem;

}

input {

    flex: 1;

    border: none;

    outline: none;

    background: transparent;

    font-size: 1.2rem;

    font-weight: 600;

    color: #0f172a;

}

input::placeholder {

    color: #94a3b8;

}

</style>