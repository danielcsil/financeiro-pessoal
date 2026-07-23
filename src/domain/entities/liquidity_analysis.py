
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class LiquidityAnalysis:

    minimum_balance: Money
    maximum_balance: Money
    ending_balance: Money

    first_negative_day: date | None

    negative_days: int

    has_negative_balance: bool
