# Coding Guidelines

Este documento define os padrões de implementação adotados no projeto **Personal Finance**.

Todos os colaboradores devem seguir estas diretrizes para manter o código consistente, legível e alinhado com a arquitetura do sistema.

---

# Linguagem

- Python 3.12 ou superior.
- Arquivos codificados em UTF-8.
- Type Hints são obrigatórios em funções, métodos e atributos públicos.
- Utilizar `Decimal` para todas as operações financeiras.
- Utilizar `pathlib.Path` para manipulação de arquivos e diretórios.
- Evitar o uso de variáveis globais.

---

# Organização do Código

- Uma classe pública por arquivo.
- Utilizar imports absolutos.
- Evitar dependências circulares.
- Manter baixo acoplamento entre módulos.
- Cada módulo deve possuir uma responsabilidade bem definida.

---

# Convenções de Nomenclatura

## Classes

Utilizar **PascalCase**.

Exemplo:

```python
FinancialEvent
CreditCardRepository
```

---

## Funções e Métodos

Utilizar **snake_case**.

Exemplo:

```python
calculate_balance()
register_payment()
```

---

## Variáveis

Utilizar **snake_case**.

---

## Constantes

Utilizar **UPPER_CASE**.

Exemplo:

```python
DEFAULT_CURRENCY
MAX_INSTALLMENTS
```

---

## Arquivos

Utilizar **snake_case.py**.

Exemplo:

```text
financial_event.py
money.py
account_repository.py
```

---

# Documentação

Toda classe pública deve possuir docstring.

Métodos públicos devem possuir docstring quando seu comportamento não for evidente.

Comentários devem explicar o **porquê** de uma decisão, nunca apenas descrever o código.

---

# Logging

Nunca utilizar `print()` no código da aplicação.

Todo registro de informação deve utilizar o módulo `logging`.

A camada de domínio não deve realizar logging de infraestrutura.

---

# Tratamento de Exceções

Nunca capturar `Exception` genericamente, exceto em pontos de entrada da aplicação (API, CLI, Jobs, etc.).

Criar exceções específicas para representar violações das regras de negócio.

Exceções do domínio não devem depender de frameworks.

---

# Modelagem do Domínio

- Entidades possuem identidade.
- Value Objects são imutáveis.
- Agregados encapsulam regras de negócio.
- Serviços de domínio devem conter apenas comportamentos que não pertencem naturalmente a uma entidade.
- Objetos do domínio nunca conhecem infraestrutura.

---

# Persistência

- Repositórios são interfaces definidas no domínio.
- Implementações pertencem à infraestrutura.
- Nenhuma entidade conhece SQLAlchemy ou qualquer outro ORM.
- Toda persistência deve ocorrer através de repositórios.

---

# Casos de Uso

Cada caso de uso deve representar uma única intenção do usuário.

Os casos de uso:

- orquestram o domínio;
- controlam transações;
- utilizam repositórios através de interfaces;
- não implementam regras de negócio.

---

# Testes

Todo componente do domínio deve possuir testes unitários.

São obrigatórios testes para:

- Value Objects;
- Entidades;
- Serviços de Domínio;
- Casos de Uso.

Testes devem ser independentes de banco de dados e infraestrutura sempre que possível.

---

# Formatação

O projeto utiliza as seguintes ferramentas:

- Black
- isort
- Ruff

Todo código deve estar formatado antes de ser enviado ao repositório.

---

# Princípios Arquiteturais

O desenvolvimento deve seguir os seguintes princípios:

- SOLID
- Clean Architecture
- Domain-Driven Design (DDD)
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple, Stupid)
- YAGNI (You Aren't Gonna Need It)

Quando houver conflito entre simplicidade e generalização, deve-se priorizar a solução mais simples que atenda aos requisitos atuais.

---

# Dependências

Antes de adicionar uma nova biblioteca ao projeto, deve-se verificar:

- se a funcionalidade já existe na biblioteca padrão do Python;
- se a dependência é realmente necessária;
- se a biblioteca possui manutenção ativa;
- se sua licença é compatível com o projeto.

A introdução de novas dependências deve ser justificada tecnicamente.