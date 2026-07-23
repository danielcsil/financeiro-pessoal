
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class FinancingNeed:

    start_date: date

    end_date: date | None

    required_amount: Money

    financing_required: bool

    justification: str
