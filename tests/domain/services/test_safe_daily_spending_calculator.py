
from src.domain.services import SafeDailySpendingCalculator


def test_should_create_safe_daily_spending_calculator():

    calculator = SafeDailySpendingCalculator()

    assert calculator is not None
