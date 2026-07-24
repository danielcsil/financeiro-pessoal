<template>
  <article class="feature-card">
    <div class="feature-card__icon">
      <component :is="icon" :size="30" />
    </div>

    <div class="feature-card__content">
      <h3>{{ title }}</h3>
      <p>{{ description }}</p>
    </div>
  </article>
</template>

<script setup lang="ts">
import type { Component } from "vue";

interface Props {
  icon: Component;
  title: string;
  description: string;
}

defineProps<Props>();
</script>

<style scoped>
.feature-card {
  display: flex;
  gap: 1.5rem;
  align-items: flex-start;

  padding: 2rem;

  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);

  transition:
    transform .25s ease,
    box-shadow .25s ease,
    border-color .25s ease;

  height: 100%;
}

.feature-card:hover {
  transform: translateY(-6px);

  border-color: var(--color-primary);

  box-shadow: var(--shadow-lg);
}

.feature-card__icon {
  width: 64px;
  height: 64px;

  display: flex;
  align-items: center;
  justify-content: center;

  flex-shrink: 0;

  border-radius: var(--radius-md);

  background: rgba(37, 99, 235, .08);
  color: var(--color-primary);
}

.feature-card__content {
  flex: 1;
}

.feature-card__content h3 {
  margin: 0 0 .75rem;

  color: var(--color-text-primary);

  font-size: 1.2rem;
  font-weight: 700;
}

.feature-card__content p {
  margin: 0;

  color: var(--color-text-secondary);

  line-height: 1.7;
}

@media (max-width: 768px) {
  .feature-card {
    flex-direction: column;
  }

  .feature-card__icon {
    width: 56px;
    height: 56px;
  }
}
</style>