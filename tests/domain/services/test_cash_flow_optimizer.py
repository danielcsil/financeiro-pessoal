
from src.domain.services import CashFlowOptimizer


def test_should_optimize(financial_plan):

    optimizer = CashFlowOptimizer()

    interventions = [
        "A",
        "B",
        "C",
    ]

    result = optimizer.optimize(
        financial_plan=financial_plan,
        interventions=interventions,
        scorer=lambda simulation: (
            simulation.liquidity.minimum_balance
        ),
    )

    assert result.best is not None

    assert result.evaluated_combinations > 0


def test_should_keep_best_first(financial_plan):

    optimizer = CashFlowOptimizer()

    interventions = [
        "A",
        "B",
    ]

    result = optimizer.optimize(
        financial_plan=financial_plan,
        interventions=interventions,
        scorer=lambda simulation: (
            simulation.liquidity.minimum_balance
        ),
    )

    assert result.best == result.combinations[0]
