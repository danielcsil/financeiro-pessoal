# Bounded Contexts

## Objetivo

Este documento detalha os bounded contexts do domínio do **Personal Finance**, definindo claramente as responsabilidades, agregados, entidades, objetos de valor, serviços de domínio, repositórios e casos de uso de cada contexto.

A separação em bounded contexts reduz o acoplamento, facilita a evolução do sistema e mantém cada módulo focado em um único conjunto de responsabilidades.

---

# Visão Geral

```
                    Personal Finance
                           │
 ┌──────────────┬──────────┼──────────┬──────────────┬──────────────┐
 │              │          │          │              │              │
 ▼              ▼          ▼          ▼              ▼              ▼
Identity   Planning   Execution   Analysis   Recommendation   AI Assistant
```

Cada contexto possui seu próprio modelo de domínio e comunica-se com os demais através de casos de uso e eventos de domínio.

---

# 1. Identity

## Responsabilidade

Gerenciar identidade e autenticação dos usuários.

Não possui qualquer regra financeira.

---

## Aggregate Root

- User

---

## Entidades

- User
- UserProfile
- Session

---

## Value Objects

- Email
- PasswordHash

---

## Repositórios

- UserRepository

---

## Casos de Uso

- RegisterUser
- AuthenticateUser
- RefreshToken
- UpdateProfile
- ChangePassword

---

## Eventos

- UserRegistered
- UserAuthenticated
- PasswordChanged

---

# 2. Financial Planning

## Responsabilidade

Representar a estrutura financeira do usuário.

Tudo o que existe antes das movimentações pertence aqui.

---

## Aggregate Roots

- Account
- CreditCard
- Loan
- Financing
- RecurringIncome
- RecurringExpense
- FinancialGoal
- Asset

---

## Entidades

### Account

Representa uma conta financeira.

### CreditCard

Representa um cartão de crédito.

### Loan

Representa empréstimos.

### Financing

Representa financiamentos.

### RecurringIncome

Receitas periódicas.

### RecurringExpense

Despesas periódicas.

### FinancialGoal

Objetivos financeiros.

### Asset

Patrimônio.

### Liability

Passivos financeiros.

---

## Value Objects

- Money
- InterestRate
- DueDate
- CreditLimit
- Recurrence
- Category

---

## Serviços de Domínio

### PlanningService

Responsável por gerar eventos financeiros previstos a partir dos cadastros.

Exemplos:

- salário do mês
- condomínio
- energia
- parcelas

---

## Repositórios

- AccountRepository
- CreditCardRepository
- LoanRepository
- FinancingRepository
- RecurringIncomeRepository
- RecurringExpenseRepository
- GoalRepository
- AssetRepository

---

## Casos de Uso

- CreateAccount
- CreateCreditCard
- RegisterLoan
- RegisterFinancing
- CreateRecurringIncome
- CreateRecurringExpense
- CreateGoal
- RegisterAsset

---

## Eventos

- AccountCreated
- CreditCardRegistered
- LoanRegistered
- FinancingRegistered
- RecurringIncomeCreated
- RecurringExpenseCreated
- GoalCreated

---

# 3. Financial Execution

## Responsabilidade

Representar tudo que realmente acontece na vida financeira.

Este é o núcleo do sistema.

---

## Aggregate Root

FinancialEvent

---

## Entidades

### FinancialEvent

Representa qualquer movimentação financeira.

Especializações conceituais:

- IncomeEvent
- ExpenseEvent
- TransferEvent
- CreditCardPurchase
- InvoicePayment
- RefundEvent
- AdjustmentEvent
- LoanPayment
- FinancingPayment

---

## Value Objects

- Money
- EventDate
- EventStatus
- PaymentMethod
- EventSource

---

## Serviços de Domínio

### EventGenerationService

Cria eventos previstos.

### InvoiceGenerationService

Gera parcelas futuras.

### ReconciliationService

Concilia movimentações importadas.

---

## Repositórios

- FinancialEventRepository

---

## Casos de Uso

- RegisterIncome
- RegisterExpense
- RegisterTransfer
- RegisterPurchase
- ConfirmPayment
- ReverseTransaction
- ImportInvoice
- ImportStatement

---

## Eventos

- FinancialEventRecorded
- PurchaseRegistered
- InvoiceImported
- StatementImported
- PaymentConfirmed
- RefundProcessed

---

# 4. Financial Analysis

## Responsabilidade

Transformar movimentações financeiras em conhecimento.

---

## Aggregate Roots

- CashFlow
- FinancialDiagnosis
- FinancialProjection

---

## Entidades

### CashFlow

Fluxo de caixa diário.

### FinancialDiagnosis

Diagnóstico financeiro.

### FinancialProjection

Projeções futuras.

### FinancialHealth

Indicadores financeiros.

---

## Value Objects

- FinancialScore
- LiquidityIndex
- DebtRatio

---

## Serviços de Domínio

### CashFlowEngine

Calcula o fluxo de caixa.

### ProjectionEngine

Calcula cenários futuros.

### DiagnosisEngine

Identifica problemas financeiros.

---

## Repositórios

Opcional.

Os resultados podem ser recalculados ou persistidos conforme necessidade.

---

## Casos de Uso

- GenerateCashFlow
- GenerateDiagnosis
- GenerateProjection
- CalculateNetWorth

---

## Eventos

- CashFlowCalculated
- DiagnosisGenerated
- ProjectionGenerated

---

# 5. Recommendation

## Responsabilidade

Gerar ações para melhorar a vida financeira.

---

## Aggregate Root

RecommendationPlan

---

## Entidades

- Recommendation
- RecommendationPlan
- Alert
- Opportunity

---

## Serviços de Domínio

### RecommendationEngine

Recebe diagnósticos e produz recomendações.

---

## Casos de Uso

- GenerateRecommendations
- PrioritizeRecommendations
- DismissRecommendation

---

## Eventos

- RecommendationGenerated
- AlertRaised
- RecommendationAccepted

---

# 6. AI Assistant

## Responsabilidade

Explicar a situação financeira ao usuário utilizando linguagem natural.

A IA nunca implementa regras financeiras.

Ela consulta os resultados produzidos pelos outros contextos.

---

## Serviços

### FinancialAssistant

Interface conversacional.

### PromptBuilder

Constrói o contexto enviado ao LLM.

### ConversationHistory

Mantém histórico das interações.

---

## Casos de Uso

- ExplainDiagnosis
- ExplainCashFlow
- SimulateScenario
- AnswerFinancialQuestion

---

# Dependências entre Contextos

```
Identity
     │
     ▼
Planning
     │
     ▼
Execution
     │
     ▼
Analysis
     │
     ▼
Recommendation
     │
     ▼
AI Assistant
```

A comunicação deve ocorrer exclusivamente por:

- Casos de Uso
- Eventos de Domínio
- Interfaces

Nenhum contexto pode acessar diretamente as entidades internas de outro contexto.

---

# Organização dos Pacotes

```
src/domain
│
├── identity
│
├── planning
│
├── execution
│
├── analysis
│
├── recommendation
│
└── assistant
```

Cada contexto possuirá internamente sua própria estrutura:

```
context/
│
├── entities/
├── value_objects/
├── repositories/
├── services/
├── events/
├── exceptions/
└── enums/
```

---

# Princípios

- Um contexto possui uma única responsabilidade.
- Cada agregado protege suas invariantes.
- Serviços de domínio concentram regras que envolvem múltiplas entidades.
- A comunicação entre contextos ocorre apenas por contratos explícitos.
- O domínio permanece totalmente independente de banco de dados, APIs e frameworks.