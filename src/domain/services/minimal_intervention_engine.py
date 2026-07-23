
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

    O cálculo do score e das evidências é totalmente
    delegado ao domínio através de funções injetadas.
    """

    def rank(
        self,
        interventions,
        evaluator: Callable[[Any], float],
        metadata_provider: Callable[[Any], dict] | None = None,
    ) -> list[EvaluatedIntervention]:

        ranking = []

        for intervention in interventions:

            metadata = (
                metadata_provider(intervention)
                if metadata_provider
                else None
            )

            ranking.append(
                EvaluatedIntervention(
                    intervention=intervention,
                    score=evaluator(intervention),
                    metadata=metadata,
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
