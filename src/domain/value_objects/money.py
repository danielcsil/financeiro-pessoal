
"""
Money Value Object.

Representa um valor monetário imutável.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from typing import Union


Number = Union[int, float, Decimal]


@dataclass(frozen=True, slots=True)
class Money:

    value: Decimal

    def __post_init__(self) -> None:
        amount = self._to_decimal(self.value)
        object.__setattr__(
            self,
            "value",
            amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        )

    @staticmethod
    def _to_decimal(value: Number | Decimal) -> Decimal:
        if isinstance(value, Decimal):
            return value
        return Decimal(str(value))

    @classmethod
    def zero(cls) -> "Money":
        return cls(Decimal("0.00"))

    @classmethod
    def from_float(cls, value: float) -> "Money":
        return cls(value)

    @classmethod
    def from_decimal(cls, value: Decimal) -> "Money":
        return cls(value)

    def to_decimal(self) -> Decimal:
        return self.value

    def to_float(self) -> float:
        return float(self.value)

    def is_zero(self) -> bool:
        return self.value == Decimal("0.00")

    def is_positive(self) -> bool:
        return self.value > Decimal("0.00")

    def is_negative(self) -> bool:
        return self.value < Decimal("0.00")

    def copy(self) -> "Money":
        return Money(self.value)

    def __add__(self, other: "Money") -> "Money":
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.value + other.value)

    def __sub__(self, other: "Money") -> "Money":
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.value - other.value)

    def __mul__(self, other: Number) -> "Money":
        return Money(self.value * self._to_decimal(other))

    def __rmul__(self, other: Number) -> "Money":
        return self * other

    def __truediv__(self, other: Number) -> "Money":
        return Money(self.value / self._to_decimal(other))

    def __neg__(self) -> "Money":
        return Money(-self.value)

    def __abs__(self) -> "Money":
        return Money(abs(self.value))

    def __str__(self) -> str:
        return f"R$ {self.value:,.2f}"

    def __repr__(self) -> str:
        return f"Money({self.value})"
