
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class FinancialHealthScore:

    overall: int

    liquidity: int

    reserve: int

    credit_dependency: int

    stability: int

    risk: int
