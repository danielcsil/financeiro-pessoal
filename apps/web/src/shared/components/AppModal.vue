<template>

    <Teleport to="body">

        <Transition name="modal">

            <div
                v-if="modelValue"
                class="overlay"
                @click.self="close"
            >

                <section class="modal">

                    <!-- ================================================== -->
                    <!-- Header -->
                    <!-- ================================================== -->

                    <header
                        v-if="$slots.header || title"
                        class="modal-header"
                    >

                        <div>

                            <h2
                                v-if="title"
                                class="modal-title"
                            >
                                {{ title }}
                            </h2>

                            <p
                                v-if="subtitle"
                                class="modal-subtitle"
                            >
                                {{ subtitle }}
                            </p>

                            <slot name="header"/>

                        </div>

                        <button
                            class="close-button"
                            @click="close"
                        >
                            ✕
                        </button>

                    </header>

                    <!-- ================================================== -->
                    <!-- Body -->
                    <!-- ================================================== -->

                    <main class="modal-body">

                        <slot/>

                    </main>

                    <!-- ================================================== -->
                    <!-- Footer -->
                    <!-- ================================================== -->

                    <footer
                        v-if="$slots.footer"
                        class="modal-footer"
                    >

                        <slot name="footer"/>

                    </footer>

                </section>

            </div>

        </Transition>

    </Teleport>

</template>

<script setup lang="ts">

withDefaults(

    defineProps<{

        modelValue: boolean;

        title?: string;

        subtitle?: string;

        width?: string;

    }>(),

    {

        width: "900px",

    },

);

const emit = defineEmits<{

    (
        event: "update:modelValue",
        value: boolean,
    ): void;

}>();

function close() {

    emit(
        "update:modelValue",
        false,
    );

}

</script>

<style scoped>

.overlay{

    position:fixed;

    inset:0;

    z-index:9999;

    display:flex;

    justify-content:center;

    align-items:center;

    padding:2rem;

    background:rgba(15,23,42,.45);

    backdrop-filter:blur(8px);

}

.modal{

    width:min(v-bind(width),100%);

    max-height:90vh;

    overflow:hidden;

    display:flex;

    flex-direction:column;

    background:white;

    border-radius:24px;

    box-shadow:

        0 40px 80px rgba(15,23,42,.20);

}

.modal-header{

    display:flex;

    justify-content:space-between;

    align-items:flex-start;

    gap:2rem;

    padding:2rem;

    border-bottom:1px solid #edf2f7;

}

.modal-title{

    margin:0;

    font-size:1.75rem;

    font-weight:700;

    color:#0f172a;

}

.modal-subtitle{

    margin-top:.5rem;

    color:#64748b;

    line-height:1.6;

}

.modal-body{

    flex:1;

    overflow:auto;

    padding:2rem;

}

.modal-footer{

    display:flex;

    justify-content:flex-end;

    gap:1rem;

    padding:1.5rem 2rem;

    border-top:1px solid #edf2f7;

}

.close-button{

    width:42px;

    height:42px;

    border:none;

    border-radius:12px;

    background:#f8fafc;

    color:#64748b;

    cursor:pointer;

    transition:.25s;

}

.close-button:hover{

    background:#e2e8f0;

    color:#0f172a;

}

.modal-enter-active,

.modal-leave-active{

    transition:.25s;

}

.modal-enter-from,

.modal-leave-to{

    opacity:0;

}

.modal-enter-from .modal,

.modal-leave-to .modal{

    transform:translateY(24px) scale(.97);

}

.modal-enter-active .modal,

.modal-leave-active .modal{

    transition:.25s;

}

@media(max-width:768px){

    .overlay{

        padding:1rem;

        align-items:flex-end;

    }

    .modal{

        width:100%;

        max-height:95vh;

        border-radius:24px 24px 0 0;

    }

    .modal-header{

        padding:1.5rem;

    }

    .modal-body{

        padding:1.5rem;

    }

    .modal-footer{

        padding:1.5rem;

        flex-direction:column-reverse;

    }

}

</style>