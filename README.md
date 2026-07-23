# Financeiro Pessoal

Núcleo de domínio, em Python, para análise e planejamento financeiro pessoal. O projeto modela eventos financeiros ao longo de um período e transforma esses dados em projeções de caixa, diagnósticos de liquidez, indicadores de saúde financeira e recomendações de intervenção.

> **Status: alpha.** A versão declarada no pacote é `0.1.0-alpha.9`. O foco atual é a regra de negócio; ainda não há interface gráfica, API HTTP ou persistência de dados pronta para uso final.

## O que o projeto faz hoje

- Modela contas, categorias, transações, períodos de planejamento, objetivos e cenários.
- Representa valores financeiros com `Money`, baseado em `Decimal` e arredondado a duas casas; o domínio não usa `float` para cálculos monetários.
- Constrói uma linha do tempo diária de fluxo de caixa e projeta o saldo para o período.
- Identifica saldo negativo, menor e maior saldo, dias negativos e eventos/lacunas de liquidez.
- Calcula uma pontuação de saúde financeira de 0 a 100.
- Simula despesas, receitas, decisões e intervenções; compara cenários e gera estratégias de recuperação/otimização.
- Produz um relatório textual com resumo e destaques da recomendação.

O ponto de orquestração é `FinancialPlanner`. Ele executa o pipeline abaixo e retorna um `PlanningResult` consolidado:

```text
Plano financeiro → projeção de caixa → análise de liquidez → score de saúde
       └────────────────────→ diagnóstico/estratégias → recomendação e relatório
```

## Arquitetura

O código segue princípios de DDD e Clean Architecture. As regras estão concentradas em `src/domain`, sem dependência de infraestrutura ou interface.

```text
src/
├── domain/
│   ├── entities/       # entidades e resultados do domínio
│   ├── enums/          # tipos e estados do domínio
│   ├── value_objects/  # Money, Percentage e DailyCashFlow
│   └── services/       # projeções, análises, simulações e recomendações
├── config/             # metadados e configurações básicas
└── main.py             # ponto de entrada informativo atual

tests/
├── domain/             # testes unitários das entidades, VOs e serviços
└── integration/        # validação do pipeline FinancialPlanner
```

### Aplicações web (monorepo)

O repositório agora também contém as aplicações de entrega em `apps/`:

- `apps/api`: API FastAPI inicial com `GET /health` e `POST /api/v1/plans/analyze`.
- `apps/web`: interface inicial em Vue 3, Vite e TypeScript. Em desenvolvimento, o Vite redireciona chamadas `/api` para `http://localhost:8000`.

`src/` e `tests/` permanecem na raiz nesta primeira etapa para preservar os imports e a configuração de testes existentes. Veja [apps/README.md](apps/README.md) para os comandos de execução e a estratégia de migração segura.

Decisões importantes do projeto:

- O domínio não conhece infraestrutura.
- Objetos de valor são imutáveis.
- Dinheiro é sempre `Money`/`Decimal`.
- Persistência em Excel é planejada como adaptador, nunca como local para regras de negócio.
- O núcleo foi pensado para futuras interfaces como CLI, web, desktop e notebooks.

Os detalhes estão em [decisões de arquitetura](docs/architecture/architecture_decisions.md), [glossário](docs/architecture/glossary.md) e [roadmap](docs/architecture/project_roadmap.md).

## Requisitos e instalação

- Python 3.12 ou superior
- `pip`

Crie e ative um ambiente virtual:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as ferramentas de desenvolvimento:

```powershell
pip install -e ".[dev]"
```

Para a dependência adicional de planilhas já listada no repositório, use:

```powershell
pip install -r requirements.txt
```

## Uso básico

O exemplo abaixo cria um período, registra uma despesa na linha do tempo e executa o planejador.

```python
from datetime import date

from src.domain.entities import (
    Account,
    CashFlowTimeline,
    Category,
    FinancialPlan,
    PlanningPeriod,
    Transaction,
)
from src.domain.enums import AccountType, CategoryType
from src.domain.services import FinancialPlanner
from src.domain.value_objects import Money

period = PlanningPeriod(date(2026, 8, 1), date(2026, 8, 31))
timeline = CashFlowTimeline(period.start_date, period.end_date)

account = Account("Conta corrente", AccountType.CHECKING)
market = Category("Mercado", CategoryType.EXPENSE)

timeline.add_transaction(
    Transaction(
        account=account,
        category=market,
        amount=Money(250),
        transaction_date=date(2026, 8, 5),
        description="Compras do mês",
    )
)

plan = FinancialPlan(
    period=period,
    opening_balance=Money(1_000),
    timeline=timeline,
)

result = FinancialPlanner().analyze(plan)

print(result.score.overall)
print(result.liquidity.minimum_balance)
print(result.report.summary)
```

`PlanningResult` disponibiliza a projeção (`projection`), a análise de liquidez (`liquidity`), o score (`score`), o resultado do aconselhamento (`advisor`), eventuais dados de otimização/comparação e o relatório final (`report`).

Há também um arquivo inicial em [examples/financial_planner_example.py](examples/financial_planner_example.py). Ele ilustra a API pública, mas ainda contém um placeholder para a construção do plano; o exemplo acima pode ser usado como referência funcional completa.

## Testes e qualidade

Execute toda a suíte com cobertura:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

No estado atual do repositório, a suíte contém **133 testes** e finaliza com sucesso. A configuração de desenvolvimento também prevê Black, isort, Ruff e mypy:

```powershell
black src tests
isort src tests
ruff check src tests
mypy src
```

As convenções de código estão em [coding_guidelines.md](docs/architecture/coding_guidelines.md).

## Escopo atual e próximos passos

O projeto já possui uma base ampla de domínio e serviços, mas alguns itens permanecem planejados ou incompletos:

- persistência/importação/exportação em Excel;
- dashboard, gráficos e uma interface de uso;
- integrações de IA e classificação automática;
- uma API ou CLI de produto, além do núcleo de domínio;
- exemplos de ponta a ponta mais completos.

Consulte o [roadmap](docs/architecture/project_roadmap.md) para a visão de evolução e o [changelog](CHANGELOG.md) para o histórico disponível.

## Autor

Daniel Cunha da Silva
