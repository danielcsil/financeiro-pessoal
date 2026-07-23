
from __future__ import annotations

from dataclasses import dataclass

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class SafeDailySpending:

    available_today: Money

    remaining_days: int

    recommended_daily_limit: Money
