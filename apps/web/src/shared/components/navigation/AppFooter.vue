<script setup lang="ts">
const currentYear = new Date().getFullYear();
</script>

<template>
  <footer class="footer">
    <div class="footer__container">

      <div class="footer__brand">
        <h3>Financial Advisor</h3>

        <p>
          Organize suas finanças, elimine dívidas e tome decisões
          financeiras com mais segurança.
        </p>
      </div>

      <div class="footer__links">

        <div class="footer__column">
          <h4>Produto</h4>

          <RouterLink to="/">
            Início
          </RouterLink>

          <RouterLink to="/features">
            Funcionalidades
          </RouterLink>

          <RouterLink to="/pricing">
            Planos
          </RouterLink>
        </div>

        <div class="footer__column">
          <h4>Empresa</h4>

          <RouterLink to="/about">
            Sobre
          </RouterLink>

          <RouterLink to="/contact">
            Contato
          </RouterLink>

          <RouterLink to="/privacy">
            Privacidade
          </RouterLink>
        </div>

      </div>

    </div>

    <div class="footer__bottom">

      © {{ currentYear }}
      Financial Advisor.
      Todos os direitos reservados.

    </div>

  </footer>
</template>

<style scoped>

.footer{

    background:var(--color-surface);

    border-top:1px solid var(--color-border);

    margin-top:auto;

}

.footer__container{

    max-width:1280px;

    margin:0 auto;

    padding:4rem 2rem;

    display:grid;

    grid-template-columns:2fr 1fr;

    gap:4rem;

}

.footer__brand h3{

    margin-bottom:1rem;

    color:var(--color-primary);

}

.footer__brand p{

    color:var(--color-text-secondary);

    line-height:1.7;

    max-width:420px;

}

.footer__links{

    display:flex;

    justify-content:space-between;

    gap:3rem;

}

.footer__column{

    display:flex;

    flex-direction:column;

    gap:.75rem;

}

.footer__column h4{

    margin-bottom:.75rem;

}

.footer__column a{

    text-decoration:none;

    color:var(--color-text-secondary);

    transition:.2s;

}

.footer__column a:hover{

    color:var(--color-primary);

}

.footer__bottom{

    border-top:1px solid var(--color-border);

    padding:1.5rem;

    text-align:center;

    color:var(--color-text-secondary);

    font-size:.9rem;

}

@media(max-width:900px){

.footer__container{

grid-template-columns:1fr;

}

.footer__links{

flex-direction:column;

gap:2rem;

}

}

</style>