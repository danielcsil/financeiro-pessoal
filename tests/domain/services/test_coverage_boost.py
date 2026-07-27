from __future__ import annotations

from datetime import date
from types import SimpleNamespace

import pytest

from src.domain.entities import (
    Account,
    Category,
    CashFlowProjection,
    CashFlowTimeline,
    FinancialHealthLevel,
    ProjectionDay,
    RecurringTransaction,
    ScenarioAdjustment,
    ScenarioAdjustmentType,
    Transaction,
)
from src.domain.entities.expense_nature import ExpenseNature
from src.domain.entities.recurrence_frequency import RecurrenceFrequency
from src.domain.enums import AccountType, CategoryType, TransactionType
from src.domain.services import (
    CashFlowProjector,
    CashFlowRecoveryPlanner,
    FinancialHealthAnalyzer,
    LiquidityAnalyzer,
    LiquidityEventAnalyzer,
    PlanEvaluator,
    RecurringTransactionExpander,
    SafeDailySpendingCalculator,
    ScenarioApplier,
    StrategyGenerator,
    AvailableCashAnalyzer,
)
from src.domain.services import cash_flow_recovery_planner as recovery_module
from src.domain.services import financial_health_analyzer as health_module
from src.domain.services import plan_evaluator as evaluator_module
from src.domain.value_objects import DailyCashFlow, Money


class IterableDay:
    def __init__(self, day_date: date, transactions: list[Transaction]):
        self.date = day_date
        self._transactions = transactions

    def __iter__(self):
        return iter(self._transactions)


def make_account() -> Account:
    return Account(
        name="Conta",
        type=AccountType.CHECKING,
    )


def make_category(
    *,
    name: str = "Mercado",
    category_type=CategoryType.EXPENSE,
):
    return Category(
        name=name,
        type=category_type,
    )


def make_transaction(
    *,
    description: str = "Despesa",
    amount: Money = Money(100),
    transaction_type: TransactionType = TransactionType.EXPENSE,
    transaction_date: date = date(2026, 8, 1),
    nature: ExpenseNature = ExpenseNature.ESSENTIAL,
) -> Transaction:
    return Transaction(
        account=make_account(),
        category=make_category(
            category_type=(
                CategoryType.INCOME
                if transaction_type == TransactionType.INCOME
                else CategoryType.EXPENSE
            ),
        ),
        type=transaction_type,
        amount=amount,
        transaction_date=transaction_date,
        description=description,
        nature=nature,
    )


def make_projection(closing_balances: list[Money]) -> CashFlowProjection:
    projection = CashFlowProjection()

    current_date = date(2026, 8, 1)
    opening_balance = closing_balances[0]

    for index, closing_balance in enumerate(closing_balances):
        opening = opening_balance if index == 0 else closing_balances[index - 1]

        projection.add_day(
            ProjectionDay(
                date=current_date,
                opening_balance=opening,
                daily_cash_flow=DailyCashFlow.zero(),
                closing_balance=closing_balance,
            )
        )

        current_date = date.fromordinal(current_date.toordinal() + 1)

    return projection


def test_financial_health_analyzer_should_cover_all_branches(monkeypatch):
    monkeypatch.setattr(
        health_module.CapitalNeedAnalyzer,
        "analyze",
        lambda self, projection, safety_margin=Money.zero(): SimpleNamespace(
            already_sufficient=True,
        ),
    )
    monkeypatch.setattr(
        health_module.CreditDependencyAnalyzer,
        "analyze",
        lambda self, projection: SimpleNamespace(depends_on_credit=False),
    )

    healthy = FinancialHealthAnalyzer().analyze(object())
    assert healthy.level == FinancialHealthLevel.HEALTHY

    monkeypatch.setattr(
        health_module.CapitalNeedAnalyzer,
        "analyze",
        lambda self, projection, safety_margin=Money.zero(): SimpleNamespace(
            already_sufficient=False,
        ),
    )

    attention = FinancialHealthAnalyzer().analyze(object())
    assert attention.level == FinancialHealthLevel.ATTENTION

    monkeypatch.setattr(
        health_module.CreditDependencyAnalyzer,
        "analyze",
        lambda self, projection: SimpleNamespace(depends_on_credit=True),
    )

    critical = FinancialHealthAnalyzer().analyze(object())
    assert critical.level == FinancialHealthLevel.CRITICAL


