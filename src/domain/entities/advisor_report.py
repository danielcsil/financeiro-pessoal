
from __future__ import annotations

from dataclasses import dataclass

from .advisor_result import AdvisorResult
from .financial_health_score import FinancialHealthScore


@dataclass(frozen=True, slots=True)
class AdvisorReport:

    score: FinancialHealthScore

    recommendation: AdvisorResult

    summary: str

    highlights: tuple[str, ...]
