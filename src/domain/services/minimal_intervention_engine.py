
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True, slots=True)
class EvaluatedIntervention:
    intervention: Any
    score: float


class MinimalInterventionEngine:
    """
    Avalia e ordena intervenções por uma função de score.

    Quanto menor o score, melhor a intervenção.
    """

    def rank(
        self,
        interventions,
        evaluator: Callable[[Any], float],
    ) -> list[EvaluatedIntervention]:

        ranking = [
            EvaluatedIntervention(
                intervention=i,
                score=evaluator(i),
            )
            for i in interventions
        ]

        ranking.sort(key=lambda item: item.score)

        return ranking


    def evaluate(
        self,
        interventions,
        evaluator: Callable[[Any], float],
    ) -> EvaluatedIntervention | None:

        ranking = self.rank(interventions, evaluator)

        return ranking[0] if ranking else None
