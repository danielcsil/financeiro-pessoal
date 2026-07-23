
from __future__ import annotations

from dataclasses import dataclass

from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class CapitalNeedAnalysis:

    required_capital: Money

    already_sufficient: bool

    safety_margin: Money
