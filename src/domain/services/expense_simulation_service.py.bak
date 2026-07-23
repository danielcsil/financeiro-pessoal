
from __future__ import annotations

from src.domain.entities import (
    ExpenseSimulationResult,
)
from src.domain.services import (
    RecurringExpenseCapacityAnalyzer,
)
from src.domain.value_objects import Money


class ExpenseSimulationService:

    def simulate(
        self,
        projection,
        expense: Money,
        safety_margin: Money = Money.zero(),
    ) -> ExpenseSimulationResult:

        analysis = RecurringExpenseCapacityAnalyzer().analyze(
            projection,
            safety_margin,
        )

        approved = expense <= analysis.maximum_recurring_expense

        remaining = analysis.maximum_recurring_expense - expense

        if remaining.is_negative():
            remaining = Money.zero()

        message = (
            "Nova despesa recorrente aprovada."
            if approved
            else "Nova despesa recorrente compromete o fluxo de caixa."
        )

        return ExpenseSimulationResult(
            approved=approved,
            simulated_expense=expense,
            remaining_margin=remaining,
            message=message,
        )
