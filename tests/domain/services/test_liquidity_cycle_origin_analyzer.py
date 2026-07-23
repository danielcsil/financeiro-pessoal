
from src.domain.services import LiquidityCycleOriginAnalyzer


def test_should_create_liquidity_cycle_origin_analyzer():

    analyzer = LiquidityCycleOriginAnalyzer()

    assert analyzer is not None
