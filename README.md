# Personal Finance

> **Personal Finance** é uma plataforma de gestão financeira pessoal desenvolvida para ajudar pessoas e famílias a recuperar o controle do fluxo de caixa, organizar suas finanças e tomar decisões financeiras mais inteligentes com o apoio de Inteligência Artificial.

Atualmente o projeto encontra-se na versão **1.0.0**, com autenticação completa, interface web, API REST e uma arquitetura preparada para evoluir para um assistente financeiro inteligente.

---

# O Problema

Grande parte das pessoas sabe quanto ganha, mas não consegue responder perguntas importantes sobre sua vida financeira, como:

- Para onde meu dinheiro está indo?
- Vou conseguir pagar todas as contas deste mês?
- Quanto dinheiro terei disponível daqui a 30 dias?
- Posso assumir um novo financiamento?
- Qual o impacto de uma compra parcelada no meu fluxo de caixa?
- Estou realmente melhorando minha saúde financeira?

As ferramentas tradicionais normalmente registram apenas o passado. Poucas ajudam o usuário a compreender o presente e, principalmente, a prever o futuro.

O **Personal Finance** nasceu para resolver esse problema.

Seu principal objetivo é transformar informações financeiras em conhecimento para apoiar decisões antes que problemas aconteçam.

---

# Objetivos

O sistema foi projetado para permitir que o usuário:

- organizar toda sua vida financeira em um único lugar;
- controlar contas bancárias, cartões, investimentos e financiamentos;
- acompanhar receitas e despesas;
- visualizar projeções futuras do fluxo de caixa;
- monitorar indicadores de saúde financeira;
- definir metas financeiras;
- receber recomendações automáticas;
- utilizar Inteligência Artificial para apoiar decisões financeiras.

Mais do que registrar movimentações, o objetivo é oferecer uma visão completa da situação financeira atual e futura.

---

# Funcionalidades

## Autenticação

- Cadastro de usuários
- Login utilizando JWT
- Rotas protegidas
- Usuário autenticado

---

## Gestão Financeira

### Implementado

- Cadastro de usuários
- Login
- Dashboard inicial

### Em desenvolvimento

- Contas
- Categorias
- Receitas
- Despesas
- Cartões de crédito
- Financiamentos
- Investimentos
- Metas
- Fluxo de Caixa
- Relatórios

---

## Inteligência Artificial

Planejado para as próximas versões:

- Diagnóstico financeiro automático
- Recomendações personalizadas
- Classificação automática de despesas
- Projeção inteligente do fluxo de caixa
- Assistente financeiro conversacional
- Sugestões de economia
- Simulações financeiras

---

# Arquitetura

O projeto segue os princípios de:

- Domain Driven Design (DDD)
- Clean Architecture
- SOLID
- Test Driven Development (TDD)

As regras de negócio permanecem totalmente independentes de frameworks e tecnologias de infraestrutura.

```
Frontend (Vue)

        │

        ▼

FastAPI

        │

        ▼

Application

        │

        ▼

Domain

        │

        ▼

Infrastructure
```

---

# Tecnologias

## Backend

- Python
- FastAPI
- JWT
- Bcrypt
- Pytest

## Frontend

- Vue 3
- TypeScript
- Vite
- Vue Router
- Pinia
- Axios

---

# Estrutura do Projeto

```text
financeiro-pessoal/

├── apps/
│   └── web/                  # Frontend Vue
│
├── src/
│   ├── api/                  # Controllers, rotas e schemas
│   ├── application/          # Casos de uso
│   ├── domain/               # Entidades e regras de negócio
│   ├── infrastructure/       # Implementações externas
│   └── config/               # Configurações
│
├── tests/                    # Testes automatizados
│
├── docs/                     # Documentação
│
└── README.md
```

---

# Estado Atual

**Versão:** `1.0.0`

## Implementado

- Backend FastAPI
- Frontend Vue
- Arquitetura DDD
- Clean Architecture
- Autenticação completa
- Cadastro de usuários
- Login
- JWT
- Rotas protegidas
- Dashboard inicial
- Testes automatizados

---

# Roadmap

## Versão 1.1

- Contas
- Categorias

## Versão 1.2

- Receitas
- Despesas

## Versão 1.3

- Cartões
- Fluxo de Caixa

## Versão 1.4

- Dashboards
- Indicadores financeiros

## Versão 2.0

- Inteligência Artificial
- Recomendações automáticas
- Planejamento financeiro inteligente
- Assistente Financeiro

---

# Como executar o projeto

## Backend

### Criar ambiente virtual

```bash
python -m venv .venv
```

### Ativar ambiente

Windows

```bash
.\.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

### Instalar dependências

```bash
pip install -e ".[dev]"
```

### Executar API

```bash
python -m uvicorn src.api.main:app --reload
```

Documentação disponível em:

```
http://localhost:8000/docs
```

---

## Frontend

```bash
cd apps/web
```

Instalar dependências

```bash
npm install
```

Executar

```bash
npm run dev
```

Aplicação disponível em:

```
http://localhost:5173
```

---

# Testes

Executar toda a suíte:

```bash
pytest
```

Ou:

```bash
python -m pytest
```

---

# Princípios Arquiteturais

O projeto foi desenvolvido seguindo os seguintes princípios:

- Clean Code
- SOLID
- Domain Driven Design
- Clean Architecture
- Test Driven Development
- Separation of Concerns
- Dependency Injection
- Repository Pattern
- Value Objects
- Entities
- Use Cases

---

# Visão de Longo Prazo

O objetivo do **Personal Finance** é evoluir para um verdadeiro **Assistente Financeiro Inteligente**.

Em vez de apenas registrar receitas e despesas, o sistema será capaz de compreender o comportamento financeiro do usuário, antecipar problemas de fluxo de caixa, sugerir estratégias para redução de gastos e auxiliar no planejamento financeiro de curto, médio e longo prazo.

O foco principal do projeto é responder continuamente à pergunta:

> **"O que devo fazer hoje para ter uma vida financeira melhor amanhã?"**

---

# Autor

**Daniel Cunha da Silva**