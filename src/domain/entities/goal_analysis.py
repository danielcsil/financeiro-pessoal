
from __future__ import annotations

from dataclasses import dataclass

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class GoalAnalysis:

    achieved: bool

    projected_balance: Money

    target_amount: Money

    difference: Money
