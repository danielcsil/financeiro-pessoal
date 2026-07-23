
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RecoveryStrategy:
    """
    Representa uma estratégia candidata para reduzir
    ou eliminar a dependência de financiamento do fluxo.
    """

    name: str

    description: str

    expected_benefit: str

    recommended: bool
