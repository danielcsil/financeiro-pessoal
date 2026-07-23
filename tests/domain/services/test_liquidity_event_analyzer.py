
from src.domain.services import LiquidityEventAnalyzer


def test_should_create_liquidity_event_analyzer():

    analyzer = LiquidityEventAnalyzer()

    assert analyzer is not None
