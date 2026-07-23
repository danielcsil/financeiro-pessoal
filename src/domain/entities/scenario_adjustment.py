
from __future__ import annotations

from dataclasses import dataclass

from .transaction import Transaction
from src.domain.entities.scenario_adjustment_type import (
    ScenarioAdjustmentType,
)


@dataclass(frozen=True, slots=True)
class ScenarioAdjustment:

    adjustment_type: ScenarioAdjustmentType
    transaction: Transaction
