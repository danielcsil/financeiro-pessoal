# Architecture Decision Records

Este documento registra as principais decisões arquiteturais adotadas no projeto **Personal Finance**.

Cada ADR representa uma decisão considerada estável e que deverá orientar a evolução do sistema. Alterações nesses princípios devem ser cuidadosamente avaliadas, pois podem impactar toda a arquitetura.

---

## ADR-001 — Independência do Domínio

### Decisão

A camada de domínio nunca conhecerá detalhes de infraestrutura.

### Motivação

As regras de negócio representam o principal ativo do sistema e devem permanecer independentes de frameworks, banco de dados, APIs ou mecanismos de persistência.

### Consequências

- O domínio permanece testável sem dependências externas.
- A infraestrutura pode ser substituída sem alterar as regras de negócio.
- O acoplamento entre as camadas é reduzido.

---

## ADR-002 — Representação de Valores Monetários

### Decisão

Todo valor monetário será representado pelo Value Object `Money`.

### Motivação

Centralizar regras relacionadas a operações financeiras e evitar representações inconsistentes de valores monetários.

### Consequências

- Todas as operações financeiras utilizam uma representação única.
- Regras de arredondamento e comparação permanecem centralizadas.
- Evita duplicação de lógica financeira.

---

## ADR-003 — Uso Exclusivo de Decimal

### Decisão

Todas as operações financeiras utilizarão `Decimal`.

O uso de `float` no domínio é proibido.

### Motivação

Operações financeiras exigem precisão decimal.

### Consequências

- Elimina erros de precisão inerentes ao tipo `float`.
- Garante consistência nos cálculos financeiros.

---

## ADR-004 — Persistência como Detalhe de Infraestrutura

### Decisão

A persistência é um detalhe de infraestrutura.

O domínio não dependerá do mecanismo de armazenamento utilizado.

### Motivação

Permitir a substituição do mecanismo de persistência sem impacto nas regras de negócio.

Atualmente, o sistema utiliza PostgreSQL como banco principal.

### Consequências

- O domínio permanece desacoplado da tecnologia de persistência.
- A infraestrutura pode evoluir independentemente da camada de domínio.

---

## ADR-005 — Regras de Negócio Pertencem ao Domínio

### Decisão

Toda regra de negócio pertence ao domínio.

A camada de aplicação apenas orquestra os casos de uso.

### Motivação

Centralizar o comportamento do sistema na camada responsável pelo conhecimento do negócio.

### Consequências

- Evita duplicação de regras.
- Mantém os casos de uso simples.
- Facilita testes unitários.

---

## ADR-006 — Imutabilidade dos Value Objects

### Decisão

Todos os Value Objects serão imutáveis.

### Motivação

Value Objects representam conceitos do domínio e não possuem identidade própria.

### Consequências

- Objetos tornam-se naturalmente thread-safe.
- Comparações são simplificadas.
- Reduz efeitos colaterais.

---

## ADR-007 — Dependência entre Camadas

### Decisão

A infraestrutura depende do domínio.

O domínio nunca dependerá da infraestrutura.

### Motivação

Seguir o princípio da inversão de dependências da Clean Architecture.

### Consequências

- O domínio permanece independente.
- Frameworks tornam-se substituíveis.
- A arquitetura permanece desacoplada.

---

## ADR-008 — Repositórios como Abstrações

### Decisão

Todos os repositórios serão definidos como interfaces no domínio.

As implementações concretas pertencem à infraestrutura.

### Motivação

Separar regras de negócio dos detalhes de persistência.

### Consequências

- Facilita testes utilizando implementações em memória.
- Permite múltiplas estratégias de persistência.

---

## ADR-009 — Independência dos Casos de Uso

### Decisão

Todos os casos de uso serão independentes da interface de entrada.

### Motivação

As regras de aplicação devem poder ser reutilizadas por diferentes interfaces.

### Consequências

Os mesmos casos de uso poderão ser utilizados por:

- API REST
- Interface Web
- CLI
- Desktop
- Testes automatizados

Sem alterações na lógica da aplicação.

---

## ADR-010 — Suporte a Múltiplas Interfaces

### Decisão

O sistema será projetado para suportar múltiplas interfaces de interação.

### Motivação

A arquitetura deve permitir reutilização da camada de aplicação independentemente do canal utilizado.

### Consequências

A evolução para novas interfaces (como aplicações móveis ou integrações externas) poderá ocorrer sem alterações significativas nas regras de negócio.