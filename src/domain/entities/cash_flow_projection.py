
from __future__ import annotations

from datetime import date

from .projection_day import ProjectionDay


class CashFlowProjection:

    def __init__(self):
        self._days: list[ProjectionDay] = []

    def add_day(self, day: ProjectionDay) -> None:
        self._days.append(day)

    @property
    def days(self) -> tuple[ProjectionDay, ...]:
        return tuple(self._days)

    def day(self, date_: date) -> ProjectionDay:
        for day in self._days:
            if day.date == date_:
                return day
        raise KeyError(date_)

    @property
    def start_date(self) -> date:
        return self._days[0].date

    @property
    def end_date(self) -> date:
        return self._days[-1].date

    def __iter__(self):
        return iter(self._days)

    def __len__(self):
        return len(self._days)
