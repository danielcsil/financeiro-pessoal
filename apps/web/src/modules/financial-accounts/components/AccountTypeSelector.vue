<template>
    <div class="account-type-selector">

        <button
            v-for="option in options"
            :key="option.value"
            type="button"
            class="option"
            :class="{
                selected: modelValue === option.value,
            }"
            @click="$emit('update:modelValue', option.value)"
        >

            <span class="icon">
                {{ option.icon }}
            </span>

            <span class="title">
                {{ option.title }}
            </span>

        </button>

    </div>
</template>

<script setup lang="ts">
import { AccountType } from "../types/financial-account";

defineProps<{
    modelValue: AccountType;
}>();

defineEmits<{
    (
        event: "update:modelValue",
        value: AccountType,
    ): void;
}>();

const options = [
    {
        value: AccountType.CHECKING,
        title: "Conta Corrente",
        icon: "🏦",
    },
    {
        value: AccountType.SAVINGS,
        title: "Poupança",
        icon: "💰",
    },
    {
        value: AccountType.INVESTMENT,
        title: "Investimento",
        icon: "📈",
    },
    {
        value: AccountType.CASH,
        title: "Dinheiro",
        icon: "💵",
    },
    {
        value: AccountType.DIGITAL_WALLET,
        title: "Carteira",
        icon: "👛",
    },
    {
        value: AccountType.OTHER,
        title: "Outra",
        icon: "💳",
    },
];
</script>

<style scoped>

.account-type-selector{

    display:grid;

    grid-template-columns:repeat(auto-fit,minmax(150px,1fr));

    gap:1rem;

}

.option{

    display:flex;

    flex-direction:column;

    align-items:center;

    justify-content:center;

    gap:.75rem;

    height:120px;

    border:1px solid #e2e8f0;

    border-radius:16px;

    background:white;

    cursor:pointer;

    transition:.25s;

}

.option:hover{

    border-color:#2563eb;

    transform:translateY(-2px);

    box-shadow:0 10px 20px rgba(0,0,0,.06);

}

.selected{

    background:#eff6ff;

    border:2px solid #2563eb;

}

.icon{

    font-size:2rem;

}

.title{

    font-size:.9rem;

    font-weight:600;

    color:#334155;

}

@media(max-width:768px){

    .account-type-selector{

        grid-template-columns:repeat(2,1fr);

    }

}

</style>