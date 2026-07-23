
from __future__ import annotations


class MinimalInterventionEngine:
    """
    Coordena a avaliação de múltiplas intervenções
    para encontrar a menor mudança capaz de eliminar
    um ciclo de dependência financeira.

    Nesta primeira versão define o contrato.
    Futuramente executará projeções, comparará
    cenários e classificará as alternativas.
    """

    def evaluate(self, interventions):

        if not interventions:
            return None

        return interventions[0]
