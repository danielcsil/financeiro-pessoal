
from __future__ import annotations

from src.domain.entities import (
    AdvisorReport,
)


class RecommendationExplainer:
    """
    Gera uma explicação compreensível para o usuário
    a partir do resultado da recomendação.
    """

    def create_report(
        self,
        score,
        advisor_result,
    ) -> AdvisorReport:

        if advisor_result.best is None:

            return AdvisorReport(
                score=score,
                recommendation=advisor_result,
                summary="Nenhuma intervenção foi considerada necessária.",
                highlights=(),
            )

        recommendation = advisor_result.best.intervention

        summary = (
            f"Saúde financeira: {score.overall}/100. "
            f"A melhor estratégia identificada foi "
            f"'{recommendation.description}'."
        )

        highlights = (
            f"Liquidez: {score.liquidity}/100",
            f"Reserva: {score.reserve}/100",
            f"Dependência de crédito: {score.credit_dependency}/100",
            f"Estabilidade: {score.stability}/100",
            f"Risco: {score.risk}/100",
        )

        return AdvisorReport(
            score=score,
            recommendation=advisor_result,
            summary=summary,
            highlights=highlights,
        )
