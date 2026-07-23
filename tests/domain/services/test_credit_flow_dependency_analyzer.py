
from src.domain.services import CreditFlowDependencyAnalyzer


def test_should_create_credit_flow_dependency():

    analyzer = CreditFlowDependencyAnalyzer()

    assert analyzer is not None
