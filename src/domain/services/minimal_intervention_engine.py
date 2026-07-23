
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True, slots=True)
class EvaluatedIntervention:
    intervention: Any
    score: float
    metadata: dict[str, Any] | None = None


class MinimalInterventionEngine:
    """
    Motor genérico para avaliação de intervenções.

    Toda regra de negócio é injetada através de funções,
    mantendo o mecanismo desacoplado do domínio financeiro.
    """

    def rank(
        self,
        interventions,
        evaluator: Callable[[Any], float],
        metadata_provider: Callable[[Any], dict] | None = None,
    ) -> list[EvaluatedIntervention]:

        ranking = []

        for intervention in interventions:

            ranking.append(
                EvaluatedIntervention(
                    intervention=intervention,
                    score=evaluator(intervention),
                    metadata=(
                        metadata_provider(intervention)
                        if metadata_provider
                        else None
                    ),
                )
            )

        ranking.sort(key=lambda item: item.score)

        return ranking


    def evaluate(
        self,
        interventions,
        evaluator,
        metadata_provider=None,
    ):

        ranking = self.rank(
            interventions,
            evaluator,
            metadata_provider,
        )

        return ranking[0] if ranking else None


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
            "metadata": candidate.metadata or {},
        }


    def recommend(
        self,
        interventions,
        evaluator,
        baseline_score,
        metadata_provider=None,
        validator=None,
    ) -> dict | None:

        if validator is not None:
            interventions = [
                i
                for i in interventions
                if validator(i)
            ]

        candidate = self.evaluate(
            interventions=interventions,
            evaluator=evaluator,
            metadata_provider=metadata_provider,
        )

        if candidate is None:
            return None

        return self.explain(
            candidate,
            baseline_score,
        )


    def recommend_all(
        self,
        interventions,
        evaluator,
        baseline_score,
        metadata_provider=None,
        validator=None,
    ) -> list[dict]:
        """
        Retorna todas as intervenções válidas,
        ordenadas da melhor para a pior.
        """

        if validator is not None:
            interventions = [
                i
                for i in interventions
                if validator(i)
            ]

        ranking = self.rank(
            interventions,
            evaluator,
            metadata_provider,
        )

        return [
            self.explain(item, baseline_score)
            for item in ranking
        ]
