
from __future__ import annotations

from src.domain.entities import (
    IncomeSimulationResult,
)
from src.domain.services import (
    RecurringExpenseCapacityAnalyzer,
)
from src.domain.value_objects import Money


class IncomeSimulationService:

    def simulate(
        self,
        projection,
        income: Money,
        safety_margin: Money = Money.zero(),
    ) -> IncomeSimulationResult:

        analysis = RecurringExpenseCapacityAnalyzer().analyze(
            projection,
            safety_margin,
        )

        return IncomeSimulationResult(
            simulated_income=income,
            additional_margin=analysis.maximum_recurring_expense + income,
            message="A renda adicional aumenta a capacidade para novas despesas recorrentes.",
        )
