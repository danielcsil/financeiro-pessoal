<template>
    <div class="color-picker">

        <button
            v-for="color in colors"
            :key="color"
            type="button"
            class="color"
            :class="{
                selected: modelValue === color,
            }"
            :style="{
                backgroundColor: color,
            }"
            @click="$emit('update:modelValue', color)"
        >
            <span
                v-if="modelValue === color"
                class="check"
            >
                ✓
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

const colors = [
    "#2563EB",
    "#16A34A",
    "#9333EA",
    "#EA580C",
    "#DC2626",
    "#0891B2",
    "#CA8A04",
    "#475569",
    "#000000",
    "#EC4899",
];

</script>

<style scoped>

.color-picker {

    display: flex;

    flex-wrap: wrap;

    gap: 1rem;

}

.color {

    width: 44px;

    height: 44px;

    border-radius: 50%;

    border: 3px solid transparent;

    cursor: pointer;

    transition: all .2s;

    display: flex;

    align-items: center;

    justify-content: center;

}

.color:hover {

    transform: scale(1.1);

}

.selected {

    border-color: #0f172a;

    transform: scale(1.12);

    box-shadow: 0 0 0 4px rgba(37,99,235,.15);

}

.check {

    color: white;

    font-size: .9rem;

    font-weight: 700;

}

</style>