
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class CreditFlowDependency:

    start_date: date

    end_date: date | None

    financed_amount: Money
