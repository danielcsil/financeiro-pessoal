<script setup lang="ts">
/**
 * =============================================================================
 * Base Modal
 * =============================================================================
 *
 * Purpose
 * =============================================================================
 *
 * Reusable modal component used throughout the application.
 *
 * The modal is responsible only for presentation and interaction.
 * It does not contain any business logic.
 *
 * Features
 * --------
 *
 * • Click outside to close.
 *
 * • ESC key support.
 *
 * • Accessible structure.
 *
 * • Header / Body / Footer slots.
 *
 * • Responsive layout.
 *
 * • Teleport friendly.
 *
 * Architecture
 * =============================================================================
 *
 * Feature View
 *        │
 *        ▼
 *   BaseModal
 *        │
 *        ▼
 *     Content Slots
 */

import { onBeforeUnmount, onMounted } from "vue";

interface Props {
  /**
   * Controls whether the modal is visible.
   */
  open: boolean;

  /**
   * Width of the modal.
   */
  width?: string;

  /**
   * Prevent closing when clicking outside.
   */
  persistent?: boolean;
}

const props = withDefaults(
  defineProps<Props>(),
  {
    width: "640px",
    persistent: false,
  },
);

const emit = defineEmits<{
  close: [];
}>();

function close(): void {

  if (props.persistent) {
    return;
  }

  emit("close");

}

function onBackdropClick(): void {

  close();

}

function onEscape(
  event: KeyboardEvent,
): void {

  if (
    event.key === "Escape" &&
    props.open
  ) {
    close();
  }

}

onMounted(() => {

  window.addEventListener(
    "keydown",
    onEscape,
  );

});

onBeforeUnmount(() => {

  window.removeEventListener(
    "keydown",
    onEscape,
  );

});
</script>

<template>

<Teleport to="body">

  <Transition name="modal">

    <div
      v-if="open"
      class="modal"
    >

      <div
        class="modal__backdrop"
        @click="onBackdropClick"
      />

      <section
        class="modal__container"
        :style="{ maxWidth: width }"
        role="dialog"
        aria-modal="true"
        @click.stop
      >

        <header
          v-if="$slots.header"
          class="modal__header"
        >

          <slot name="header" />

        </header>

        <main class="modal__body">

          <slot />

        </main>

        <footer
          v-if="$slots.footer"
          class="modal__footer"
        >

          <slot name="footer" />

        </footer>

      </section>

    </div>

  </Transition>

</Teleport>

</template>

<style scoped>

.modal{

    position:fixed;

    inset:0;

    display:flex;

    justify-content:center;

    align-items:center;

    z-index:1000;

}

.modal__backdrop{

    position:absolute;

    inset:0;

    background:rgba(15,23,42,.55);

    backdrop-filter:blur(2px);

}

.modal__container{

    position:relative;

    width:95vw;

    max-height:90vh;

    overflow:auto;

    background:var(--color-surface);

    border-radius:1rem;

    box-shadow:0 20px 60px rgba(0,0,0,.25);

    display:flex;

    flex-direction:column;

}

.modal__header{

    padding:1.5rem;

    border-bottom:1px solid var(--color-border);

}

.modal__body{

    padding:1.5rem;

    overflow:auto;

}

.modal__footer{

    display:flex;

    justify-content:flex-end;

    gap:1rem;

    padding:1.5rem;

    border-top:1px solid var(--color-border);

}

.modal-enter-active,
.modal-leave-active{

    transition:opacity .2s ease;

}

.modal-enter-active .modal__container,
.modal-leave-active .modal__container{

    transition:
        transform .2s ease,
        opacity .2s ease;

}

.modal-enter-from,
.modal-leave-to{

    opacity:0;

}

.modal-enter-from .modal__container,
.modal-leave-to .modal__container{

    transform:translateY(20px);

    opacity:0;

}

@media (max-width:768px){

    .modal{

        align-items:flex-end;

    }

    .modal__container{

        width:100vw;

        max-width:100% !important;

        max-height:95vh;

        border-bottom-left-radius:0;

        border-bottom-right-radius:0;

    }

}

</style>