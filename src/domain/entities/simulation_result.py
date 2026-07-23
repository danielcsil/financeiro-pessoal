
from __future__ import annotations

from dataclasses import dataclass

from src.domain.entities import (
    CashFlowProjection,
    LiquidityAnalysis,
)


@dataclass(frozen=True, slots=True)
class SimulationResult:

    projection: CashFlowProjection

    liquidity: LiquidityAnalysis
