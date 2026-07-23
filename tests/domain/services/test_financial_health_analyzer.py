
from src.domain.services import FinancialHealthAnalyzer


def test_should_create_health_analyzer():

    analyzer = FinancialHealthAnalyzer()

    assert analyzer is not None
