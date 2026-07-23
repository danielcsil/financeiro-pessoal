
from __future__ import annotations

from dataclasses import dataclass

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class CashFlowRecoveryPlan:

    required_capital: Money

    suggested_monthly_reduction: Money

    estimated_months_to_recover: int
