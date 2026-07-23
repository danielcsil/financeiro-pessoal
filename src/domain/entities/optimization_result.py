
from __future__ import annotations

from dataclasses import dataclass

from .intervention_simulation import InterventionSimulation


@dataclass(frozen=True, slots=True)
class OptimizationResult:

    best: InterventionSimulation | None

    evaluated_combinations: int

    combinations: tuple[InterventionSimulation, ...]
