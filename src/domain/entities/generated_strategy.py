
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GeneratedStrategy:

    type: str

    description: str

    payload: object | None = None
