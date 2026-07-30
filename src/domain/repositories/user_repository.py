from __future__ import annotations

"""
Contrato do repositório de usuários.

O repositório representa a coleção de agregados User do domínio,
abstraindo completamente a tecnologia de persistência utilizada.

A responsabilidade de confirmar ou desfazer alterações pertence à
Unit of Work. Por esse motivo, este contrato não expõe operações
explícitas de atualização (update) ou persistência (commit).
"""

from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities.user import User
from src.domain.value_objects.email import Email


class UserRepository(ABC):
    """
    Contrato para persistência e consulta de usuários.
    """

    @abstractmethod
    def add(
        self,
        user: User,
    ) -> None:
        """
        Adiciona um novo usuário ao repositório.

        A persistência definitiva será realizada pela Unit of Work.
        """
        raise NotImplementedError

    @abstractmethod
    def remove(
        self,
        user: User,
    ) -> None:
        """
        Remove um usuário do repositório.

        A remoção definitiva será realizada pela Unit of Work.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_id(
        self,
        user_id: UUID,
    ) -> User | None:
        """
        Recupera um usuário pelo identificador.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_email(
        self,
        email: Email,
    ) -> User | None:
        """
        Recupera um usuário pelo endereço de e-mail.
        """
        raise NotImplementedError

    @abstractmethod
    def exists_by_id(
        self,
        user_id: UUID,
    ) -> bool:
        """
        Verifica se existe um usuário com o identificador informado.
        """
        raise NotImplementedError

    @abstractmethod
    def exists_by_email(
        self,
        email: Email,
    ) -> bool:
        """
        Verifica se existe um usuário com o e-mail informado.
        """
        raise NotImplementedError