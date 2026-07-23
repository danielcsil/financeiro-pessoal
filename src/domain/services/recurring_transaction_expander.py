
from __future__ import annotations

from datetime import timedelta

from src.domain.entities import Transaction


class RecurringTransactionExpander:

    def expand(self, recurring):

        current = recurring.start_date

        transactions = []

        while current <= recurring.end_date:

            transactions.append(
                Transaction(
                    description=recurring.description,
                    amount=recurring.amount,
                    account=recurring.account,
                    category=recurring.category,
                    date=current,
                )
            )

            if recurring.frequency.name == "DAILY":
                current += timedelta(days=1)

            elif recurring.frequency.name == "WEEKLY":
                current += timedelta(days=7)

            elif recurring.frequency.name == "MONTHLY":
                current = current.replace(month=current.month + 1)

            elif recurring.frequency.name == "YEARLY":
                current = current.replace(year=current.year + 1)

        return transactions
