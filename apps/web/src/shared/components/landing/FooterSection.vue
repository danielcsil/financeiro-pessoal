<template>
    <footer class="footer">

        <div class="landing-container">

            <div class="footer-grid">

                <div class="footer-brand">

                    <RouterLink
                        to="/"
                        class="footer-logo"
                    >
                        <svg
                            class="footer-logo__icon"
                            viewBox="0 0 32 32"
                            xmlns="http://www.w3.org/2000/svg"
                            aria-hidden="true"
                        >
                            <!-- Base -->
                            <path
                                d="M4 28H28"
                                stroke="currentColor"
                                stroke-width="3"
                                stroke-linecap="round"
                            />

                            <!-- Barras -->
                            <rect
                                x="6"
                                y="17"
                                width="5"
                                height="9"
                                rx="1.5"
                                fill="#60A5FA"
                            />

                            <rect
                                x="13.5"
                                y="10"
                                width="5"
                                height="16"
                                rx="1.5"
                                fill="#3B82F6"
                            />

                            <rect
                                x="21"
                                y="4"
                                width="5"
                                height="22"
                                rx="1.5"
                                fill="currentColor"
                            />
                        </svg>

                        <span class="footer-logo__text">
                            Personal Finance
                        </span>
                    </RouterLink>

                    <p>
                        Uma plataforma moderna para controlar receitas,
                        despesas, cartões, patrimônio, investimentos e fluxo de
                        caixa, utilizando Inteligência Artificial para apoiar
                        decisões financeiras.
                    </p>

                </div>

                <div class="footer-column">

                    <h4>Produto</h4>

                    <RouterLink to="/">
                        Início
                    </RouterLink>

                    <RouterLink to="/register">
                        Criar Conta
                    </RouterLink>

                    <RouterLink to="/login">
                        Entrar
                    </RouterLink>

                    <a href="#">
                        Funcionalidades
                    </a>

                </div>

                <div class="footer-column">

                    <h4>Recursos</h4>

                    <a href="#">
                        Documentação
                    </a>

                    <a href="#">
                        API
                    </a>

                    <a href="#">
                        Roadmap
                    </a>

                    <a href="#">
                        Changelog
                    </a>

                </div>

                <div class="footer-column">

                    <h4>Suporte</h4>

                    <a href="#">
                        Central de Ajuda
                    </a>

                    <a href="#">
                        FAQ
                    </a>

                    <a href="#">
                        Contato
                    </a>

                    <a href="#">
                        Política de Privacidade
                    </a>

                </div>

            </div>

            <div class="footer-bottom">

                <p>
                    © {{ year }} Personal Finance.
                    Todos os direitos reservados.
                </p>

                <div class="socials">

                    <a href="#">
                        GitHub
                    </a>

                    <a href="#">
                        LinkedIn
                    </a>

                    <a href="#">
                        E-mail
                    </a>

                </div>

            </div>

        </div>

    </footer>
</template>

<script setup lang="ts">
import { RouterLink } from "vue-router";

const year = new Date().getFullYear();
</script>

<style scoped>

.footer{

    background:#08111F;

    color:#CBD5E1;

    padding:5rem 0 2rem;

}

.footer-grid{

    display:grid;

    grid-template-columns:2fr 1fr 1fr 1fr;

    gap:4rem;

}

.footer-brand p{

    margin-top:1.5rem;

    line-height:1.9;

    max-width:420px;

}

/* ---------------------------------------------------------------- */
/* Logo */
/* ---------------------------------------------------------------- */

.footer-logo{

    display:flex;

    align-items:center;

    gap:.85rem;

    text-decoration:none;

    color:white;

    font-size:1.35rem;

    font-weight:700;

}

.footer-logo__icon{

    width:36px;
    height:36px;

    display:block;

    flex-shrink:0;

}

.footer-logo__text{

    color:white;

    font-size:1.45rem;

    font-weight:700;

    line-height:1;

    white-space:nowrap;

}

/* ---------------------------------------------------------------- */

.footer-column{

    display:flex;

    flex-direction:column;

    gap:1rem;

}

.footer-column h4{

    color:white;

    margin-bottom:.5rem;

}

.footer-column a{

    color:#CBD5E1;

    text-decoration:none;

    transition:.25s;

}

.footer-column a:hover{

    color:white;

}

.footer-bottom{

    margin-top:4rem;

    padding-top:2rem;

    border-top:1px solid rgba(255,255,255,.08);

    display:flex;

    justify-content:space-between;

    align-items:center;

    flex-wrap:wrap;

    gap:1rem;

}

.socials{

    display:flex;

    gap:1.5rem;

}

.socials a{

    color:#CBD5E1;

    text-decoration:none;

}

.socials a:hover{

    color:white;

}

@media(max-width:980px){

.footer-grid{

    grid-template-columns:1fr 1fr;

}

}

@media(max-width:640px){

.footer-grid{

    grid-template-columns:1fr;

}

.footer-bottom{

    flex-direction:column;

    align-items:flex-start;

}

}

</style>