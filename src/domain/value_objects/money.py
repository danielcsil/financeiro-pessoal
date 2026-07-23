
"""
Representa um valor monetário utilizando Decimal.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP


@dataclass(frozen=True, slots=True)
class Money:

    value: Decimal

    def __init__(self, value):
        object.__setattr__(
            self,
            "value",
            Decimal(str(value)).quantize(
                Decimal("0.01"),
                rounding=ROUND_HALF_UP,
            ),
        )

    def __str__(self) -> str:
        valor = f"{self.value:,.2f}"
        valor = valor.replace(",", "X").replace(".", ",").replace("X", ".")
        return f"R$ {valor}"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        return Money(self.value + other.value)

    def __sub__(self, other):
        return Money(self.value - other.value)

    def __mul__(self, other):
        return Money(self.value * Decimal(str(other)))

    def __truediv__(self, other):
        return Money(self.value / Decimal(str(other)))

    def __neg__(self):
        return Money(-self.value)

    def __abs__(self):
        return Money(abs(self.value))

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __eq__(self, other):
        if not isinstance(other, Money):
            return False
        return self.value == other.value

    def to_decimal(self):
        return self.value

    def to_float(self):
        return float(self.value)