def test_plan_evaluator_should_score_health_and_goal(monkeypatch):
    monkeypatch.setattr(
        evaluator_module.FinancialHealthAnalyzer,
        "analyze",
        lambda self, projection: SimpleNamespace(
            level=SimpleNamespace(name="ATTENTION"),
        ),
    )
    monkeypatch.setattr(
        evaluator_module.GoalAnalyzer,
        "analyze",
        lambda self, projection, goal: SimpleNamespace(achieved=True),
    )

    result = PlanEvaluator().evaluate(object(), goal=object())

    assert result.feasible
    assert result.score == 80


def test_plan_evaluator_should_penalize_unmet_goal(monkeypatch):
    monkeypatch.setattr(
        evaluator_module.FinancialHealthAnalyzer,
        "analyze",
        lambda self, projection: SimpleNamespace(
            level=SimpleNamespace(name="CRITICAL"),
        ),
    )
    monkeypatch.setattr(
        evaluator_module.GoalAnalyzer,
        "analyze",
        lambda self, projection, goal: SimpleNamespace(achieved=False),
    )

    result = PlanEvaluator().evaluate(object(), goal=object())

    assert not result.feasible
    assert result.score == 20


@pytest.mark.parametrize(
    ("required", "capacity", "expected_months"),
    [
        (300, 100, 3),
        (250, 100, 3),
        (100, 0, 0),
    ],
)
def test_cash_flow_recovery_planner_should_calculate_months(
    monkeypatch,
    required: int,
    capacity: int,
    expected_months: int,
):
    monkeypatch.setattr(
        recovery_module.CapitalNeedAnalyzer,
        "analyze",
        lambda self, projection: SimpleNamespace(
            required_capital=Money(required),
        ),
    )

    plan = CashFlowRecoveryPlanner().build(object(), Money(capacity))

    assert plan.required_capital == Money(required)
    assert plan.estimated_months_to_recover == expected_months


def test_safe_daily_spending_calculator_should_handle_positive_and_zero_days():
    calculator = SafeDailySpendingCalculator()

    positive = calculator.calculate(Money(300), 3)
    assert positive.recommended_daily_limit == Money(100)

    zero_days = calculator.calculate(Money(300), 0)
    assert zero_days.recommended_daily_limit == Money(300)


def test_liquidity_event_analyzer_should_detect_large_events():
    class Day:
        def __init__(self, day_date: date, transactions: list[SimpleNamespace]):
            self.date = day_date
            self._transactions = transactions

        def __iter__(self):
            return iter(self._transactions)

    timeline = [
        Day(
            date(2026, 8, 1),
            [
                SimpleNamespace(
                    amount=Money(50),
                    description="Small",
                )
            ],
        ),
        Day(
            date(2026, 8, 2),
            [
                SimpleNamespace(
                    amount=Money(-120),
                    description="Large",
                )
            ],
        ),
    ]

    events = LiquidityEventAnalyzer().analyze(timeline, Money(100))

    assert len(events) == 1
    assert events[0].date == date(2026, 8, 2)
    assert events[0].impact == Money(-120)


def test_liquidity_analyzer_should_track_negative_balance():
    projection = make_projection(
        [
            Money(100),
            Money(-50),
            Money(-20),
        ]
    )

    analysis = LiquidityAnalyzer().analyze(projection)

    assert analysis.minimum_balance == Money(-50)
    assert analysis.maximum_balance == Money(100)
    assert analysis.ending_balance == Money(-20)
    assert analysis.first_negative_day == date(2026, 8, 2)
    assert analysis.negative_days == 2
    assert analysis.has_negative_balance


def test_available_cash_analyzer_should_zero_negative_amount():
    projection = CashFlowProjection()
    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 1),
            opening_balance=Money(100),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(120),
        )
    )
    projection.add_day(
        ProjectionDay(
            date=date(2026, 8, 2),
            opening_balance=Money(120),
            daily_cash_flow=DailyCashFlow.zero(),
            closing_balance=Money(130),
        )
    )

    analysis = AvailableCashAnalyzer().analyze(projection)

    assert analysis.current_balance == Money(100)
    assert analysis.minimum_future_balance == Money(120)
    assert analysis.available_to_spend == Money.zero()


