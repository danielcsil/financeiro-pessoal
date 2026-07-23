
from src.domain.services import CashFlowCostAnalyzer


def test_should_create_cash_flow_cost_analyzer():

    analyzer = CashFlowCostAnalyzer()

    assert analyzer is not None
