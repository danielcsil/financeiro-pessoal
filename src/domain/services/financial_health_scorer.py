
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

    def calculate_from_liquidity(
        self,
        liquidity,
    ) -> FinancialHealthScore:

        liquidity_score = 100 if not liquidity.has_negative_balance else 40
        risk_score = 100 if liquidity.negative_days == 0 else 50

        return self.calculate(
            liquidity=liquidity_score,
            reserve=100 if liquidity.ending_balance.is_positive() else 0,
            credit_dependency=100,
            stability=max(0, 100 - liquidity.negative_days * 10),
            risk=risk_score,
        )
