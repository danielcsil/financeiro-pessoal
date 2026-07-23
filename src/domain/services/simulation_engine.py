
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

        baseline_projection = CashFlowProjector().project(
            opening_balance=financial_plan.opening_balance,
            timeline=financial_plan.timeline,
        )

        baseline_liquidity = LiquidityAnalyzer().analyze(
            baseline_projection
        )

        simulated_timeline = ScenarioApplier().apply(
            financial_plan.timeline,
            adjustments,
        )

        simulated_projection = CashFlowProjector().project(
            opening_balance=financial_plan.opening_balance,
            timeline=simulated_timeline,
        )

        simulated_liquidity = LiquidityAnalyzer().analyze(
            simulated_projection
        )

        return SimulationResult(
            projection=simulated_projection,
            liquidity=simulated_liquidity,
            baseline_projection=baseline_projection,
            baseline_liquidity=baseline_liquidity,
        )
