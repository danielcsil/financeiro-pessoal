<template>
  <div class="card">
    <header
      v-if="$slots.header"
      class="card-header"
    >
      <slot name="header" />
    </header>

    <section class="card-body">
      <slot />
    </section>

    <footer
      v-if="$slots.footer"
      class="card-footer"
    >
      <slot name="footer" />
    </footer>
  </div>
</template>