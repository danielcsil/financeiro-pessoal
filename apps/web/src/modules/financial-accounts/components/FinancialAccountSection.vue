<template>
    <section
        class="financial-section"
        aria-labelledby="section-title"
    >
        <header
            v-if="title || description"
            class="section-header"
        >
            <div class="section-header__content">
                <h3
                    v-if="title"
                    id="section-title"
                    class="section-title"
                >
                    {{ title }}
                </h3>

                <p
                    v-if="description"
                    class="section-description"
                >
                    {{ description }}
                </p>
            </div>
        </header>

        <div class="section-content">
            <!--
                Default slot.

                Every module is responsible for providing its own
                content (cards, tables, charts, forms, etc.).
            -->
            <slot />

            <!--
                Named slot kept for future flexibility.

                Allows future layouts without breaking compatibility.
            -->
            <slot name="content" />
        </div>
    </section>
</template>

<script setup lang="ts">
/**
 * ============================================================================
 * Financial Account Section
 * ============================================================================
 *
 * Generic layout component used throughout the application to organize
 * information into consistent visual sections.
 *
 * Responsibilities
 * ----------------
 * • Render an optional title.
 * • Render an optional description.
 * • Provide a responsive container for child components.
 *
 * This component intentionally contains no business logic.
 *
 * It must never:
 *
 * • call APIs;
 * • access stores;
 * • perform validations;
 * • manipulate state;
 * • implement financial rules.
 *
 * The content is supplied through Vue slots, making this component reusable
 * across every module of the application.
 *
 * Examples
 * --------
 *
 * Dashboard
 * Financial Accounts
 * Categories
 * Credit Cards
 * Investments
 * Goals
 * Reports
 */

interface Props {
    /**
     * Section title.
     */
    title?: string;

    /**
     * Optional section description.
     */
    description?: string;
}

defineProps<Props>();
</script>

<style scoped>
.financial-section {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.section-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
}

.section-header__content {
    display: flex;
    flex-direction: column;
}

.section-title {
    margin: 0;
    color: #0f172a;
    font-size: 1.15rem;
    font-weight: 700;
    line-height: 1.3;
}

.section-description {
    margin: 0.35rem 0 0;
    color: #64748b;
    font-size: 0.95rem;
    line-height: 1.5;
}

.section-content {
    display: grid;
    grid-template-columns:
        repeat(
            auto-fit,
            minmax(260px, 1fr)
        );
    gap: 1.5rem;
}

@media (max-width: 768px) {
    .section-content {
        grid-template-columns: 1fr;
        gap: 1rem;
    }
}
</style>