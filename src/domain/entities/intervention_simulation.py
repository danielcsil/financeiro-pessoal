
from __future__ import annotations

from dataclasses import dataclass

from .simulation_result import SimulationResult


@dataclass(frozen=True, slots=True)
class InterventionSimulation:

    intervention: object

    result: SimulationResult

    score: float
