
from __future__ import annotations

from dataclasses import dataclass

from .cash_flow_projection import CashFlowProjection
from .liquidity_analysis import LiquidityAnalysis


@dataclass(frozen=True, slots=True)
class SimulationResult:

    projection: CashFlowProjection

    liquidity: LiquidityAnalysis

    baseline_projection: CashFlowProjection | None = None

    baseline_liquidity: LiquidityAnalysis | None = None

    @property
    def has_baseline(self) -> bool:
        return (
            self.baseline_projection is not None
            and self.baseline_liquidity is not None
        )
