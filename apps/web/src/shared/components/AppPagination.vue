<template>

    <div class="app-pagination">

        <div class="app-pagination__info">

            <slot name="info">

                Mostrando
                <strong>{{ startItem }}</strong>
                a
                <strong>{{ endItem }}</strong>
                de
                <strong>{{ totalItems }}</strong>
                registros

            </slot>

        </div>

        <div class="app-pagination__controls">

            <div class="app-pagination__page-size">

                <label for="page-size">

                    Itens por página

                </label>

                <select
                    id="page-size"
                    :value="pageSize"
                    @change="changePageSize"
                >

                    <option
                        v-for="option in pageSizeOptions"
                        :key="option"
                        :value="option"
                    >
                        {{ option }}
                    </option>

                </select>

            </div>

            <div class="app-pagination__buttons">

                <button
                    class="page-button"
                    :disabled="currentPage === 1"
                    @click="emit('update:currentPage', 1)"
                >
                    «
                </button>

                <button
                    class="page-button"
                    :disabled="currentPage === 1"
                    @click="emit('update:currentPage', currentPage - 1)"
                >
                    ‹
                </button>

                <button
                    v-for="page in visiblePages"
                    :key="page"
                    class="page-button"
                    :class="{
                        active: page === currentPage,
                    }"
                    @click="emit('update:currentPage', page)"
                >

                    {{ page }}

                </button>

                <button
                    class="page-button"
                    :disabled="currentPage === totalPages"
                    @click="emit('update:currentPage', currentPage + 1)"
                >
                    ›
                </button>

                <button
                    class="page-button"
                    :disabled="currentPage === totalPages"
                    @click="emit('update:currentPage', totalPages)"
                >
                    »
                </button>

            </div>

        </div>

    </div>

</template>

<script setup lang="ts">

/**
 * ============================================================================
 * App Pagination
 * ============================================================================
 *
 * Generic pagination component used across every paginated screen.
 *
 * Responsibilities
 * ----------------
 *
 * • Display pagination information.
 *
 * • Allow page navigation.
 *
 * • Allow page size selection.
 *
 * • Remain presentation-only.
 */

import { computed } from "vue";

const props = withDefaults(

    defineProps<{

        currentPage: number;

        pageSize: number;

        totalItems: number;

        pageSizeOptions?: number[];

    }>(),

    {

        pageSizeOptions: () => [

            10,

            20,

            50,

            100,

        ],

    },

);

const emit = defineEmits<{

    (

        event: "update:currentPage",

        value: number,

    ): void;

    (

        event: "update:pageSize",

        value: number,

    ): void;

}>();

const totalPages = computed(() =>

    Math.max(

        1,

        Math.ceil(

            props.totalItems /

            props.pageSize,

        ),

    ),

);

const startItem = computed(() =>

    props.totalItems === 0

        ? 0

        : (props.currentPage - 1) *

            props.pageSize +

            1,

);

const endItem = computed(() =>

    Math.min(

        props.currentPage *

            props.pageSize,

        props.totalItems,

    ),

);

const visiblePages = computed(() => {

    const pages: number[] = [];

    const radius = 2;

    const start = Math.max(

        1,

        props.currentPage - radius,

    );

    const end = Math.min(

        totalPages.value,

        props.currentPage + radius,

    );

    for (

        let page = start;

        page <= end;

        page++

    ) {

        pages.push(page);

    }

    return pages;

});

function changePageSize(

    event: Event,

): void {

    const value = Number(

        (

            event.target as HTMLSelectElement

        ).value,

    );

    emit(

        "update:pageSize",

        value,

    );

}

</script>

<style scoped>

.app-pagination{

    display:flex;

    justify-content:space-between;

    align-items:center;

    gap:2rem;

    padding:1.25rem 0;

}

.app-pagination__info{

    color:#64748b;

    font-size:.9rem;

}

.app-pagination__info strong{

    color:#0f172a;

    font-weight:600;

}

.app-pagination__controls{

    display:flex;

    align-items:center;

    gap:1.5rem;

}

.app-pagination__page-size{

    display:flex;

    align-items:center;

    gap:.75rem;

    color:#64748b;

    font-size:.9rem;

}

.app-pagination__page-size select{

    min-width:80px;

    height:38px;

    padding:0 .75rem;

    border:1px solid #dbe3ed;

    border-radius:10px;

    background:white;

    color:#0f172a;

    cursor:pointer;

}

.app-pagination__buttons{

    display:flex;

    align-items:center;

    gap:.4rem;

}

.page-button{

    min-width:38px;

    height:38px;

    border:1px solid #dbe3ed;

    border-radius:10px;

    background:white;

    color:#334155;

    cursor:pointer;

    transition:.2s;

    font-weight:600;

}

.page-button:hover:not(:disabled){

    background:#eff6ff;

    border-color:#2563eb;

    color:#2563eb;

}

.page-button.active{

    background:#2563eb;

    border-color:#2563eb;

    color:white;

}

.page-button:disabled{

    opacity:.45;

    cursor:not-allowed;

}

@media(max-width:768px){

    .app-pagination{

        flex-direction:column;

        align-items:flex-start;

    }

    .app-pagination__controls{

        width:100%;

        justify-content:space-between;

        flex-wrap:wrap;

    }

}

</style>