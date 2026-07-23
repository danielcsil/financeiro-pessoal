from datetime import date

from src.domain.entities import (
    Account,
    CashFlowTimeline,
    Category,
    FinancialPlan,
    PlanningPeriod,
    ScenarioAdjustment,
)
from src.domain.entities.scenario_adjustment_type import (
    ScenarioAdjustmentType,
)
from src.domain.entities.expense_nature import ExpenseNature
from src.domain.entities.transaction import Transaction

from src.domain.enums import (
    AccountType,
    CategoryType,
    TransactionType,
)

from src.domain.services import CashFlowOptimizer
from src.domain.value_objects import Money


def create_financial_plan() -> FinancialPlan:
    period = PlanningPeriod(
        start_date=date(2026, 1, 1),
        end_date=date(2026, 12, 31),
    )

    return FinancialPlan(
        period=period,
        opening_balance=Money(1000),
        timeline=CashFlowTimeline(
            period.start_date,
            period.end_date,
        ),
    )


def create_account() -> Account:
    return Account(
        name="Conta Corrente",
        type=AccountType.CHECKING,
    )


def create_income_category() -> Category:
    return Category(
        name="Receita",
        type=CategoryType.INCOME,
    )


def create_adjustment(amount: int) -> ScenarioAdjustment:
    transaction = Transaction(
        account=create_account(),
        category=create_income_category(),
        type=TransactionType.INCOME,
        amount=Money(amount),
        transaction_date=date(2026, 1, 10),
        description=f"Ajuste {amount}",
        nature=ExpenseNature.ESSENTIAL,
    )

    return ScenarioAdjustment(
        adjustment_type=ScenarioAdjustmentType.ADD_TRANSACTION,
        transaction=transaction,
    )


def test_should_optimize():

    financial_plan = create_financial_plan()

    optimizer = CashFlowOptimizer()

    interventions = [
        create_adjustment(100),
        create_adjustment(500),
        create_adjustment(1000),
    ]

    result = optimizer.optimize(
        financial_plan=financial_plan,
        interventions=interventions,
        scorer=lambda simulation: simulation.liquidity.minimum_balance,
    )

    assert result.best is not None
    assert result.evaluated_combinations > 0
    assert len(result.combinations) == result.evaluated_combinations


def test_should_keep_best_first():

    financial_plan = create_financial_plan()

    optimizer = CashFlowOptimizer()

    interventions = [
        create_adjustment(100),
        create_adjustment(500),
    ]

    result = optimizer.optimize(
        financial_plan=financial_plan,
        interventions=interventions,
        scorer=lambda simulation: simulation.liquidity.minimum_balance,
    )

    assert result.best == result.combinations[0]