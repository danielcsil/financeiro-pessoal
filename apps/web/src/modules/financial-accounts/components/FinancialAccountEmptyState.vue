<template>
    <section class="empty-state">

        <div class="empty-icon">
            💼
        </div>

        <h2>
            Você ainda não possui contas financeiras
        </h2>

        <p>
            Cadastre sua primeira conta para começar a controlar seu
            patrimônio, acompanhar seu fluxo de caixa e organizar sua vida
            financeira.
        </p>

        <button
            class="create-button"
            type="button"
            @click="$emit('create')"
        >
            + Nova Conta
        </button>

    </section>
</template>

<script setup lang="ts">
defineEmits<{
    (
        event: "create",
    ): void;
}>();
</script>

<style scoped>

.empty-state {

    display: flex;

    flex-direction: column;

    align-items: center;

    justify-content: center;

    text-align: center;

    background: white;

    border: 2px dashed #dbe4f0;

    border-radius: 24px;

    padding: 5rem 2rem;

}

.empty-icon {

    width: 96px;

    height: 96px;

    border-radius: 24px;

    display: flex;

    align-items: center;

    justify-content: center;

    background: #eff6ff;

    font-size: 3rem;

    margin-bottom: 2rem;

}

h2 {

    margin: 0;

    font-size: 1.9rem;

    color: #0f172a;

    font-weight: 700;

}

p {

    max-width: 520px;

    margin: 1rem 0 2.5rem;

    color: #64748b;

    line-height: 1.7;

    font-size: 1rem;

}

.create-button {

    border: none;

    border-radius: 14px;

    background: #2563eb;

    color: white;

    font-size: 1rem;

    font-weight: 600;

    padding: .95rem 2rem;

    cursor: pointer;

    transition: all .25s;

}

.create-button:hover {

    background: #1d4ed8;

    transform: translateY(-2px);

    box-shadow: 0 12px 28px rgba(37,99,235,.25);

}

@media (max-width:768px){

    .empty-state{

        padding:3rem 1.5rem;

    }

    h2{

        font-size:1.5rem;

    }

    .empty-icon{

        width:72px;

        height:72px;

        font-size:2.3rem;

    }

}

</style>