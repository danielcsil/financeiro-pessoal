
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True, slots=True)
class EvaluatedIntervention:
    intervention: Any
    score: float


class MinimalInterventionEngine:
    """
    Motor genérico para avaliação de intervenções.

    Todo o processo de decisão é baseado em funções
    injetadas pelo domínio (Strategy Pattern).
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
            item
            for item in self.rank(interventions, evaluator)
            if item.score < baseline_score
        ]


    def explain(
        self,
        candidate: EvaluatedIntervention,
        baseline_score: float,
    ) -> dict:

        improvement = baseline_score - candidate.score

        return {
            "intervention": candidate.intervention,
            "score": candidate.score,
            "baseline_score": baseline_score,
            "improvement": improvement,
            "improvement_percent": (
                round(improvement / baseline_score * 100, 2)
                if baseline_score > 0 else 0.0
            ),
        }


    def recommend(
        self,
        interventions,
        evaluator: Callable[[Any], float],
        baseline_score: float,
        validator: Callable[[Any], bool] | None = None,
    ) -> dict | None:
        """
        Gera uma recomendação utilizando apenas
        intervenções válidas.
        """

        if validator is not None:
            interventions = [
                i
                for i in interventions
                if validator(i)
            ]

        best = self.evaluate(
            interventions,
            evaluator,
        )

        if best is None:
            return None

        return self.explain(
            best,
            baseline_score,
        )
