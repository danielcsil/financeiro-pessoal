
from src.domain.services import RecoveryStrategyEngine


def test_should_create_recovery_strategy_engine():

    engine = RecoveryStrategyEngine()

    assert engine is not None
