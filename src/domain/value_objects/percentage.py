
"""
Percentage Value Object.

Representa um percentual imutável.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from typing import Union

Number = Union[int, float, Decimal]


@dataclass(frozen=True, slots=True)
class Percentage:

    value: Decimal

    def __post_init__(self) -> None:
        amount = self._to_decimal(self.value)
        object.__setattr__(
            self,
            "value",
            amount.quantize(
                Decimal("0.0001"),
                rounding=ROUND_HALF_UP,
            ),
        )

    @staticmethod
    def _to_decimal(value: Number | Decimal) -> Decimal:
        if isinstance(value, Decimal):
            return value
        return Decimal(str(value))

    @classmethod
    def zero(cls) -> "Percentage":
        return cls(Decimal("0"))

    @classmethod
    def from_factor(cls, factor: Number) -> "Percentage":
        return cls(cls._to_decimal(factor) * Decimal("100"))

    def to_decimal(self) -> Decimal:
        return self.value

    def factor(self) -> Decimal:
        return self.value / Decimal("100")

    def apply(self, amount) -> Decimal:
        return amount.to_decimal() * self.factor()

    def is_zero(self) -> bool:
        return self.value == Decimal("0")

    def is_positive(self) -> bool:
        return self.value > Decimal("0")

    def is_negative(self) -> bool:
        return self.value < Decimal("0")

    def __add__(self, other: "Percentage") -> "Percentage":
        if not isinstance(other, Percentage):
            return NotImplemented
        return Percentage(self.value + other.value)

    def __sub__(self, other: "Percentage") -> "Percentage":
        if not isinstance(other, Percentage):
            return NotImplemented
        return Percentage(self.value - other.value)

    def __mul__(self, other: Number) -> Decimal:
        return self.factor() * self._to_decimal(other)

    def __truediv__(self, other: Number) -> Decimal:
        return self.value / self._to_decimal(other)

    def __neg__(self) -> "Percentage":
        return Percentage(-self.value)

    def __abs__(self) -> "Percentage":
        return Percentage(abs(self.value))

    def __str__(self) -> str:
        return f"{self.value.normalize()}%"

    def __repr__(self) -> str:
        return f"Percentage({self.value})"
