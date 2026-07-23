"""Ponto de entrada da API FastAPI.

Esta camada só valida/serializa HTTP e delega o cálculo ao domínio existente.
"""

from fastapi import FastAPI, HTTPException

from src.domain.entities import (
    Account,
    CashFlowTimeline,
    Category,
    FinancialPlan,
    PlanningPeriod,
    Transaction,
)
from src.domain.enums import AccountType, CategoryType, TransactionType
from src.domain.services import FinancialPlanner
from src.domain.value_objects import Money

from .schemas import (
    LiquidityResponse,
    PlanAnalysisRequest,
    PlanAnalysisResponse,
    ScoreResponse,
)


app = FastAPI(
    title="Financeiro Pessoal API",
    version="0.1.0-alpha.9",
    description="API inicial para análise de planejamento financeiro pessoal.",
)


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/v1/plans/analyze", response_model=PlanAnalysisResponse, tags=["plans"])
def analyze_plan(payload: PlanAnalysisRequest) -> PlanAnalysisResponse:
    if payload.end_date < payload.start_date:
        raise HTTPException(
            status_code=422,
            detail="end_date deve ser igual ou posterior a start_date.",
        )

    period = PlanningPeriod(payload.start_date, payload.end_date)
    timeline = CashFlowTimeline(period.start_date, period.end_date)
    account = Account("Planejamento", AccountType.CHECKING)

    for item in payload.transactions:
        if item.date < period.start_date or item.date > period.end_date:
            raise HTTPException(
                status_code=422,
                detail="Todas as transações devem estar dentro do período informado.",
            )

        transaction_type = TransactionType(item.type)
        category_type = (
            CategoryType.INCOME
            if transaction_type is TransactionType.INCOME
            else CategoryType.EXPENSE
        )
        timeline.add_transaction(
            Transaction(
                account=account,
                category=Category(item.category, category_type),
                amount=Money(item.amount),
                type=transaction_type,
                transaction_date=item.date,
                description=item.description,
            )
        )

    result = FinancialPlanner().analyze(
        FinancialPlan(
            period=period,
            opening_balance=Money(payload.opening_balance),
            timeline=timeline,
        )
    )

    liquidity = result.liquidity
    score = result.score
    return PlanAnalysisResponse(
        score=ScoreResponse(
            overall=score.overall,
            liquidity=score.liquidity,
            reserve=score.reserve,
            credit_dependency=score.credit_dependency,
            stability=score.stability,
            risk=score.risk,
        ),
        liquidity=LiquidityResponse(
            minimum_balance=liquidity.minimum_balance.to_decimal(),
            maximum_balance=liquidity.maximum_balance.to_decimal(),
            ending_balance=liquidity.ending_balance.to_decimal(),
            first_negative_day=liquidity.first_negative_day,
            negative_days=liquidity.negative_days,
            has_negative_balance=liquidity.has_negative_balance,
        ),
        summary=result.report.summary,
        highlights=list(result.report.highlights),
    )
