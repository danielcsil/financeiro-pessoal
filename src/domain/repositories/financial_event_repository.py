"""
Contrato do repositório de eventos financeiros.

O FinancialEvent é o principal Aggregate Root do domínio financeiro.
Este contrato define as operações necessárias para persistência e
consulta dos eventos, sem acoplamento à tecnologia utilizada.

A implementação concreta pertence à camada de infraestrutura.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date

from src.domain.entities.financial_event import FinancialEvent
from src.domain.value_objects.identifiers.account_id import AccountId
from src.domain.value_objects.identifiers.financial_event_id import (
    FinancialEventId,
)
from src.domain.value_objects.identifiers.user_id import UserId


class FinancialEventRepository(ABC):
    """
    Contrato para persistência de eventos financeiros.
    """

    @abstractmethod
    def add(self, event: FinancialEvent) -> None:
        """
        Adiciona um novo evento financeiro.
        """
        raise NotImplementedError

    @abstractmethod
    def get_by_id(
        self,
        event_id: FinancialEventId,
    ) -> FinancialEvent | None:
        """
        Obtém um evento pelo seu identificador.
        """
        raise NotImplementedError

    @abstractmethod
    def remove(
        self,
        event: FinancialEvent,
    ) -> None:
        """
        Remove um evento financeiro.
        """
        raise NotImplementedError

    @abstractmethod
    def exists(
        self,
        event_id: FinancialEventId,
    ) -> bool:
        """
        Verifica se o evento existe.
        """
        raise NotImplementedError

    @abstractmethod
    def list_by_user(
        self,
        user_id: UserId,
    ) -> list[FinancialEvent]:
        """
        Lista todos os eventos pertencentes ao usuário.
        """
        raise NotImplementedError

    @abstractmethod
    def list_by_account(
        self,
        account_id: AccountId,
    ) -> list[FinancialEvent]:
        """
        Lista todos os eventos de uma conta.
        """
        raise NotImplementedError

    @abstractmethod
    def list_between_dates(
        self,
        user_id: UserId,
        start_date: date,
        end_date: date,
    ) -> list[FinancialEvent]:
        """
        Lista os eventos compreendidos entre duas datas.
        """
        raise NotImplementedError