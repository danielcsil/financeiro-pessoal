
from __future__ import annotations

from dataclasses import dataclass

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class CashFlowCost:

    financed_amount: Money

    monthly_income: Money

    percentage_of_income: float
