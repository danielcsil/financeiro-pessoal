
from __future__ import annotations

from src.domain.entities import (
    CashFlowProjection,
    ProjectionDay,
)
from src.domain.value_objects import (
    DailyCashFlow,
    Money,
)


class CashFlowProjector:

    def project(
        self,
        timeline,
        opening_balance: Money,
    ) -> CashFlowProjection:

        projection = CashFlowProjection()

        balance = opening_balance

        for day in timeline:

            income = Money.zero()
            expense = Money.zero()
            adjustment = Money.zero()

            for transaction in day:

                if transaction.is_income():
                    income += transaction.amount

                elif transaction.is_expense():
                    expense += transaction.amount

                elif transaction.is_adjustment():
                    adjustment += transaction.amount

            summary = DailyCashFlow(
                income=income,
                expense=expense,
                adjustment=adjustment,
            )

            opening = balance
            closing = opening + summary.net_change

            projection.add_day(
                ProjectionDay(
                    date=day.date,
                    opening_balance=opening,
                    daily_cash_flow=summary,
                    closing_balance=closing,
                )
            )

            balance = closing

        return projection
