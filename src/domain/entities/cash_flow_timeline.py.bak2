
from __future__ import annotations

from datetime import date, timedelta

from src.domain.entities import TimelineDay, Transaction


class CashFlowTimeline:

    def __init__(
        self,
        start_date: date,
        end_date: date,
    ):
        if end_date < start_date:
            raise ValueError(
                "End date must be greater than or equal to start date."
            )

        self._days: dict[date, TimelineDay] = {}

        current = start_date

        while current <= end_date:
            self._days[current] = TimelineDay(current)
            current += timedelta(days=1)

    @property
    def start_date(self) -> date:
        return min(self._days.keys())

    @property
    def end_date(self) -> date:
        return max(self._days.keys())

    @property
    def days(self) -> tuple[TimelineDay, ...]:
        return tuple(self._days.values())

    def day(self, day: date) -> TimelineDay:
        return self._days[day]

    def add_transaction(
        self,
        transaction: Transaction,
    ) -> None:
        self.day(
            transaction.transaction_date
        ).add_transaction(transaction)
