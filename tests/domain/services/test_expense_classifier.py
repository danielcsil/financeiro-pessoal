
from src.domain.entities import ExpenseNature
from src.domain.services import ExpenseClassifier


class DummyTransaction:

    def __init__(self, nature):
        self.nature = nature


def test_should_identify_essential_transaction():

    classifier = ExpenseClassifier()

    tx = DummyTransaction(ExpenseNature.ESSENTIAL)

    assert classifier.is_essential(tx)
