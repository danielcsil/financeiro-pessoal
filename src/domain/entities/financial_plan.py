
from __future__ import annotations

from dataclasses import dataclass, field

from src.domain.entities import (
    CashFlowTimeline,
    FinancialGoal,
    PlanningPeriod,
    Scenario,
)
from src.domain.value_objects import Money


@dataclass(slots=True)
class FinancialPlan:

    period: PlanningPeriod

    opening_balance: Money

    timeline: CashFlowTimeline

    goals: list[FinancialGoal] = field(default_factory=list)

    scenarios: list[Scenario] = field(default_factory=list)

    def add_goal(self, goal: FinancialGoal) -> None:
        self.goals.append(goal)

    def add_scenario(self, scenario: Scenario) -> None:
        self.scenarios.append(scenario)
