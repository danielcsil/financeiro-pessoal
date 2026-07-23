
from types import SimpleNamespace

from src.domain.services import StrategyGenerator


def test_should_generate_financing_strategies():

    diagnosis = SimpleNamespace(
        has_financing_dependency=True,
        has_negative_balance=False,
    )

    generator = StrategyGenerator()

    result = generator.generate(diagnosis)

    assert len(result) == 2


def test_should_generate_negative_balance_strategy():

    diagnosis = SimpleNamespace(
        has_financing_dependency=False,
        has_negative_balance=True,
    )

    generator = StrategyGenerator()

    result = generator.generate(diagnosis)

    assert result[0].type == "POSTPONE_EXPENSE"
