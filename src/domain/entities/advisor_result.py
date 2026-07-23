
from __future__ import annotations

from dataclasses import dataclass

from .intervention_simulation import InterventionSimulation


@dataclass(frozen=True, slots=True)
class AdvisorResult:

    best: InterventionSimulation | None

    ranking: list[InterventionSimulation]