def test_cash_flow_projector_should_sum_transaction_types():
    timeline = CashFlowTimeline(
        date(2026, 8, 1),
        date(2026, 8, 1),
    )

    day = timeline.day(date(2026, 8, 1))
    day.add_transaction(
        make_transaction(
            description="Salary",
            amount=Money(1000),
            transaction_type=TransactionType.INCOME,
            transaction_date=date(2026, 8, 1),
        )
    )
    day.add_transaction(
        make_transaction(
            description="Rent",
            amount=Money(200),
            transaction_type=TransactionType.EXPENSE,
            transaction_date=date(2026, 8, 1),
        )
    )
    day.add_transaction(
        make_transaction(
            description="Adjustment",
            amount=Money(50),
            transaction_type=TransactionType.ADJUSTMENT,
            transaction_date=date(2026, 8, 1),
        )
    )

    projection = CashFlowProjector().project(timeline, Money(100))

    assert projection.days[0].income == Money(1000)
    assert projection.days[0].expense == Money(200)
    assert projection.days[0].adjustment == Money(50)
    assert projection.days[0].closing_balance == Money(950)


def test_scenario_applier_should_remove_transaction_without_mutating_input():
    timeline = CashFlowTimeline(
        date(2026, 8, 1),
        date(2026, 8, 1),
    )

    transaction = make_transaction(
        description="Rent",
        amount=Money(200),
        transaction_type=TransactionType.EXPENSE,
        transaction_date=date(2026, 8, 1),
    )
    timeline.add_transaction(transaction)

    adjustment = ScenarioAdjustment(
        adjustment_type=ScenarioAdjustmentType.REMOVE_TRANSACTION,
        transaction=transaction,
    )

    result = ScenarioApplier().apply(timeline, [adjustment])

    assert len(timeline.day(date(2026, 8, 1))) == 1
    assert len(result.day(date(2026, 8, 1))) == 0


def test_strategy_generator_should_attach_candidate_payload():
    candidate = make_transaction(
        description="Optional expense",
        amount=Money(75),
        transaction_type=TransactionType.EXPENSE,
        transaction_date=date(2026, 8, 10),
        nature=ExpenseNature.DISCRETIONARY,
    )

    financial_plan = SimpleNamespace(
        timeline=[
            IterableDay(
                date(2026, 8, 10),
                [candidate],
            )
        ]
    )
    diagnosis = SimpleNamespace(
        has_financing_dependency=False,
        has_negative_balance=True,
    )

    strategies = StrategyGenerator().generate(
        financial_plan,
        diagnosis,
    )

    assert len(strategies) == 1
    assert strategies[0].type == "POSTPONE_EXPENSE"
    assert strategies[0].payload == candidate


@pytest.mark.parametrize(
    ("frequency", "start", "end", "expected_dates"),
    [
        (
            RecurrenceFrequency.DAILY,
            date(2026, 8, 1),
            date(2026, 8, 3),
            [
                date(2026, 8, 1),
                date(2026, 8, 2),
                date(2026, 8, 3),
            ],
        ),
        (
            RecurrenceFrequency.MONTHLY,
            date(2026, 1, 15),
            date(2026, 3, 15),
            [
                date(2026, 1, 15),
                date(2026, 2, 15),
                date(2026, 3, 15),
            ],
        ),
        (
            RecurrenceFrequency.YEARLY,
            date(2026, 1, 15),
            date(2028, 1, 15),
            [
                date(2026, 1, 15),
                date(2027, 1, 15),
                date(2028, 1, 15),
            ],
        ),
    ],
)
def test_recurring_transaction_expander_should_handle_frequencies(
    frequency,
    start,
    end,
    expected_dates,
):
    recurring = RecurringTransaction(
        description="Subscription",
        amount=Money(50),
        account=make_account(),
        category=make_category(),
        start_date=start,
        end_date=end,
        frequency=frequency,
    )

    transactions = RecurringTransactionExpander().expand(recurring)

    assert [transaction.transaction_date for transaction in transactions] == expected_dates
