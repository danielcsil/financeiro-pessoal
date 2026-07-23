
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class CashFlowFinancingCycle:
    """
    Representa um ciclo contínuo no qual o fluxo de caixa
    depende de financiamento externo para permanecer viável.
    """

    start_date: date

    end_date: date | None

    origin: str

    maximum_financing_need: Money

    estimated_recovery_date: date | None
