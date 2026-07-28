# Domain Blueprint

## Objetivo

Este documento define a estrutura interna dos agregados do domínio do Personal Finance.

Para cada agregado são especificados:

- Responsabilidade
- Invariantes
- Entidades
- Value Objects
- Serviços
- Eventos
- Repositórios
- Casos de Uso

Este documento serve como referência para a implementação da camada de domínio.

---

# Aggregate: User

## Responsabilidade

Representar o proprietário de todas as informações financeiras.

## Entidades

- User

## Value Objects

- Email
- PasswordHash

## Invariantes

- Email único
- Senha sempre armazenada como hash
- Usuário ativo para autenticação

## Eventos

- UserRegistered
- UserUpdated
- PasswordChanged

## Repositório

- UserRepository

## Casos de Uso

- RegisterUser
- AuthenticateUser
- UpdateProfile

---

# Aggregate: Account

## Responsabilidade

Representar locais onde o dinheiro é armazenado.

## Entidade Principal

Account

## Atributos

- id
- userId
- name
- type
- initialBalance
- currentBalance
- currency
- active

## Value Objects

- Money
- Balance

## Invariantes

- saldo nunca nulo
- moeda obrigatória
- pertence a um único usuário

## Eventos

- AccountCreated
- AccountClosed
- BalanceAdjusted

## Casos de Uso

- CreateAccount
- UpdateAccount
- CloseAccount

---

# Aggregate: CreditCard

## Responsabilidade

Representar cartões de crédito.

## Entidade Principal

CreditCard

## Entidades Internas

Invoice

Purchase

Installment

## Value Objects

- CreditLimit
- DueDate
- ClosingDate

## Invariantes

- limite positivo
- fechamento obrigatório
- vencimento obrigatório

## Eventos

- CreditCardRegistered
- PurchaseRegistered
- InvoiceClosed
- InvoicePaid

## Casos de Uso

- RegisterCreditCard
- RegisterPurchase
- PayInvoice

---

# Aggregate: Loan

## Responsabilidade

Representar empréstimos.

## Atributos

- principal
- balance
- interestRate
- installmentValue
- installments

## Eventos

- LoanRegistered
- InstallmentPaid
- LoanSettled

## Casos de Uso

- RegisterLoan
- PayLoanInstallment

---

# Aggregate: Financing

Mesmo comportamento de Loan.

Especialização para aquisição de bens.

---

# Aggregate: Asset

## Responsabilidade

Representar patrimônio.

## Exemplos

- imóvel
- veículo
- ações
- fundos
- tesouro

## Eventos

- AssetRegistered
- AssetUpdated
- AssetDisposed

---

# Aggregate: FinancialGoal

## Responsabilidade

Representar objetivos financeiros.

## Atributos

- targetAmount
- currentAmount
- deadline

## Eventos

- GoalCreated
- GoalAchieved
- GoalUpdated

---

# Aggregate: FinancialEvent

## Responsabilidade

Representar qualquer fato financeiro.

Este é o principal agregado do domínio.

---

## Atributos

- id
- userId
- accountId
- categoryId
- date
- amount
- description
- status
- origin
- referenceId

---

## Tipos

- IncomeEvent
- ExpenseEvent
- TransferEvent
- PurchaseEvent
- InvoicePaymentEvent
- LoanPaymentEvent
- FinancingPaymentEvent
- RefundEvent
- AdjustmentEvent

---

## Invariantes

- valor obrigatório
- data obrigatória
- status obrigatório
- usuário obrigatório
- evento nunca muda de proprietário

---

## Status

- Planned
- Pending
- Confirmed
- Cancelled
- Reversed

---

## Eventos

- FinancialEventRecorded
- FinancialEventConfirmed
- FinancialEventCancelled
- FinancialEventReversed

---

## Casos de Uso

- RegisterIncome
- RegisterExpense
- RegisterTransfer
- ConfirmEvent
- CancelEvent
- ReverseEvent

---

# Aggregate: CashFlow

## Responsabilidade

Representar o fluxo diário.

Não é persistido obrigatoriamente.

Pode ser recalculado.

---

## Atributos

- date
- openingBalance
- totalIncome
- totalExpense
- closingBalance

---

## Eventos

- CashFlowCalculated

---

## Casos de Uso

- GenerateCashFlow

---

# Aggregate: FinancialDiagnosis

## Responsabilidade

Interpretar o fluxo financeiro.

---

## Indicadores

- Liquidez

- Endividamento

- Comprometimento da renda

- Dependência do cartão

- Reserva de emergência

- Patrimônio líquido

---

## Problemas Detectáveis

- Fluxo negativo

- Parcelamento excessivo

- Baixa liquidez

- Renda insuficiente

- Crescimento do endividamento

---

## Eventos

- DiagnosisGenerated

---

## Casos de Uso

- GenerateDiagnosis

---

# Aggregate: FinancialProjection

## Responsabilidade

Projetar cenários futuros.

---

## Entradas

- eventos previstos

- metas

- financiamentos

- empréstimos

- receitas recorrentes

---

## Saídas

- saldo futuro

- patrimônio futuro

- necessidade de caixa

---

## Eventos

- ProjectionGenerated

---

## Casos de Uso

- GenerateProjection

- SimulateScenario

---

# Aggregate: RecommendationPlan

## Responsabilidade

Transformar diagnósticos em ações.

---

## Estrutura

Recommendation

Priority

ExpectedImpact

Status

---

## Eventos

- RecommendationGenerated

- RecommendationAccepted

- RecommendationDismissed

---

## Casos de Uso

- GenerateRecommendations

- AcceptRecommendation

- RejectRecommendation

---

# Serviços de Domínio

PlanningService

Gera eventos previstos.

---

InvoiceGenerationService

Transforma compras parceladas em parcelas.

---

CashFlowEngine

Calcula fluxo de caixa.

---

DiagnosisEngine

Produz diagnósticos.

---

ProjectionEngine

Calcula projeções.

---

RecommendationEngine

Produz recomendações.

---

NetWorthEngine

Calcula patrimônio líquido.

---

# Fluxo Completo

User

↓

Planning

↓

Financial Events

↓

Cash Flow

↓

Diagnosis

↓

Projection

↓

Recommendation

↓

AI Assistant

---

# Princípios

- Todo comportamento pertence ao domínio.
- Entidades protegem suas invariantes.
- Serviços concentram regras entre agregados.
- O domínio é independente da infraestrutura.
- O banco de dados é apenas um mecanismo de persistência.
- APIs apenas expõem casos de uso.
- A IA nunca implementa regras financeiras.