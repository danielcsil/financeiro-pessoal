# Project Roadmap

## Objetivo

Este documento descreve a evolução planejada do projeto **Personal Finance**.

Cada versão representa um incremento funcional que adiciona valor ao sistema, mantendo uma base arquitetural estável e permitindo evolução contínua.

As versões intermediárias representam marcos de desenvolvimento e não necessariamente versões públicas.

---

# v0.1 — Fundação

Objetivo: estabelecer a base do projeto.

Entregas:

- Estrutura do repositório
- Clean Architecture
- Domain-Driven Design (DDD)
- Configuração do ambiente de desenvolvimento
- Pipeline de qualidade (Black, Ruff, isort, pytest)
- Documentação inicial

---

# v0.2 — Núcleo do Domínio

Objetivo: implementar os principais conceitos do domínio.

Entregas:

- Money
- Percentage
- Enums
- Value Objects
- Exceções do domínio
- Eventos de domínio

---

# v0.3 — Planejamento Financeiro

Objetivo: permitir o cadastro da estrutura financeira do usuário.

Entregas:

- Usuário
- Contas
- Categorias
- Cartões de Crédito
- Receitas Recorrentes
- Despesas Recorrentes
- Metas Financeiras

---

# v0.4 — Execução Financeira

Objetivo: registrar acontecimentos financeiros.

Entregas:

- FinancialEvent
- Transferências
- Compras
- Parcelamentos
- Faturas
- Pagamentos
- Estornos

---

# v0.5 — Persistência

Objetivo: armazenar os dados de forma segura e consistente.

Entregas:

- PostgreSQL
- SQLAlchemy
- Alembic
- Repositórios
- Unit of Work

---

# v0.6 — Análise Financeira

Objetivo: transformar dados em informações.

Entregas:

- Fluxo de Caixa
- Diagnóstico Financeiro
- Indicadores
- Projeções
- Saúde Financeira

---

# v0.7 — Interface Web

Objetivo: disponibilizar a aplicação ao usuário.

Entregas:

- Dashboard
- Gestão financeira
- Visualizações
- Relatórios
- Gráficos

---

# v0.8 — Inteligência Financeira

Objetivo: apoiar o usuário na tomada de decisão.

Entregas:

- Recomendações automáticas
- Classificação inteligente
- Assistente Financeiro
- Explicações sobre diagnósticos

---

# v0.9 — Integrações

Objetivo: ampliar as formas de entrada e saída de dados.

Entregas:

- Importação de extratos
- Exportação de dados
- Open Finance
- APIs externas

---

# v1.0 — Primeira Versão Estável

Objetivo: disponibilizar a primeira versão completa do sistema.

Entregas:

- Plataforma Web
- Gestão financeira completa
- Fluxo de caixa
- Diagnósticos
- Recomendações
- Relatórios
- Documentação
- Testes automatizados