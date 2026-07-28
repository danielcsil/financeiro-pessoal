# Arquitetura

Esta pasta reúne toda a documentação arquitetural do projeto **Personal Finance**.

O objetivo é registrar as decisões de projeto, a modelagem do domínio e as diretrizes que orientam a implementação do sistema.

---

# Organização

## 1. Visão

Documento que descreve a motivação do sistema, seus objetivos e o problema de negócio que ele resolve.

Arquivo:

```
vision.md
```

---

## 2. Modelo Conceitual

Descreve os principais conceitos do domínio e como eles se relacionam.

Arquivo:

```
domain-model.md
```

---

## 3. Bounded Contexts

Define os limites de responsabilidade de cada contexto do domínio.

Arquivo:

```
bounded-contexts.md
```

---

## 4. Linguagem Ubíqua

Padroniza os termos utilizados em todo o projeto.

Arquivo:

```
ubiquitous-language.md
```

---

## 5. Domain Blueprint

Detalha cada Aggregate Root, suas responsabilidades, invariantes, eventos e casos de uso.

Arquivo:

```
domain-blueprint.md
```

---

## 6. Estrutura do Projeto

Define como a arquitetura é refletida na organização do código.

Arquivo:

```
project-structure.md
```

---

## 7. Modelo de Persistência

Documenta a estratégia de persistência do sistema.

Arquivo:

```
persistence-model.md
```

---

## 8. ADR

Registra decisões arquiteturais específicas.

Cada ADR representa apenas uma decisão.

```
adr/
```

---

# Ordem de Leitura

Para compreender completamente a arquitetura recomenda-se a seguinte sequência:

1. vision.md
2. domain-model.md
3. bounded-contexts.md
4. ubiquitous-language.md
5. domain-blueprint.md
6. project-structure.md
7. persistence-model.md
8. ADRs

---

# Objetivos Arquiteturais

O projeto adota os seguintes princípios:

- Domain-Driven Design (DDD)
- Clean Architecture
- SOLID
- Test-Driven Development (TDD)
- Repository Pattern
- Unit of Work
- Domain Events
- Dependency Injection

---

# Objetivo do Domínio

O foco do sistema não é registrar receitas e despesas.

O objetivo é compreender a realidade financeira do usuário, explicar seu fluxo de caixa, produzir diagnósticos e recomendar ações que melhorem sua saúde financeira.

Toda decisão arquitetural deve preservar esse princípio.