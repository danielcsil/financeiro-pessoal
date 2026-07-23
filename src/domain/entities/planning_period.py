
from __future__ import annotations

from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class PlanningPeriod:

    start_date: date
    end_date: date

    @property
    def total_days(self) -> int:
        return (self.end_date - self.start_date).days + 1
