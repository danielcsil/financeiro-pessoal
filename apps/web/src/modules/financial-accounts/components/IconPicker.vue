<template>
    <div class="icon-picker">

        <button
            v-for="icon in icons"
            :key="icon.value"
            type="button"
            class="icon-button"
            :class="{
                selected: modelValue === icon.value,
            }"
            @click="$emit('update:modelValue', icon.value)"
        >
            <span class="emoji">
                {{ icon.emoji }}
            </span>

            <span class="label">
                {{ icon.label }}
            </span>
        </button>

    </div>
</template>

<script setup lang="ts">

defineProps<{
    modelValue: string;
}>();

defineEmits<{
    (
        event: "update:modelValue",
        value: string,
    ): void;
}>();

const icons = [
    {
        value: "wallet",
        emoji: "👛",
        label: "Carteira",
    },
    {
        value: "bank",
        emoji: "🏦",
        label: "Banco",
    },
    {
        value: "credit-card",
        emoji: "💳",
        label: "Cartão",
    },
    {
        value: "cash",
        emoji: "💵",
        label: "Dinheiro",
    },
    {
        value: "coins",
        emoji: "🪙",
        label: "Moedas",
    },
    {
        value: "chart",
        emoji: "📈",
        label: "Invest.",
    },
    {
        value: "piggy-bank",
        emoji: "🐷",
        label: "Poupança",
    },
    {
        value: "safe",
        emoji: "🔐",
        label: "Cofre",
    },
    {
        value: "building",
        emoji: "🏢",
        label: "Empresa",
    },
];
</script>

<style scoped>

.icon-picker {

    display: grid;

    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));

    gap: 1rem;

}

.icon-button {

    display: flex;

    flex-direction: column;

    align-items: center;

    justify-content: center;

    gap: .75rem;

    padding: 1rem;

    border: 1px solid #e2e8f0;

    border-radius: 16px;

    background: white;

    cursor: pointer;

    transition: all .25s;

}

.icon-button:hover {

    border-color: #2563eb;

    transform: translateY(-2px);

    box-shadow: 0 8px 18px rgba(0,0,0,.08);

}

.selected {

    background: #eff6ff;

    border: 2px solid #2563eb;

}

.emoji {

    font-size: 2rem;

}

.label {

    font-size: .85rem;

    font-weight: 600;

    color: #334155;

    text-align: center;

}

@media (max-width: 768px) {

    .icon-picker {

        grid-template-columns: repeat(3, 1fr);

    }

}

</style>