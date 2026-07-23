
from src.domain.services import FinancialDecisionSimulator


def test_should_create_financial_decision_simulator():

    simulator = FinancialDecisionSimulator()

    assert simulator is not None
