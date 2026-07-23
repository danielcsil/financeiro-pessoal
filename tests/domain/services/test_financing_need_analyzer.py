
from src.domain.services import FinancingNeedAnalyzer


def test_should_create_financing_need_analyzer():

    analyzer = FinancingNeedAnalyzer()

    assert analyzer is not None
