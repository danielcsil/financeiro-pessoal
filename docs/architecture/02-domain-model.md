# Modelo Conceitual do Domínio

## Objetivo

O **Personal Finance** é um sistema de inteligência financeira pessoal cujo objetivo é compreender a realidade financeira do usuário, explicar as causas dos problemas de fluxo de caixa, projetar cenários futuros e recomendar ações para melhorar sua saúde financeira.

Diferentemente de um sistema tradicional de controle financeiro, o foco não está no registro de receitas e despesas, mas na transformação desses dados em conhecimento para apoiar a tomada de decisão.

---

# Visão Geral do Domínio

O domínio é organizado em torno do ciclo natural da gestão financeira.

```text
                 Usuário
                     │
                     ▼
        Planejamento Financeiro
                     │
                     ▼
      Geração de Eventos Financeiros
                     │
                     ▼
         Fluxo de Caixa Diário
                     │
                     ▼
      Diagnóstico Financeiro
                     │
                     ▼
     Motor de Recomendações
                     │
                     ▼
        Assistente Financeiro IA
```

O cadastro não representa o objetivo do sistema.

Ele apenas fornece as informações necessárias para que o restante do domínio produza análises, diagnósticos e recomendações.

---

# Bounded Contexts

O domínio está dividido em seis grandes contextos.

## Identity

Responsável pela autenticação e gerenciamento do usuário.

### Entidades

- User
- UserProfile
- Session

---

## Financial Planning

Representa toda a estrutura financeira planejada pelo usuário.

### Entidades

- Account
- CreditCard
- Loan
- Financing
- RecurringIncome
- RecurringExpense
- FinancialGoal
- Asset
- Liability
- Category

Esse contexto descreve compromissos financeiros.

Nenhuma dessas entidades representa movimentações financeiras.

---

## Financial Execution

Representa tudo aquilo que realmente aconteceu.

O Aggregate Root desse contexto é:

- FinancialEvent

Todo fato financeiro é modelado como um evento.

Exemplos:

- salário recebido
- compra no cartão
- pagamento da fatura
- PIX
- estorno
- amortização
- transferência

---

## Financial Analysis

Recebe os eventos financeiros e produz conhecimento.

Principais entidades:

- CashFlow
- FinancialDiagnosis
- FinancialProjection
- FinancialIndicator
- FinancialHealth

---

## Recommendation

Responsável por gerar ações recomendadas ao usuário.

Entidades:

- Recommendation
- RecommendationPlan
- Alert
- Opportunity

---

## AI Assistant

Representa o agente financeiro inteligente.

A IA não realiza cálculos financeiros.

Ela interpreta os resultados produzidos pelo domínio e os apresenta ao usuário em linguagem natural.

---

# Aggregate Roots

## Identity

- User

## Planning

- Account
- CreditCard
- Loan
- Financing
- RecurringIncome
- RecurringExpense
- FinancialGoal
- Asset

## Execution

- FinancialEvent

## Analysis

- CashFlow
- FinancialDiagnosis
- FinancialProjection

## Recommendation

- RecommendationPlan

---

# Entidades

## User

Representa o proprietário dos dados financeiros.

---

## Account

Representa contas financeiras.

Exemplos:

- Conta Corrente
- Conta Digital
- Carteira
- Poupança

---

## CreditCard

Representa um cartão de crédito.

Responsável por:

- limite
- fechamento
- vencimento
- compras
- parcelas

---

## Loan

Representa empréstimos.

---

## Financing

Representa financiamentos.

---

## RecurringIncome

Representa receitas previstas.

Exemplos:

- salário
- aluguel
- aposentadoria

---

## RecurringExpense

Representa despesas recorrentes.

Exemplos:

- condomínio
- energia
- internet
- escola
- plano de saúde

---

## FinancialGoal

Representa objetivos financeiros.

Exemplos:

- reserva de emergência
- viagem
- quitar financiamento

---

## Asset

Representa patrimônio.

Exemplos:

- imóvel
- veículo
- investimentos

---

## Liability

Representa obrigações financeiras.

Exemplos:

- empréstimos
- financiamentos
- cartões

---

## FinancialEvent

É o núcleo do domínio.

Representa qualquer fato financeiro.

Exemplos:

- recebimento
- pagamento
- compra
- estorno
- amortização
- rendimento

Todo evento possui:

- data
- valor
- origem
- destino
- categoria
- status

---

## CashFlow

Representa a evolução do caixa.

Não armazena movimentações.

É calculado a partir dos eventos financeiros.

---

## FinancialDiagnosis

Explica a situação financeira do usuário.

Exemplos:

- excesso de parcelamentos
- fluxo negativo
- cartão utilizado como extensão da conta
- despesas variáveis elevadas

---

## RecommendationPlan

Representa um plano de ação para melhorar a saúde financeira.

---

# Value Objects

Os seguintes conceitos são objetos de valor.

- Money
- Percentage
- Installment
- InterestRate
- DueDate
- Recurrence
- Period
- Category
- PaymentMethod
- CreditLimit
- Balance

---

# Domain Events

## Planning

- RecurringExpenseCreated
- RecurringIncomeCreated
- GoalCreated
- LoanRegistered
- CardRegistered

---

## Execution

- FinancialEventRecorded
- PurchaseRegistered
- InvoiceImported
- PaymentConfirmed
- TransferCompleted
- RefundProcessed

---

## Analysis

- CashFlowCalculated
- DiagnosisGenerated
- ProjectionUpdated

---

## Recommendation

- RecommendationGenerated
- AlertRaised
- RiskDetected

---

# Relacionamento entre os Contextos

```text
                        User
                          │
     ┌───────────────┬────┴───────────────┐
     ▼               ▼                    ▼
 Accounts      CreditCards          FinancialGoals
     │               │                    │
     ├───────────────┴───────────────┐
     ▼                               ▼
RecurringIncome               RecurringExpense
             │                      │
             └────────────┬─────────┘
                          ▼
                  FinancialEvent
                          │
          ┌───────────────┼────────────────┐
          ▼               ▼                ▼
      CashFlow     FinancialDiagnosis   Projection
          │               │                │
          └───────────────┼────────────────┘
                          ▼
                 RecommendationPlan
                          │
                          ▼
                    AI Assistant
```

---

# Princípios Arquiteturais

O domínio foi organizado segundo os seguintes princípios:

- o cadastro não é o objetivo do sistema;
- toda movimentação financeira é representada por eventos;
- o fluxo de caixa é derivado dos eventos;
- diagnósticos são produzidos a partir do fluxo de caixa;
- recomendações são produzidas a partir dos diagnósticos;
- a IA interpreta o conhecimento produzido pelo domínio, não executa regras de negócio.

Essa organização coloca a inteligência financeira no centro da aplicação e mantém o domínio independente de tecnologias, interfaces e mecanismos de persistência.