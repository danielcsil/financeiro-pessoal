<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <div class="auth-layout">
    <!-- ====================================================== -->
    <!-- Painel Institucional -->
    <!-- ====================================================== -->

    <section class="auth-layout__left">
      <!-- Elementos decorativos -->
      <div class="bg-shape bg-shape--top"></div>
      <div class="bg-shape bg-shape--bottom"></div>

      <div class="bg-dots bg-dots--top"></div>
      <div class="bg-dots bg-dots--bottom"></div>

      <!-- Voltar -->

      <RouterLink
        to="/"
        class="back-home"
      >
        <span class="back-home__arrow">←</span>

        <span>Voltar para a Home</span>
      </RouterLink>

      <!-- Conteúdo -->

      <div class="brand">
        <!-- Logo -->

        <div class="brand__header">
          <svg
            class="brand__logo"
            viewBox="0 0 32 32"
            xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true"
          >
            <path
              d="M4 28H28"
              stroke="currentColor"
              stroke-width="3"
              stroke-linecap="round"
            />

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
              fill="#ffffff"
            />
          </svg>

          <div>
            <h1 class="brand__title">
              Personal Finance
            </h1>

            <span class="brand__subtitle">
              Gestão Financeira Inteligente
            </span>
          </div>
        </div>

        <!-- Texto -->

        <div class="brand__content">
          <h2>
            Sua vida financeira
            <br />
            em um único lugar.
          </h2>

          <p>
            Organize receitas, despesas, cartões,
            investimentos e acompanhe seu patrimônio
            através de uma plataforma moderna,
            segura e intuitiva.
          </p>
        </div>

        <!-- Benefícios -->

        <div class="features">
          <div class="feature">
            <div class="feature__icon">
              ✓
            </div>

            <span>
              Controle completo das suas contas.
            </span>
          </div>

          <div class="feature">
            <div class="feature__icon">
              ✓
            </div>

            <span>
              Fluxo de caixa projetado.
            </span>
          </div>

          <div class="feature">
            <div class="feature__icon">
              ✓
            </div>

            <span>
              Planejamento financeiro.
            </span>
          </div>

          <div class="feature">
            <div class="feature__icon">
              ✓
            </div>

            <span>
              Metas financeiras.
            </span>
          </div>

          <div class="feature">
            <div class="feature__icon">
              ✓
            </div>

            <span>
              Assistente Financeiro com IA.
            </span>
          </div>
        </div>
      </div>
    </section>

    <!-- ====================================================== -->
    <!-- Painel de autenticação -->
    <!-- ====================================================== -->

    <section class="auth-layout__right">
      <div class="auth-card">
        <RouterView />
      </div>
    </section>
  </div>
</template>

