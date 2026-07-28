# Modelo de Persistência

## Objetivo

Este documento define a estratégia de persistência do Personal Finance.

A persistência foi projetada para atender aos seguintes objetivos:

- preservar o histórico financeiro;
- permitir reconstrução completa do fluxo de caixa;
- suportar auditoria;
- suportar projeções futuras;
- evitar perda de informação;
- manter o domínio independente do banco de dados.

---

# Estratégia

O sistema utiliza um modelo híbrido.

Existem dois tipos de informação:

## 1. Dados Estruturais

Representam a configuração financeira do usuário.

Exemplos

- contas
- cartões
- metas
- patrimônio
- receitas recorrentes
- despesas recorrentes
- empréstimos

São CRUDs tradicionais.

---

## 2. Eventos Financeiros

Representam acontecimentos.

Nunca representam configuração.

São imutáveis.

Exemplos

- compra
- pagamento
- PIX
- salário
- estorno
- transferência
- rendimento

---

# Regra Fundamental

O sistema nunca altera o passado.

Quando algo muda, um novo evento é criado.

Exemplo

Compra

↓

Estorno

↓

Nova compra

Nunca:

UPDATE valor = ...

---

# Agregados Persistidos

## Identity

User

---

## Planning

Account

CreditCard

Loan

Financing

RecurringIncome

RecurringExpense

FinancialGoal

Asset

Liability

---

## Execution

FinancialEvent

Invoice

Installment

StatementImport

---

## Recommendation

Recommendation

RecommendationPlan

---

# Objetos Não Persistidos

Os seguintes objetos são produzidos sob demanda.

CashFlow

FinancialDiagnosis

FinancialProjection

FinancialHealth

Esses objetos poderão ser armazenados futuramente para otimização.

Inicialmente serão sempre recalculados.

---

# Modelo Lógico

```
User
 │
 ├──────────────┐
 ▼              ▼
Account     CreditCard
 │              │
 ├──────┐       │
 ▼      ▼       ▼
RecurringIncome RecurringExpense
        │
        ▼
FinancialEvent
        │
        ├──────────────┐
        ▼              ▼
Invoice       Installment
```

---

# Entidade FinancialEvent

É a principal tabela do sistema.

Todos os acontecimentos financeiros serão armazenados nela.

Campos

- id
- user_id
- occurred_at
- effective_at
- amount
- currency
- type
- status
- source
- account_id
- category_id
- reference_id
- description
- metadata

---

# Tipos de Evento

Income

Expense

Transfer

Purchase

InvoicePayment

Refund

Interest

Adjustment

LoanPayment

FinancingPayment

Investment

Dividend

---

# Status

Planned

Pending

Confirmed

Cancelled

Reversed

---

# Origem

Manual

CSV

OFX

OpenFinance

OCR

API

AI

System

---

# Effective Date

Todo evento possui duas datas.

## occurred_at

Quando aconteceu.

Exemplo

Compra realizada em 02/08.

---

## effective_at

Quando impacta o fluxo.

Exemplo

Compra parcelada.

A compra ocorreu em:

02/08

Mas a parcela impactará:

10/09

---

# Reference ID

Permite ligar eventos relacionados.

Exemplo

Compra

↓

12 Parcelas

↓

Pagamento

Todos compartilham a mesma referência.

---

# Metadata

Informações específicas do tipo.

Exemplo

Compra

```
merchant

authorization

cardBrand
```

PIX

```
endToEndId

bank
```

Importação

```
statementLine

fileName
```

---

# Estratégia para Parcelas

Uma compra parcelada gera:

Compra

+

N parcelas futuras.

Cada parcela é um evento independente.

Cada parcela poderá ser:

- prevista
- confirmada
- cancelada

---

# Estratégia para Recorrência

Receitas e despesas recorrentes nunca geram movimentações automaticamente no banco.

Elas geram eventos previstos.

Exemplo

Salário

↓

Evento previsto

↓

Usuário confirma

↓

Evento confirmado

---

# Exclusão

Eventos financeiros nunca serão excluídos.

As possibilidades são:

- Confirmado

- Cancelado

- Revertido

---

# Auditoria

Todas as entidades estruturais terão:

created_at

updated_at

created_by

updated_by

---

FinancialEvent

Nunca utiliza updated_at para alterar regras financeiras.

Caso seja necessário alterar um evento:

gera-se outro evento.

---

# Índices

FinancialEvent

Índices

(user_id, effective_at)

(user_id, occurred_at)

(account_id)

(category_id)

(type)

(status)

(reference_id)

---

# Chaves Estrangeiras

FinancialEvent

↓

Account

FinancialEvent

↓

Category

FinancialEvent

↓

User

FinancialEvent

↓

Reference

(opcional)

---

# Estratégia de Banco

Banco principal

PostgreSQL

---

ORM

SQLAlchemy 2.x

---

Migrations

Alembic

---

# Unit of Work

Cada caso de uso executa:

BEGIN

↓

persistência

↓

publicação de eventos

↓

COMMIT

---

# Soft Delete

Entidades estruturais

Sim.

Campo

deleted_at

---

Eventos financeiros

Nunca.

Eventos são históricos.

---

# Versionamento

Somente entidades estruturais poderão ser alteradas.

Caso seja necessário manter histórico de configuração:

Versionamento futuro.

---

# Backup

A recuperação completa do fluxo financeiro depende apenas de:

Dados estruturais

+

FinancialEvent

Todo o restante pode ser reconstruído.

---

# Princípios

- O histórico financeiro nunca é perdido.
- Eventos são imutáveis.
- Fluxo de caixa é calculado.
- Diagnósticos são derivados.
- Recomendações são derivadas.
- O banco de dados armazena fatos, não interpretações.