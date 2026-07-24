<script setup lang="ts">
import { computed } from "vue";

interface Props {
  modelValue?: string | number;

  label?: string;

  placeholder?: string;

  type?: string;

  disabled?: boolean;

  error?: string;

  required?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  modelValue: "",
  placeholder: "",
  type: "text",
  disabled: false,
  error: "",
  required: false,
});

const emit = defineEmits<{
  (e: "update:modelValue", value: string): void;
}>();

const value = computed({
  get: () => String(props.modelValue),

  set: (value: string) => emit("update:modelValue", value),
});
</script>

<template>
  <div class="form-group">
    <label
      v-if="label"
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

    <input
      v-model="value"
      class="form-control"
      :class="{
        'is-invalid': error
      }"
      :type="type"
      :placeholder="placeholder"
      :disabled="disabled"
    >

    <small
      v-if="error"
      class="form-error"
    >
      {{ error }}
    </small>
  </div>
</template>