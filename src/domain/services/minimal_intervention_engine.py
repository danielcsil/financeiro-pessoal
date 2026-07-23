
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True, slots=True)
class EvaluatedIntervention:
    intervention: Any
    score: float


class MinimalInterventionEngine:
    """
    Avalia, ordena, filtra e explica intervenções.

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

        return [
            candidate
            for candidate in self.rank(interventions, evaluator)
            if candidate.score < baseline_score
        ]


    def explain(
        self,
        candidate: EvaluatedIntervention,
        baseline_score: float,
    ) -> dict:

        improvement = baseline_score - candidate.score

        improvement_percent = (
            (improvement / baseline_score) * 100
            if baseline_score > 0
            else 0.0
        )

        return {
            "intervention": candidate.intervention,
            "score": candidate.score,
            "baseline_score": baseline_score,
            "improvement": improvement,
            "improvement_percent": round(improvement_percent, 2),
        }
