
from __future__ import annotations

from src.domain.entities import FinancialHealthScore


class FinancialHealthScorer:
    """
    Consolida diversos indicadores financeiros
    em um índice único de saúde financeira.
    """

    def calculate(
        self,
        liquidity: int,
        reserve: int,
        credit_dependency: int,
        stability: int,
        risk: int,
    ) -> FinancialHealthScore:

        values = [
            liquidity,
            reserve,
            credit_dependency,
            stability,
            risk,
        ]

        overall = round(sum(values) / len(values))

        return FinancialHealthScore(
            overall=overall,
            liquidity=liquidity,
            reserve=reserve,
            credit_dependency=credit_dependency,
            stability=stability,
            risk=risk,
        )
