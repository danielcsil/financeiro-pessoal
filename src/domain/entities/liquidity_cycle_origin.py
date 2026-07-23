
from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class LiquidityCycleOrigin:

    start_date: date

    triggering_event: str

    explanation: str
