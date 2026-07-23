
from __future__ import annotations

from src.domain.entities import CashFlowRecoveryPlan
from .capital_need_analyzer import CapitalNeedAnalyzer


class CashFlowRecoveryPlanner:

    def build(
        self,
        projection,
        monthly_saving_capacity,
    ) -> CashFlowRecoveryPlan:

        capital = CapitalNeedAnalyzer().analyze(projection)

        required = capital.required_capital

        if monthly_saving_capacity.is_zero():

            months = 0

        else:

            months = int(
                (required / monthly_saving_capacity).value
            )

            if required % monthly_saving_capacity:
                months += 1

        return CashFlowRecoveryPlan(
            required_capital=required,
            suggested_monthly_reduction=monthly_saving_capacity,
            estimated_months_to_recover=months,
        )
