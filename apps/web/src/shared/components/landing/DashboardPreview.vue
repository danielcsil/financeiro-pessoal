<template>
    <section class="landing-section dashboard-preview-section">
        <div class="landing-container">

            <div class="section-header">
                <span class="section-badge">
                    Dashboard Inteligente
                </span>

                <h2>
                    Visualize sua vida financeira em segundos
                </h2>

                <p>
                    O painel principal concentra as informações mais importantes
                    para que você saiba exatamente como está sua situação
                    financeira hoje e como ela ficará nos próximos meses.
                </p>
            </div>

            <div class="dashboard-preview">

                <img
                    src="@/assets/images/hero-finance.png"
                    alt="Dashboard do Personal Finance"
                />

            </div>

            <div class="dashboard-highlights">

                <div class="highlight-card">
                    <span class="number">01</span>

                    <h3>Fluxo de Caixa</h3>

                    <p>
                        Descubra antecipadamente quando faltará dinheiro e
                        organize seu orçamento.
                    </p>
                </div>

                <div class="highlight-card">
                    <span class="number">02</span>

                    <h3>Cartões</h3>

                    <p>
                        Controle limites, parcelamentos e faturas futuras em um
                        único lugar.
                    </p>
                </div>

                <div class="highlight-card">
                    <span class="number">03</span>

                    <h3>IA Financeira</h3>

                    <p>
                        Receba recomendações inteligentes para reduzir gastos e
                        melhorar seu planejamento.
                    </p>
                </div>

            </div>

        </div>
    </section>
</template>

<script setup lang="ts">
</script>

<style scoped>

.dashboard-preview-section{
    background:var(--color-background);
}

.section-header{
    max-width:760px;
    margin:0 auto 4rem;
    text-align:center;
}

.dashboard-preview{

    display:flex;
    justify-content:center;

    margin-bottom:5rem;
}

.dashboard-preview img{

    width:100%;
    max-width:1280px;

    display:block;

    transition:transform .35s ease;

}

.dashboard-preview img:hover{

    transform:translateY(-6px);

}

.dashboard-highlights{

    display:grid;

    grid-template-columns:repeat(3,1fr);

    gap:2rem;
}

.highlight-card{

    padding:2rem;

    background:var(--color-surface);

    border:1px solid var(--color-border);

    border-radius:20px;

    transition:.25s;
}

.highlight-card:hover{

    transform:translateY(-6px);

    border-color:var(--color-primary);

    box-shadow:var(--shadow-lg);

}

.number{

    display:inline-flex;

    width:48px;
    height:48px;

    align-items:center;
    justify-content:center;

    margin-bottom:1.5rem;

    border-radius:50%;

    font-weight:700;

    color:white;

    background:var(--color-primary);

}

.highlight-card h3{

    margin-bottom:.8rem;

    color:var(--color-text-primary);

}

.highlight-card p{

    color:var(--color-text-secondary);

    line-height:1.8;

}

@media(max-width:900px){

.dashboard-highlights{

grid-template-columns:1fr;

}

}

</style>