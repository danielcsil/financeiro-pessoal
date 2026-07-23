
from __future__ import annotations

from dataclasses import dataclass

from src.domain.entities import FinancialHealthScore


@dataclass(frozen=True, slots=True)
class ScenarioComparison:

    current: FinancialHealthScore

    projected: FinancialHealthScore

    score_gain: int

    liquidity_gain: float

    credit_reduction: float

    negative_days_reduction: int
