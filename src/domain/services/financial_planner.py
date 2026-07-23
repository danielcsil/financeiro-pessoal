
from __future__ import annotations

from src.domain.entities import PlanningResult

from src.domain.services import (
    CashFlowProjector,
    LiquidityAnalyzer,
    FinancialHealthScorer,
    FinancialAdvisor,
    RecommendationExplainer,
)


class FinancialPlanner:

    def __init__(self):

        self.projector = CashFlowProjector()

        self.liquidity = LiquidityAnalyzer()

        self.scorer = FinancialHealthScorer()

        self.advisor = FinancialAdvisor()

        self.explainer = RecommendationExplainer()

    def analyze(self, financial_plan) -> PlanningResult:
        """
        Executa o pipeline completo de planejamento
        financeiro utilizando os serviços do domínio.
        """

        projection = self.projector.project(financial_plan)

        liquidity = self.liquidity.analyze(projection)

        score = self.scorer.calculate_from_liquidity(
            liquidity
        )

        advisor = self.advisor.analyze(
            financial_plan
        )

        report = self.explainer.create_report(
            score,
            advisor,
        )

        optimization = getattr(
            advisor,
            "optimization",
            None,
        )

        comparison = getattr(
            advisor,
            "comparison",
            None,
        )

        return PlanningResult(
            projection=projection,
            liquidity=liquidity,
            score=score,
            advisor=advisor,
            optimization=optimization,
            comparison=comparison,
            report=report,
        )
