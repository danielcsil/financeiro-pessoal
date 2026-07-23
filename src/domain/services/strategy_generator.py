
from __future__ import annotations

from src.domain.entities import GeneratedStrategy


class StrategyGenerator:
    """
    Gera automaticamente estratégias financeiras
    candidatas.

    Nesta primeira versão o mecanismo utiliza regras
    heurísticas simples.
    """

    def generate(self, diagnosis):

        strategies = []

        if diagnosis.has_financing_dependency:

            strategies.append(
                GeneratedStrategy(
                    type="CHANGE_DUE_DATE",
                    description="Alterar vencimento do cartão",
                )
            )

            strategies.append(
                GeneratedStrategy(
                    type="USE_CASH_RESERVE",
                    description="Utilizar parte da reserva",
                )
            )

        if diagnosis.has_negative_balance:

            strategies.append(
                GeneratedStrategy(
                    type="POSTPONE_EXPENSE",
                    description="Adiar despesa não essencial",
                )
            )

        return strategies
