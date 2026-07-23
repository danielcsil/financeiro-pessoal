
from src.domain.services import FinancialAdvisor


def test_should_create_financial_advisor():

    advisor = FinancialAdvisor()

    assert advisor is not None
