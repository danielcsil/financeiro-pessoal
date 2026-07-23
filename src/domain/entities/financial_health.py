
from __future__ import annotations

from dataclasses import dataclass

from .financial_health_level import FinancialHealthLevel


@dataclass(frozen=True, slots=True)
class FinancialHealth:

    level: FinancialHealthLevel

    summary: str
