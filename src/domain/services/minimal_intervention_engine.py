
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True, slots=True)
class EvaluatedIntervention:
    intervention: Any
    score: float


class MinimalInterventionEngine:
    """
    Avalia múltiplas intervenções e retorna aquela que
    produz o melhor resultado segundo uma função de score.

    Quanto menor o score, melhor a intervenção.
    """

    def evaluate(
        self,
        interventions,
        evaluator: Callable[[Any], float],
    ) -> EvaluatedIntervention | None:

        best = None

        for intervention in interventions:

            score = evaluator(intervention)

            candidate = EvaluatedIntervention(
                intervention=intervention,
                score=score,
            )

            if best is None or candidate.score < best.score:
                best = candidate

        return best
