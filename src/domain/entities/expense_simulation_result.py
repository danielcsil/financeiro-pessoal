
from __future__ import annotations

from dataclasses import dataclass

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class ExpenseSimulationResult:

    approved: bool

    simulated_expense: Money

    remaining_margin: Money

    message: str
