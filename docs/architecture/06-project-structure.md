# Arquitetura do Projeto

## Objetivo

Este documento define a organização da implementação do Personal Finance utilizando:

- Domain-Driven Design (DDD)
- Clean Architecture
- SOLID
- Repository Pattern
- Unit of Work
- Domain Events
- CQRS (parcial)
- Dependency Injection

O objetivo é garantir uma arquitetura modular, desacoplada, testável e preparada para evolução.

---

# Camadas

O sistema é dividido em quatro camadas principais.

```
                   API
                    │
                    ▼
             Application
                    │
                    ▼
                Domain
                    ▲
                    │
            Infrastructure
```

O domínio não conhece nenhuma outra camada.

---

# Estrutura do Projeto

```
src/

├── api/
│
├── application/
│
├── domain/
│
├── infrastructure/
│
└── shared/
```

Cada camada possui responsabilidades específicas.

---

# Domain

Responsável por representar o negócio.

Não depende de:

- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT
- HTTP

Contém apenas regras de negócio.

---

Estrutura

```
domain/

identity/

planning/

execution/

analysis/

recommendation/

assistant/
```

Cada contexto possui:

```
entities/

value_objects/

repositories/

services/

events/

exceptions/

enums/
```

---

# Application

Implementa os casos de uso.

Não contém regras de infraestrutura.

Estrutura:

```
application/

dto/

commands/

queries/

use_cases/

interfaces/

mappers/
```

---

## DTO

Representam entrada e saída.

Nunca possuem regras de negócio.

---

## Commands

Representam ações.

Exemplo

RegisterPurchaseCommand

---

## Queries

Representam consultas.

Exemplo

GetCashFlowQuery

---

## Use Cases

Implementam fluxos de negócio.

Exemplo

GenerateDiagnosisUseCase

---

# Infrastructure

Implementa detalhes técnicos.

Exemplos

- PostgreSQL
- SQLAlchemy
- JWT
- bcrypt
- arquivos
- Open Finance
- OCR

Estrutura

```
infrastructure/

database/

repositories/

security/

services/

config/

external/

events/
```

---

# API

Responsável apenas pela comunicação HTTP.

Estrutura

```
api/

routers/

dependencies/

middlewares/

schemas/

responses/
```

Nenhuma regra de negócio deve existir aqui.

---

# Organização por Contexto

Cada contexto será organizado de forma semelhante.

Exemplo

```
execution/

entities/

FinancialEvent.py

repositories/

FinancialEventRepository.py

services/

CashFlowService.py

events/

FinancialEventRecorded.py

value_objects/

Money.py

Status.py

enums/

EventStatus.py
```

---

# Fluxo de Dependências

```
API

↓

Use Case

↓

Repository Interface

↓

Domain

↑

Repository Implementation

↓

PostgreSQL
```

O domínio nunca conhece SQLAlchemy.

---

# Repository Pattern

Todo Aggregate Root possui um repositório.

Exemplo

```
AccountRepository

CreditCardRepository

FinancialEventRepository

GoalRepository
```

A implementação pertence à infraestrutura.

```
SqlAlchemyAccountRepository

SqlAlchemyFinancialEventRepository
```

---

# Unit of Work

Cada caso de uso executa dentro de uma Unit of Work.

Exemplo

```
Begin Transaction

↓

Executa Caso de Uso

↓

Publica Domain Events

↓

Commit

↓

Rollback (se necessário)
```

O domínio nunca faz commit.

---

# Domain Events

Todo Aggregate pode produzir eventos.

Exemplo

```
PurchaseRegistered

↓

InvoiceGenerationService

↓

FinancialEventCreated

↓

CashFlowInvalidated

↓

DiagnosisInvalidated
```

Isso reduz o acoplamento entre agregados.

---

# Serviços de Domínio

Serviços existem apenas quando a regra envolve múltiplos agregados.

Exemplo

CashFlowEngine

DiagnosisEngine

ProjectionEngine

RecommendationEngine

InvoiceGenerationService

---

# CQRS

O sistema utilizará CQRS apenas na camada de aplicação.

Comandos

```
RegisterPurchase

RegisterIncome

PayInvoice

GenerateRecommendations
```

Consultas

```
GetDashboard

GetCashFlow

GetInvoices

GetDiagnosis
```

Não haverá bancos separados.

A separação é lógica.

---

# Dependency Injection

Toda dependência será injetada.

Exemplo

```
UseCase

↓

Repository

↓

Infrastructure
```

Nunca utilizar instanciação direta.

---

# Persistência

As entidades não conhecem SQLAlchemy.

Mapeadores converterão:

```
Entity

↓

ORM Model

↓

Tabela
```

O domínio permanece limpo.

---

# Tratamento de Erros

Cada contexto define suas próprias exceções.

Exemplo

```
InsufficientBalanceException

CreditLimitExceededException

InvoiceAlreadyPaidException

LoanAlreadySettledException
```

As exceções são traduzidas para HTTP apenas na API.

---

# Testes

A estratégia será dividida em quatro níveis.

## Testes Unitários

Entidades

Value Objects

Serviços

---

## Testes de Casos de Uso

Use Cases

---

## Testes de Integração

Repositórios

Banco

---

## Testes End-to-End

API completa.

---

# Comunicação entre Contextos

Nunca acessar diretamente outro agregado.

Sempre utilizar:

- Use Cases

ou

- Domain Events

---

# Evolução

Novos módulos poderão ser adicionados sem alterar os existentes.

Exemplos

- Open Finance

- Investimentos

- OCR

- IA

- Planejamento Tributário

- Planejamento Previdenciário

- Planejamento Sucessório

Todos serão adicionados como novos bounded contexts ou novos serviços de domínio.

---

# Princípios Arquiteturais

1. O domínio é o centro do sistema.
2. O banco de dados é um detalhe de implementação.
3. APIs apenas expõem casos de uso.
4. Toda regra financeira pertence ao domínio.
5. Eventos reduzem acoplamento.
6. Casos de uso orquestram o domínio.
7. Infraestrutura nunca define regras de negócio.
8. IA interpreta resultados; nunca executa regras financeiras.
9. Todo código deve ser facilmente testável.
10. O sistema deve evoluir sem exigir alterações no domínio existente.