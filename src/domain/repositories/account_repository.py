from __future__ import annotations

"""
Contrato do repositório de contas financeiras.

O repositório representa a coleção de agregados Account do domínio,
abstraindo completamente a tecnologia de persistência utilizada.

A responsabilidade de confirmar ou desfazer alterações pertence à
Unit of Work. Por esse motivo, este contrato não expõe operações
explícitas de atualização (update) ou persistência (commit).
"""

from abc import ABC, abstractmethod

from src.domain.entities.account import Account
from src.domain.value_objects.identifiers.account_id import AccountId
from src.domain.value_objects.identifiers.user_id import UserId


class AccountRepository(ABC):
    """
    Contrato para persistência e consulta de contas financeiras.
    """

    @abstractmethod
    def add(self, account: Account) -> None:
        """
        Adiciona uma nova conta ao repositório.
        """
        raise NotImplementedError

    @abstractmethod
    def remove(self, account: Account) -> None:
        """
        Remove uma conta do repositório.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_id(
        self,
        account_id: AccountId,
    ) -> Account | None:
        """
        Recupera uma conta pelo seu identificador.
        """
        raise NotImplementedError

    @abstractmethod
    def list_by_user(
        self,
        user_id: UserId,
    ) -> list[Account]:
        """
        Retorna todas as contas pertencentes ao usuário.
        """
        raise NotImplementedError

    @abstractmethod
    def exists_by_id(
        self,
        account_id: AccountId,
    ) -> bool:
        """
        Verifica se uma conta existe.
        """
        raise NotImplementedError

    @abstractmethod
    def exists_by_name(
        self,
        user_id: UserId,
        name: str,
    ) -> bool:
        """
        Verifica se o usuário já possui uma conta com o nome informado.
        """
        raise NotImplementedError