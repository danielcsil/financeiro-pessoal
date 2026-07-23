
"""
Representa um percentual.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class Percentage:

    value: Decimal

    def __init__(self, value):
        object.__setattr__(
            self,
            "value",
            Decimal(str(value))
        )

    @property
    def factor(self):
        return self.value / Decimal("100")

    def __str__(self):
        return f"{self.value}%"
