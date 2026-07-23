
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True, slots=True)
class EvaluatedIntervention:
    intervention: Any
    score: float


class MinimalInterventionEngine:
    """
    Avalia, ordena e filtra intervenções.

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


    def filter_improvements(
        self,
        interventions,
        evaluator: Callable[[Any], float],
        baseline_score: float,
    ) -> list[EvaluatedIntervention]:
        """
        Retorna apenas intervenções que produzem
        melhoria em relação ao cenário atual.
        """

        return [
            candidate
            for candidate in self.rank(interventions, evaluator)
            if candidate.score < baseline_score
        ]
