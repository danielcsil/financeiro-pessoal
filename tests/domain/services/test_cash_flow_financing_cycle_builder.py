
from src.domain.services import CashFlowFinancingCycleBuilder


def test_should_create_cash_flow_financing_cycle_builder():

    builder = CashFlowFinancingCycleBuilder()

    assert builder is not None
