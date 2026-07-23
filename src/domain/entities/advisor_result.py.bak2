
from __future__ import annotations

from dataclasses import dataclass

from src.domain.entities import InterventionSimulation


@dataclass(frozen=True, slots=True)
class AdvisorResult:

    best: InterventionSimulation | None

    ranking: list[InterventionSimulation]
