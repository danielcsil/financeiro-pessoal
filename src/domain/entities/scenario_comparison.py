
from __future__ import annotations

from dataclasses import dataclass

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class ScenarioComparison:

    original_max_gap: Money

    simulated_max_gap: Money

    gap_reduction: Money

    original_recovery_months: int

    simulated_recovery_months: int

    recommendation: str
