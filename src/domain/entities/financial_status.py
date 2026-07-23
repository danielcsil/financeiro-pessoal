
from __future__ import annotations

from dataclasses import dataclass

from src.domain.entities.financial_status_type import FinancialStatusType
from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class FinancialStatus:

    status: FinancialStatusType
    balance: Money
