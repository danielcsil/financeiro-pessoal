
"""
Exemplo de utilização da API pública do domínio financeiro.

Este exemplo demonstra o fluxo completo de planejamento
financeiro utilizando apenas a classe FinancialPlanner.
"""

from src.domain.services import FinancialPlanner


def main():

    planner = FinancialPlanner()

    # TODO:
    # Substituir pelo construtor real do plano financeiro
    financial_plan = ...

    result = planner.analyze(financial_plan)

    print("===== PLANEJAMENTO FINANCEIRO =====")

    print()

    print("Score:", result.score.overall)

    print("Liquidez:", result.liquidity)

    print()

    print(result.report.summary)

    print()

    if result.report.highlights:

        print("Indicadores")

        for item in result.report.highlights:

            print("-", item)


if __name__ == "__main__":

    main()
