
from __future__ import annotations

from dataclasses import dataclass

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class IncomeSimulationResult:

    simulated_income: Money

    additional_margin: Money

    message: str
