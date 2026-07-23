
from src.domain.services import CashFlowMetricsBuilder


def test_should_create_cash_flow_metrics_builder():

    builder = CashFlowMetricsBuilder()

    assert builder is not None
