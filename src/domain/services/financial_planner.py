
from __future__ import annotations

from src.domain.entities import PlanningResult

from .cash_flow_projector import CashFlowProjector
from .financial_advisor import FinancialAdvisor
from .financial_health_scorer import FinancialHealthScorer
from .liquidity_analyzer import LiquidityAnalyzer
from .recommendation_explainer import RecommendationExplainer


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

        projection = self.projector.project(
            financial_plan.timeline,
            financial_plan.opening_balance,
        )

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
