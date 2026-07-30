"""
Classe base para todos os identificadores do domínio.

Cada Aggregate Root possui um identificador fortemente tipado,
evitando que IDs de diferentes entidades sejam utilizados de forma
incorreta.

Exemplos:

    UserId
    AccountId
    CreditCardId
    FinancialEventId

Internamente todos são UUIDs, porém o domínio trabalha com tipos
específicos para aumentar a segurança e a expressividade.
"""

from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True, slots=True)
class EntityId:
    """
    Classe base para identificadores do domínio.
    """

    value: UUID

    @classmethod
    def new(cls) -> "EntityId":
        """
        Cria um novo identificador.

        Returns
        -------
        EntityId
            Nova instância contendo um UUID gerado automaticamente.
        """
        return cls(uuid4())

    @classmethod
    def from_string(cls, value: str) -> "EntityId":
        """
        Constrói um identificador a partir de uma string UUID.

        Parameters
        ----------
        value:
            UUID em formato textual.

        Returns
        -------
        EntityId
        """
        return cls(UUID(value))

    def __str__(self) -> str:
        return str(self.value)