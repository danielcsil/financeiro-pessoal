from src.domain.entities import GeneratedStrategy
from src.domain.entities.expense_nature import ExpenseNature
from src.domain.enums import TransactionType


class StrategyGenerator:

    def generate(
        self,
        financial_plan,
        diagnosis=None,
    ):
        if diagnosis is None:
            diagnosis = financial_plan
            financial_plan = None

        strategies = []

        if diagnosis.has_financing_dependency:
            strategies.append(
                GeneratedStrategy(
                    type="CHANGE_DUE_DATE",
                    description="Alterar vencimento do cartao",
                )
            )

            strategies.append(
                GeneratedStrategy(
                    type="USE_CASH_RESERVE",
                    description="Utilizar parte da reserva",
                )
            )

        if diagnosis.has_negative_balance:
            transaction = None

            if financial_plan is not None:
                for day in financial_plan.timeline:
                    for candidate in day:
                        if (
                            candidate.type == TransactionType.EXPENSE
                            and candidate.nature == ExpenseNature.NON_ESSENTIAL
                        ):
                            transaction = candidate
                            break

                    if transaction:
                        break

            strategies.append(
                GeneratedStrategy(
                    type="POSTPONE_EXPENSE",
                    description="Adiar despesa nao essencial",
                    payload=transaction,
                )
            )

        return strategies
