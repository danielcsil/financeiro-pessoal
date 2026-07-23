
from __future__ import annotations

from dataclasses import dataclass

from src.domain.entities import FinancialPlan
from src.domain.entities.scenario_type import ScenarioType


@dataclass(slots=True)
class Scenario:

    name: str
    scenario_type: ScenarioType

    plan: FinancialPlan
