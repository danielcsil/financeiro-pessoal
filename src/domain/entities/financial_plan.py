
from __future__ import annotations

from dataclasses import dataclass

from src.domain.entities import CashFlowTimeline
from src.domain.entities import PlanningPeriod
from src.domain.value_objects import Money


@dataclass(slots=True)
class FinancialPlan:

    period: PlanningPeriod
    opening_balance: Money
    timeline: CashFlowTimeline
