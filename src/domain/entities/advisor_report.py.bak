
from __future__ import annotations

from dataclasses import dataclass

from src.domain.entities import (
    AdvisorResult,
    FinancialHealthScore,
)


@dataclass(frozen=True, slots=True)
class AdvisorReport:

    score: FinancialHealthScore

    recommendation: AdvisorResult

    summary: str

    highlights: tuple[str, ...]
