
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True, slots=True)
class EvaluatedIntervention:
    intervention: Any
    score: float
    metadata: dict[str, Any] | None = None


class MinimalInterventionEngine:

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


    def recommend(
        self,
        interventions,
        evaluator,
        baseline_score: float,
        validator=None,
        metadata_provider=None,
    ):

        candidates = [
            intervention
            for intervention in interventions
            if validator is None or validator(intervention)
        ]

        best = self.evaluate(
            candidates,
            evaluator,
            metadata_provider,
        )

        if best is None:
            return None

        return self.explain(best, baseline_score)


    def recommend_all(
        self,
        interventions,
        evaluator,
        baseline_score: float,
        validator=None,
        metadata_provider=None,
    ) -> list[dict]:

        candidates = [
            intervention
            for intervention in interventions
            if validator is None or validator(intervention)
        ]

        ranking = self.rank(
            candidates,
            evaluator,
            metadata_provider,
        )

        return [
            self.explain(candidate, baseline_score)
            for candidate in ranking
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
            "metadata": candidate.metadata or {},
        }


    def compare(
        self,
        ranking: list[EvaluatedIntervention],
    ) -> list[dict]:

        if not ranking:
            return []

        best_score = ranking[0].score

        comparison = []

        for item in ranking:

            comparison.append({
                "intervention": item.intervention,
                "score": item.score,
                "gap_to_best": item.score - best_score,
                "metadata": item.metadata or {},
            })

        return comparison
