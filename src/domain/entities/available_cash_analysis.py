
from __future__ import annotations

from dataclasses import dataclass

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class AvailableCashAnalysis:

    current_balance: Money
    minimum_future_balance: Money
    available_to_spend: Money
