
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PlanEvaluation:

    feasible: bool

    score: int

    summary: str
