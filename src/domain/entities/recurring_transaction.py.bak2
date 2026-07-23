
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from src.domain.entities import Account, Category
from src.domain.entities.recurrence_frequency import RecurrenceFrequency
from src.domain.value_objects import Money


@dataclass(frozen=True, slots=True)
class RecurringTransaction:

    description: str
    amount: Money
    account: Account
    category: Category

    start_date: date
    end_date: date

    frequency: RecurrenceFrequency
