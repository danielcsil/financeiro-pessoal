
from __future__ import annotations

from src.domain.entities import (
    SimulationResult,
)
from src.domain.services import (
    CashFlowProjector,
    LiquidityAnalyzer,
    ScenarioApplier,
)


class SimulationEngine:

    def simulate(
        self,
        financial_plan,
        adjustments,
    ) -> SimulationResult:

        timeline = ScenarioApplier().apply(
            financial_plan.timeline,
            adjustments,
        )

        projection = CashFlowProjector().project(
            opening_balance=financial_plan.opening_balance,
            timeline=timeline,
        )

        liquidity = LiquidityAnalyzer().analyze(
            projection
        )

        return SimulationResult(
            projection=projection,
            liquidity=liquidity,
        )
