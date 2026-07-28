# Sistema Financeiro Pessoal

# Glossário

## Objetivo

Este documento reúne os principais termos utilizados no domínio do **Personal Finance**.

Seu objetivo é padronizar a linguagem utilizada entre desenvolvedores, analistas e usuários do sistema, garantindo consistência na documentação e na implementação.

Todos os nomes utilizados no código devem seguir este glossário.

---

## Account

Representa um local onde o usuário mantém recursos financeiros.

Exemplos:

- Conta Corrente
- Conta Digital
- Carteira
- Poupança
- Conta Internacional

---

## Asset

Representa um bem ou investimento pertencente ao usuário.

Exemplos:

- Imóvel
- Veículo
- Ações
- Tesouro Direto

---

## Balance

Representa o saldo atual de uma conta.

Sempre é representado pelo Value Object `Money`.

---

## Budget

Representa o planejamento financeiro para um determinado período.

Pode estabelecer limites de gastos, metas de economia e distribuição de receitas.

---

## Category

Representa a classificação de um lançamento ou evento financeiro.

Exemplos:

- Alimentação
- Moradia
- Transporte
- Educação
- Saúde

---

## Credit Card

Representa um cartão de crédito.

Não possui saldo próprio.

Seu objetivo é registrar despesas que serão consolidadas em uma fatura.

---

## Domain Service

Objeto responsável por executar regras de negócio que envolvem múltiplas entidades ou agregados.

---

## Entity

Objeto do domínio que possui identidade própria ao longo do tempo.

---

## Expense

Representa uma saída de recursos financeiros.

---

## Financial Diagnosis

Representa a análise da situação financeira do usuário em determinado momento.

É produzido a partir dos eventos financeiros registrados.

---

## Financial Event

Representa qualquer fato financeiro que impacte ou venha a impactar o fluxo de caixa.

Exemplos:

- Receita
- Despesa
- Transferência
- Pagamento
- Compra
- Estorno
- Juros
- Rendimento

É o principal conceito do domínio.

---

## Financial Goal

Representa um objetivo financeiro definido pelo usuário.

Exemplos:

- Criar reserva de emergência
- Comprar um veículo
- Quitar um financiamento

---

## Financial Projection

Representa uma simulação da evolução financeira baseada em eventos previstos e históricos.

---

## Income

Representa uma entrada de recursos financeiros.

---

## Installment

Representa uma parcela pertencente a uma compra, empréstimo ou financiamento.

Cada parcela possui seu próprio ciclo de vida.

---

## Invoice

Representa a fatura de um cartão de crédito.

Agrupa despesas realizadas durante um período.

---

## Liability

Representa uma obrigação financeira do usuário.

Exemplos:

- Empréstimos
- Financiamentos
- Dívidas

---

## Money

Value Object responsável por representar valores monetários com precisão decimal.

---

## Recommendation

Representa uma sugestão produzida pelo sistema para melhorar a saúde financeira do usuário.

---

## Repository

Abstração responsável pela persistência dos agregados do domínio.

Nunca contém regras de negócio.

---

## Recurring Expense

Representa uma despesa recorrente planejada.

Exemplos:

- Aluguel
- Internet
- Academia

---

## Recurring Income

Representa uma receita recorrente planejada.

Exemplos:

- Salário
- Aluguel recebido
- Bolsa de estudos

---

## Transfer

Representa uma movimentação entre duas contas.

Possui um evento de saída e um evento correspondente de entrada.

---

## Use Case

Representa uma ação executada pelo usuário através do sistema.

Coordena a execução das regras de negócio sem implementá-las.

---

## Value Object

Objeto imutável identificado apenas pelos seus atributos.

Não possui identidade própria.