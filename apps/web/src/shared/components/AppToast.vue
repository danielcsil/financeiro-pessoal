<template>

    <Transition name="toast">

        <div
            v-if="visible"
            class="toast"
            :class="variant"
        >

            <div class="icon">

                <AppIcon
                    :name="icon"
                    :size="20"
                />

            </div>

            <div class="content">

                <strong>
                    {{ title }}
                </strong>

                <span
                    v-if="message"
                >
                    {{ message }}
                </span>

            </div>

            <button
                class="close-button"
                @click="close"
            >
                ×
            </button>

        </div>

    </Transition>

</template>

<script setup lang="ts">

import {
    computed,
    watch,
} from "vue";

import AppIcon
from "./AppIcon.vue";

const props = withDefaults(

    defineProps<{

        visible: boolean;

        title: string;

        message?: string;

        variant?:
            | "success"
            | "error"
            | "warning"
            | "info";

        duration?: number;

    }>(),

    {

        variant: "info",

        duration: 4000,

    },

);

const emit = defineEmits<{

    (
        event: "update:visible",
        value: boolean,
    ): void;

}>();

const icon = computed(() => {

    switch (props.variant) {

        case "success":
            return "check-circle";

        case "error":
            return "circle-x";

        case "warning":
            return "triangle-alert";

        default:
            return "info";

    }

});

watch(

    () => props.visible,

    value => {

        if (!value) {

            return;

        }

        window.setTimeout(

            close,

            props.duration,

        );

    },

);

function close() {

    emit(

        "update:visible",

        false,

    );

}

</script>

<style scoped>

.toast{

    position:fixed;

    top:24px;

    right:24px;

    width:380px;

    max-width:calc(100vw - 32px);

    display:flex;

    align-items:flex-start;

    gap:1rem;

    padding:1rem 1.25rem;

    border-radius:18px;

    background:white;

    border:1px solid #e2e8f0;

    box-shadow:

        0 20px 40px rgba(15,23,42,.12);

    z-index:99999;

}

.icon{

    display:flex;

    align-items:center;

    justify-content:center;

    width:40px;

    height:40px;

    border-radius:12px;

    flex-shrink:0;

}

.content{

    flex:1;

    display:flex;

    flex-direction:column;

    gap:.35rem;

}

.content strong{

    color:#0f172a;

    font-size:.95rem;

}

.content span{

    color:#64748b;

    line-height:1.5;

    font-size:.9rem;

}

.close-button{

    border:none;

    background:none;

    cursor:pointer;

    color:#94a3b8;

    font-size:1.2rem;

}

.success .icon{

    background:#dcfce7;

    color:#16a34a;

}

.error .icon{

    background:#fee2e2;

    color:#dc2626;

}

.warning .icon{

    background:#fef3c7;

    color:#d97706;

}

.info .icon{

    background:#dbeafe;

    color:#2563eb;

}

.toast-enter-active,

.toast-leave-active{

    transition:.3s;

}

.toast-enter-from,

.toast-leave-to{

    opacity:0;

    transform:translateX(80px);

}

@media(max-width:768px){

    .toast{

        left:16px;

        right:16px;

        width:auto;

        top:16px;

    }

}

</style>