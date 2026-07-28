# Ubiquitous Language

## Objetivo

Este documento define a **Linguagem Ubíqua (Ubiquitous Language)** do domínio do **Personal Finance**.

Todos os desenvolvedores, documentação, APIs, testes, banco de dados e interface do usuário devem utilizar os mesmos termos com o mesmo significado.

A existência de múltiplos nomes para o mesmo conceito ou do mesmo nome para conceitos diferentes gera inconsistências, aumenta a complexidade do código e dificulta a evolução do sistema.

---

# Princípios

- Um conceito possui um único nome.
- Um nome representa apenas um conceito.
- O código deve refletir a linguagem do negócio.
- A interface deve utilizar os mesmos termos do domínio.
- Evitar sinônimos.

---

# Glossário

## User

Pessoa proprietária de toda a informação financeira.

Não existem movimentações compartilhadas entre usuários.

---

## Account

Local onde o dinheiro é armazenado.

Exemplos:

- Conta Corrente
- Conta Digital
- Carteira
- Poupança

Uma conta possui saldo.

Uma conta não possui parcelas.

---

## Credit Card

Instrumento de pagamento que gera compras e faturas.

Um cartão possui:

- limite
- fechamento
- vencimento
- compras
- parcelas
- faturas

---

## Financial Event

É qualquer fato financeiro ocorrido ou previsto.

Todo evento modifica ou poderá modificar o fluxo de caixa.

Exemplos:

- recebimento
- pagamento
- compra
- transferência
- estorno
- rendimento
- amortização

É a entidade central do domínio.

---

## Transaction

Representa uma operação financeira registrada.

No domínio do Personal Finance, toda Transaction corresponde a um Financial Event.

No código será utilizado apenas o termo:

FinancialEvent

O termo Transaction deve ser evitado.

---

## Cash Flow

Representa a evolução cronológica da disponibilidade financeira.

Não é um cadastro.

Não é uma tabela.

É um resultado calculado.

---

## Balance

Valor disponível em determinado instante.

Pode representar:

- saldo da conta
- saldo projetado
- saldo consolidado

---

## Asset

Bem ou investimento pertencente ao usuário.

Exemplos:

- imóvel
- veículo
- ações
- CDB
- Tesouro Direto

---

## Liability

Obrigação financeira.

Exemplos:

- empréstimo
- financiamento
- cartão
- dívida

---

## Financial Goal

Objetivo financeiro.

Exemplos:

- reserva de emergência
- comprar veículo
- quitar financiamento

---

## Recurring Income

Receita prevista que ocorre periodicamente.

Exemplos:

- salário
- aluguel
- aposentadoria

Não significa que foi recebida.

---

## Income Event

Recebimento efetivamente ocorrido.

Representa um FinancialEvent.

---

## Recurring Expense

Despesa prevista.

Exemplos:

- condomínio
- internet
- energia

Não representa pagamento.

---

## Expense Event

Pagamento efetivamente ocorrido.

Representa um FinancialEvent.

---

## Installment

Uma parcela.

Uma compra pode gerar diversas parcelas.

Cada parcela gera um evento financeiro independente.

---

## Invoice

Conjunto de parcelas pertencentes ao mesmo cartão.

Uma fatura pode possuir:

- compras
- ajustes
- juros
- multas

---

## Category

Classificação financeira.

Exemplos:

- Alimentação
- Saúde
- Transporte
- Educação

Categorias existem para classificação.

Nunca para controle de fluxo.

---

## Payment Method

Forma utilizada para realizar um pagamento.

Exemplos:

- PIX
- Débito
- Crédito
- Dinheiro
- TED

---

## Financial Diagnosis

Resultado da análise financeira.

Explica:

- problemas
- riscos
- causas

Não sugere ações.

---

## Recommendation

Ação sugerida.

Sempre deriva de um diagnóstico.

---

## Alert

Mensagem produzida automaticamente pelo sistema.

Exemplo:

"O limite do cartão será excedido em 12 dias."

---

## Projection

Simulação financeira futura.

Baseada em:

- eventos futuros
- eventos recorrentes
- metas
- financiamentos

---

## Simulation

Execução hipotética de cenários.

Exemplo:

"E se eu quitar o financiamento?"

---

## Financial Health

Estado geral das finanças.

É produzido pelo domínio.

Não é informado pelo usuário.

---

# Termos proibidos

Evitar estes nomes no código.

❌ Transaction

Usar:

FinancialEvent

---

❌ Receita

Usar:

RecurringIncome
ou

IncomeEvent

---

❌ Despesa

Usar:

RecurringExpense
ou

ExpenseEvent

---

❌ Conta Bancária

Usar:

Account

Uma conta pode representar carteira, dinheiro em espécie, conta digital ou conta corrente.

---

❌ Dívida

Usar:

Liability

---

❌ Extrato

Usar:

Statement

---

❌ Meta

Usar:

FinancialGoal

---

# Convenções de nomenclatura

## Entidades

Sempre substantivos.

Exemplo:

- Account
- CreditCard
- FinancialEvent

---

## Value Objects

Representam conceitos imutáveis.

Exemplo:

- Money
- InterestRate
- DueDate

---

## Casos de Uso

Sempre verbo + objeto.

Exemplos:

- RegisterPurchase
- GenerateCashFlow
- ImportStatement

---

## Eventos de Domínio

Sempre no passado.

Exemplos:

- PaymentConfirmed
- RecommendationGenerated
- InvoiceImported

---

## Repositórios

Sempre:

<Entity>Repository

Exemplo:

FinancialEventRepository

---

## Serviços de Domínio

Sempre terminados em Engine ou Service.

Exemplos:

- CashFlowEngine
- DiagnosisEngine
- RecommendationEngine

---

# Linguagem do Usuário x Linguagem do Domínio

| Interface | Domínio |
|------------|----------|
| Receita | Income Event |
| Despesa | Expense Event |
| Compra | Credit Card Purchase |
| Conta | Account |
| Cartão | Credit Card |
| Parcela | Installment |
| Fatura | Invoice |
| Saldo | Balance |
| Fluxo de Caixa | Cash Flow |
| Diagnóstico | Financial Diagnosis |
| Recomendação | Recommendation |

---

# Regra Fundamental

O domínio do Personal Finance não é orientado por CRUD.

Ele é orientado por eventos financeiros.

Toda informação financeira cadastrada existe para produzir eventos.

Os eventos produzem fluxo de caixa.

O fluxo produz diagnósticos.

Os diagnósticos produzem recomendações.

As recomendações são interpretadas pelo Assistente Financeiro IA.