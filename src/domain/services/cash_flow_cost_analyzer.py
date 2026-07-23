
from __future__ import annotations

from src.domain.entities import CashFlowCost
from .credit_flow_dependency_analyzer import CreditFlowDependencyAnalyzer


class CashFlowCostAnalyzer:
    def analyze(
        self,
        projection,
        monthly_income,
    ) -> CashFlowCost:

        dependency = CreditFlowDependencyAnalyzer().analyze(
            projection
        )

        financed = (
            dependency.financed_amount
            if dependency is not None
            else monthly_income.zero()
        )

        percentage = (
            float(financed) / float(monthly_income) * 100
            if monthly_income > monthly_income.zero()
            else 0.0
        )

        return CashFlowCost(
            financed_amount=financed,
            monthly_income=monthly_income,
            percentage_of_income=percentage,
        )
