
# Coding Guidelines

## Python

- Python 3.12+
- UTF-8
- Type Hints obrigatórios
- dataclass sempre que possível
- Decimal para dinheiro
- pathlib para arquivos

---

## Organização

Uma classe por arquivo.

Imports absolutos.

Sem imports circulares.

---

## Nomes

Classes:

PascalCase

Funções:

snake_case

Constantes:

UPPER_CASE

Arquivos:

snake_case.py

---

## Docstrings

Todas as classes públicas possuem docstrings.

---

## Logging

Nunca usar print dentro do domínio.

---

## Exceções

Nunca capturar Exception genericamente.

Sempre utilizar exceções específicas.

---

## Testes

Todo Value Object deverá possuir testes unitários.

---

## Formatação

Black

isort

ruff

---

## Princípios

SOLID

Clean Architecture

DDD

DRY

KISS

YAGNI
