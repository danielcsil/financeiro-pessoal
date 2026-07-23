
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class CreditDependencyAnalysis:

    depends_on_credit: bool

    first_credit_day: date | None

    required_credit: Money

    days_using_credit: int
