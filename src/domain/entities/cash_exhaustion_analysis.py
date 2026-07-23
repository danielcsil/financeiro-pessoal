
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class CashExhaustionAnalysis:

    exhausted: bool

    exhaustion_date: date | None

    balance_before_exhaustion: Money | None

    negative_balance: Money | None
