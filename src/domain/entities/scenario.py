from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.domain.entities.scenario_type import ScenarioType

if TYPE_CHECKING:
    from .financial_plan import FinancialPlan


@dataclass(slots=True)
class Scenario:
    name: str
    scenario_type: ScenarioType
    plan: FinancialPlan | None = None