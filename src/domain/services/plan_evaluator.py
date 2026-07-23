
from __future__ import annotations

from src.domain.entities import PlanEvaluation
from .financial_health_analyzer import FinancialHealthAnalyzer
from .goal_analyzer import GoalAnalyzer


class PlanEvaluator:

    def evaluate(
        self,
        projection,
        goal=None,
    ) -> PlanEvaluation:

        score = 100

        health = FinancialHealthAnalyzer().analyze(projection)

        if health.level.name == "CRITICAL":
            score -= 50
        elif health.level.name == "ATTENTION":
            score -= 20

        if goal is not None:
            goal_result = GoalAnalyzer().analyze(
                projection,
                goal,
            )

            if not goal_result.achieved:
                score -= 30

        score = max(0, score)

        return PlanEvaluation(
            feasible=score >= 70,
            score=score,
            summary="Plano financeiramente viável." if score >= 70 else "Plano necessita de ajustes.",
        )
