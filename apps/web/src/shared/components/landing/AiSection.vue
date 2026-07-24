<template>
    <section class="landing-section ai-section">

        <div class="landing-container ai-grid">

            <div class="ai-content">

                <span class="section-badge">
                    Inteligência Artificial
                </span>

                <h2>
                    Um consultor financeiro disponível 24 horas por dia
                </h2>

                <p class="description">
                    O Personal Finance utiliza Inteligência Artificial para
                    analisar sua situação financeira, identificar padrões de
                    gastos e apresentar recomendações personalizadas para que
                    você tome melhores decisões.
                </p>

                <div class="features">

                    <div class="feature">
                        <div class="icon">
                            🧠
                        </div>

                        <div>
                            <h3>Análise Inteligente</h3>

                            <p>
                                Descubra automaticamente onde seu dinheiro está
                                sendo consumido.
                            </p>
                        </div>
                    </div>

                    <div class="feature">
                        <div class="icon">
                            📈
                        </div>

                        <div>
                            <h3>Projeções Futuras</h3>

                            <p>
                                Saiba como estará seu fluxo de caixa nas próximas
                                semanas e meses.
                            </p>
                        </div>
                    </div>

                    <div class="feature">
                        <div class="icon">
                            💡
                        </div>

                        <div>
                            <h3>Recomendações</h3>

                            <p>
                                Receba sugestões para economizar, quitar dívidas
                                e atingir suas metas mais rapidamente.
                            </p>
                        </div>
                    </div>

                </div>

            </div>

            <div class="ai-preview">

                <div class="chat-window">

                    <div class="chat-header">
                        Assistente Financeiro
                    </div>

                    <div class="message user">
                        Como posso economizar este mês?
                    </div>

                    <div class="message ai">
                        Você gastou 32% acima da média com alimentação. Reduzindo
                        esse valor em R$ 400,00 será possível manter saldo
                        positivo até o final do mês.
                    </div>

                    <div class="message user">
                        Posso comprar um notebook de R$ 4.500?
                    </div>

                    <div class="message ai">
                        Neste momento não é recomendado. A compra fará seu fluxo
                        de caixa ficar negativo em setembro. Aguarde mais dois
                        meses ou reduza o valor da entrada.
                    </div>

                </div>

            </div>

        </div>

    </section>
</template>

<script setup lang="ts">
</script>

<style scoped>

.ai-section{
    background:linear-gradient(
        180deg,
        var(--color-background-secondary),
        var(--color-background)
    );
}

.ai-grid{

    display:grid;
    grid-template-columns:1.1fr .9fr;

    gap:5rem;

    align-items:center;
}

.description{

    margin:2rem 0;

    color:var(--color-text-secondary);

    line-height:1.9;
}

.features{

    display:flex;

    flex-direction:column;

    gap:2rem;
}

.feature{

    display:flex;

    gap:1.25rem;

    align-items:flex-start;
}

.icon{

    width:60px;
    height:60px;

    display:flex;
    align-items:center;
    justify-content:center;

    border-radius:16px;

    background:rgba(37,99,235,.08);

    font-size:1.5rem;
}

.feature h3{

    margin-bottom:.4rem;

    color:var(--color-text-primary);
}

.feature p{

    color:var(--color-text-secondary);

    line-height:1.7;
}

.chat-window{

    background:white;

    border-radius:24px;

    overflow:hidden;

    box-shadow:var(--shadow-xl);

    border:1px solid var(--color-border);

}

.chat-header{

    padding:1.2rem 1.5rem;

    background:var(--color-primary);

    color:white;

    font-weight:700;
}

.message{

    margin:1rem;

    padding:1rem 1.25rem;

    border-radius:16px;

    line-height:1.7;

    max-width:85%;
}

.user{

    margin-left:auto;

    background:#E8F0FE;
}

.ai{

    background:#F8FAFC;
}

@media(max-width:960px){

.ai-grid{

grid-template-columns:1fr;

}

}

</style>