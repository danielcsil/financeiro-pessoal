
from __future__ import annotations

from src.domain.entities import Recommendation


class RecommendationEngine:

    def generate(self, analysis):

        recommendations = []

        if analysis.has_negative_balance:

            recommendations.append(
                Recommendation(
                    title="Saldo negativo previsto",
                    description=(
                        "Seu fluxo de caixa ficará negativo. "
                        "Revise despesas ou antecipe receitas."
                    ),
                    priority=1,
                )
            )

        if analysis.negative_days >= 7:

            recommendations.append(
                Recommendation(
                    title="Período prolongado de saldo negativo",
                    description=(
                        "O saldo permanecerá negativo por vários dias."
                    ),
                    priority=2,
                )
            )

        if analysis.ending_balance.is_negative():

            recommendations.append(
                Recommendation(
                    title="Encerramento do período negativo",
                    description=(
                        "A projeção termina com saldo negativo."
                    ),
                    priority=1,
                )
            )

        return sorted(
            recommendations,
            key=lambda r: r.priority
        )
