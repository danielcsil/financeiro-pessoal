<template>
    <footer class="footer">

        <div class="landing-container">

            <div class="footer-grid">

                <div class="footer-brand">

                    <RouterLink
                        to="/"
                        class="logo"
                    >
                        <div class="logo-icon">
                            PF
                        </div>

                        <span>Personal Finance</span>
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

.logo{

    display:flex;

    align-items:center;

    gap:1rem;

    text-decoration:none;

    color:white;

    font-size:1.3rem;

    font-weight:700;

}

.logo-icon{

    width:44px;
    height:44px;

    display:flex;
    align-items:center;
    justify-content:center;

    border-radius:12px;

    background:var(--color-primary);

}

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