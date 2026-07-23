
from __future__ import annotations

from dataclasses import dataclass, field

from .cash_flow_timeline import CashFlowTimeline
from .financial_goal import FinancialGoal
from .planning_period import PlanningPeriod
from .scenario import Scenario
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
