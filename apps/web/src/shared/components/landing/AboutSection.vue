<template>
  <section
    id="about"
    class="about-section"
  >
    <div class="about-container">

      <!-- Dashboard -->
      <div class="about-image">

        <div class="dashboard-preview">

          <img
              src="@/assets/images/hero-finance.png"
              alt="Dashboard do Personal Finance"
          />

        </div>

      </div>

      <!-- Texto -->
      <div class="about-content">

        <span class="section-badge">
          Controle financeiro inteligente
        </span>

        <h2 class="section-title">
          Muito mais do que uma planilha financeira
        </h2>

        <p class="section-description">
          O Personal Finance foi desenvolvido para centralizar toda a sua
          vida financeira em uma única plataforma. Em vez de utilizar
          diversas planilhas, aplicativos e anotações, você acompanha
          receitas, despesas, cartões, financiamentos, patrimônio,
          investimentos e metas em um ambiente moderno e intuitivo.
        </p>

        <p class="section-description">
          Com uma visão consolidada da sua situação financeira, fica muito
          mais fácil entender para onde seu dinheiro está indo, identificar
          oportunidades de economia e planejar um futuro financeiro mais
          seguro.
        </p>

        <div class="benefits">

          <div class="benefit">

            <div class="benefit-icon">
              💰
            </div>

            <div>

              <h3>Fluxo de Caixa</h3>

              <p>
                Acompanhe entradas, saídas e projeções futuras em tempo
                real.
              </p>

            </div>

          </div>

          <div class="benefit">

            <div class="benefit-icon">
              💳
            </div>

            <div>

              <h3>Cartões de Crédito</h3>

              <p>
                Controle limites, parcelas, vencimentos e gastos em um só
                lugar.
              </p>

            </div>

          </div>

          <div class="benefit">

            <div class="benefit-icon">
              📈
            </div>

            <div>

              <h3>Patrimônio</h3>

              <p>
                Visualize a evolução do seu patrimônio e acompanhe seu
                crescimento financeiro.
              </p>

            </div>

          </div>

          <div class="benefit">

            <div class="benefit-icon">
              🤖
            </div>

            <div>

              <h3>Inteligência Artificial</h3>

              <p>
                Receba recomendações personalizadas para melhorar sua saúde
                financeira.
              </p>

            </div>

          </div>

        </div>

      </div>

    </div>
  </section>
</template>

<script setup lang="ts">
</script>

<style scoped>

.about-section {

    padding:110px 0;

    background:white;

}

.about-container{

    max-width:1280px;

    margin:auto;

    display:grid;

    grid-template-columns:
        1fr
        1fr;

    gap:70px;

    align-items:center;

    padding:0 40px;

}

.about-image{

    display:flex;

    justify-content:center;

}

.dashboard-preview{

    width:100%;

    border-radius:24px;

    overflow:hidden;

    background:#ffffff;

    box-shadow:
        0 25px 60px rgba(0,0,0,.08);

}

.dashboard-preview img{

    width:100%;

    display:block;

}

.section-badge{

    display:inline-block;

    padding:8px 18px;

    background:#dbeafe;

    color:#2563eb;

    border-radius:999px;

    font-weight:600;

    margin-bottom:20px;

}

.section-title{

    font-size:42px;

    font-weight:800;

    color:var(--color-text-primary);

    line-height:1.2;

    margin-bottom:25px;

}

.section-description{

    color:var(--color-text-secondary);

    line-height:1.9;

    font-size:18px;

    margin-bottom:24px;

}

.benefits{

    display:grid;

    grid-template-columns:1fr;

    gap:24px;

    margin-top:40px;

}

.benefit{

    display:flex;

    gap:20px;

    align-items:flex-start;

}

.benefit-icon{

    width:56px;

    height:56px;

    border-radius:14px;

    background:#eff6ff;

    display:flex;

    align-items:center;

    justify-content:center;

    font-size:28px;

    flex-shrink:0;

}

.benefit h3{

    margin-bottom:8px;

    color:var(--color-text-primary);

    font-size:20px;

}

.benefit p{

    color:var(--color-text-secondary);

    line-height:1.7;

}

@media(max-width:1024px){

.about-container{

    grid-template-columns:1fr;

}

.about-image{

    order:2;

}

.about-content{

    order:1;

}

}

@media(max-width:768px){

.about-section{

    padding:70px 0;

}

.about-container{

    padding:0 20px;

}

.section-title{

    font-size:34px;

}

.section-description{

    font-size:17px;

}

.benefit{

    gap:16px;

}

}

</style>