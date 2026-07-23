
from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class FinancialDecision:

    transaction_id: str

    original_date: date

    new_date: date

    reason: str = ""