<style scoped>
  /* ==========================================================
    LAYOUT
  ========================================================== */

  .auth-layout {
    display: grid;
    grid-template-columns: minmax(760px, 1fr) 560px;
    min-height: 100vh;
    background: #f7f9fc;
    overflow: hidden;
  }

  /* ==========================================================
    PAINEL ESQUERDO
  ========================================================== */

  .auth-layout__left {
    position: relative;

    display: flex;
    justify-content: center;
    align-items: center;

    overflow: hidden;

    padding: 64px 72px;

    color: white;

    background:
      radial-gradient(
        circle at top left,
        rgba(255,255,255,.10),
        transparent 35%
      ),
      radial-gradient(
        circle at bottom right,
        rgba(255,255,255,.08),
        transparent 40%
      ),
      linear-gradient(
        135deg,
        #072B5B 0%,
        #0D4C97 55%,
        #1B64C7 100%
      );
  }

  /* ==========================================================
    FORMAS DECORATIVAS
  ========================================================== */

  .bg-shape {
    position: absolute;

    pointer-events: none;

    opacity: .12;
  }

  .bg-shape--top {

    width: 620px;
    height: 620px;

    top: -380px;
    right: -180px;

    border-radius: 50%;

    border: 90px solid rgba(255,255,255,.12);
  }

  .bg-shape--bottom {

    width: 760px;
    height: 760px;

    bottom: -520px;
    left: -140px;

    border-radius: 50%;

    border: 80px solid rgba(255,255,255,.08);
  }

  /* ==========================================================
    PONTOS DECORATIVOS
  ========================================================== */

  .bg-dots {
    position: absolute;

    width: 110px;
    height: 110px;

    opacity: .22;

    background-image:
      radial-gradient(
        rgba(255,255,255,.7) 1.8px,
        transparent 1.8px
      );

    background-size: 18px 18px;
  }

  .bg-dots--top {
    top: 72px;
    right: 72px;
  }

  .bg-dots--bottom {
    left: 56px;
    bottom: 56px;
  }

  /* ==========================================================
    BOTÃO HOME
  ========================================================== */

  .back-home {

    position: absolute;

    top: 36px;
    left: 44px;

    display: inline-flex;
    align-items: center;
    gap: 10px;

    color: rgba(255,255,255,.95);

    text-decoration: none;

    font-size: .98rem;
    font-weight: 600;

    transition:
      color .25s ease,
      transform .25s ease;
  }

  .back-home::after {

    content: "";

    position: absolute;

    left: 28px;
    bottom: -10px;

    width: 68px;
    height: 2px;

    border-radius: 999px;

    background: #3B82F6;

    transition: width .25s;
  }

  .back-home:hover {

    color: white;

    transform: translateX(-3px);
  }

  .back-home:hover::after {
    width: 105px;
  }

  .back-home__arrow {

    font-size: 1.15rem;

    line-height: 1;
  }

  /* ==========================================================
    CONTEÚDO
  ========================================================== */

  .brand {

    position: relative;

    z-index: 2;

    width: 100%;
    max-width: 620px;
  }

  /* ==========================================================
    LOGO
  ========================================================== */

  .brand__header {

    display: flex;
    align-items: center;

    gap: 22px;

    margin-bottom: 70px;
  }

  .brand__logo {

    width: 72px;
    height: 72px;

    flex-shrink: 0;

    color: white;

    filter: drop-shadow(
      0 8px 18px rgba(0,0,0,.18)
    );
  }

  .brand__title {

    margin: 0;

    font-size: 3rem;
    font-weight: 700;
    line-height: 1.05;

    letter-spacing: -.02em;

    color: white;
  }

  .brand__subtitle {

    display: inline-block;

    margin-top: 8px;

    color: #60A5FA;

    font-size: 1.18rem;

    font-weight: 600;
  }

  /* ==========================================================
    TEXTO
  ========================================================== */

  .brand__content {

    max-width: 620px;
  }

  .brand__content h2 {

    margin: 0;

    font-size: 4rem;

    line-height: 1.08;

    font-weight: 700;

    letter-spacing: -.03em;

    color: white;
  }

  .brand__content p {

    margin-top: 34px;

    max-width: 620px;

    font-size: 1.42rem;

    line-height: 1.75;

    color: rgba(255,255,255,.88);
  }

  /* ==========================================================
    BENEFÍCIOS
  ========================================================== */

  .features {

    margin-top: 70px;

    display: flex;
    flex-direction: column;

    gap: 22px;
  }

  .feature {

    display: flex;
    align-items: center;

    gap: 18px;
  }

  .feature__icon {

    width: 38px;
    height: 38px;

    display: flex;
    align-items: center;
    justify-content: center;

    flex-shrink: 0;

    border-radius: 50%;

    background: rgba(59,130,246,.95);

    color: white;

    font-weight: 700;

    box-shadow:
      0 10px 24px rgba(0,0,0,.18);
  }

  .feature span {

    font-size: 1.22rem;

    color: rgba(255,255,255,.96);

    line-height: 1.5;
  }

  /* ==========================================================
    PAINEL DIREITO
  ========================================================== */

  .auth-layout__right {
    display: flex;
    flex-direction: column;

    justify-content: center;
    align-items: center;

    position: relative;

    padding: 48px;

    background: linear-gradient(
      180deg,
      #fafcff 0%,
      #f2f6fb 100%
    );
  }

  /* ==========================================================
    CARD
  ========================================================== */

  .auth-card {
    width: 100%;
    max-width: 460px;

    position: relative;
    z-index: 2;

    padding: 48px;

    background: #ffffff;

    border-radius: 24px;

    border: 1px solid #e8eef5;

    box-shadow:
      0 30px 80px rgba(15, 76, 129, 0.10),
      0 12px 24px rgba(0, 0, 0, 0.05);

    animation: fadeInUp .45s ease;
  }

  /* ==========================================================
    ELEMENTOS INTERNOS DO ROUTERVIEW
  ========================================================== */

  :deep(h1) {
    margin: 0 0 10px;

    font-size: 2rem;
    font-weight: 700;

    color: #14304d;
  }

  :deep(.subtitle) {
    margin-bottom: 32px;

    color: #6b7280;

    font-size: .98rem;

    line-height: 1.6;
  }

  :deep(.form-group) {
    margin-bottom: 22px;
  }

  :deep(label) {
    display: block;

    margin-bottom: 8px;

    font-weight: 600;

    color: #334155;
  }

  :deep(input) {
    width: 100%;

    padding: 14px 16px;

    border: 1px solid #d9e2ec;

    border-radius: 12px;

    font-size: .95rem;

    transition:
      border-color .2s,
      box-shadow .2s;
  }

  :deep(input:focus) {
    outline: none;

    border-color: #3b82f6;

    box-shadow:
      0 0 0 4px rgba(59,130,246,.12);
  }

  :deep(input::placeholder) {
    color: #94a3b8;
  }

  :deep(.checkbox) {
    display: flex;
    align-items: flex-start;

    gap: 12px;

    margin: 24px 0;
  }

  :deep(.checkbox input) {
    width: 18px;
    height: 18px;

    margin-top: 2px;
  }

  :deep(.checkbox span) {
    line-height: 1.5;

    color: #475569;
  }

  :deep(.btn-primary) {
    width: 100%;

    padding: 15px;

    border: none;

    border-radius: 12px;

    background: linear-gradient(
      135deg,
      #2563eb,
      #1d4ed8
    );

    color: white;

    font-size: 1rem;

    font-weight: 600;

    cursor: pointer;

    transition:
      transform .2s,
      box-shadow .2s;
  }

  :deep(.btn-primary:hover) {
    transform: translateY(-2px);

    box-shadow:
      0 16px 34px rgba(37,99,235,.25);
  }

  :deep(.btn-primary:disabled) {
    cursor: not-allowed;

    opacity: .6;

    transform: none;

    box-shadow: none;
  }

  :deep(a) {
    color: #2563eb;

    text-decoration: none;

    font-weight: 600;
  }

  :deep(a:hover) {
    text-decoration: underline;
  }

  /* ==========================================================
    FOOTER
  ========================================================== */

  .auth-footer {
    margin-top: 32px;

    color: #64748b;

    font-size: .85rem;
  }

  /* ==========================================================
    ANIMAÇÕES
  ========================================================== */

  @keyframes fadeInUp {

    from {

      opacity: 0;

      transform:
        translateY(18px)
        scale(.98);
    }

    to {

      opacity: 1;

      transform:
        translateY(0)
        scale(1);
    }

  }

  /* ==========================================================
    RESPONSIVIDADE
  ========================================================== */

  @media (max-width: 1200px) {

    .auth-layout {
      grid-template-columns: minmax(520px, 1fr) 480px;
    }

    .brand__content h2 {
      font-size: 3.2rem;
    }

    .brand__content p {
      font-size: 1.15rem;
    }

  }

  @media (max-width: 1024px) {

    .auth-layout {
      grid-template-columns: 1fr;
    }

    .auth-layout__left {
      display: none;
    }

    .auth-layout__right {
      padding: 48px 24px;
    }

  }

  @media (max-width: 640px) {

    .auth-layout__right {
      padding: 20px;
    }

    .auth-card {
      padding: 32px 24px;

      border-radius: 18px;
    }

    :deep(h1) {
      font-size: 1.75rem;
    }

  }
</style>