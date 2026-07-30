from __future__ import annotations

"""
Aggregate Root que representa uma conta financeira.

Uma conta representa um local onde recursos financeiros são
armazenados ou movimentados, como conta corrente, poupança,
carteira ou conta de investimento.

A entidade é responsável apenas pelo seu próprio estado e pelas
regras relacionadas ao seu ciclo de vida.
"""

from dataclasses import dataclass, field
from datetime import UTC, datetime

from src.domain.value_objects.identifiers.account_id import AccountId
from src.domain.value_objects.identifiers.user_id import UserId


@dataclass(slots=True)
class Account:
    """
    Aggregate Root que representa uma conta financeira.
    """

    user_id: UserId
    name: str

    id: AccountId = field(default_factory=AccountId.new)

    description: str | None = None

    institution: str | None = None

    is_active: bool = True

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    @classmethod
    def create(
        cls,
        user_id: UserId,
        name: str,
        institution: str | None = None,
        description: str | None = None,
    ) -> "Account":
        """
        Cria uma nova conta.
        """

        name = name.strip()

        if not name:
            raise ValueError("Account name cannot be empty.")

        return cls(
            user_id=user_id,
            name=name,
            institution=institution,
            description=description,
        )

    def rename(
        self,
        name: str,
    ) -> None:
        """
        Altera o nome da conta.
        """

        name = name.strip()

        if not name:
            raise ValueError("Account name cannot be empty.")

        self.name = name
        self.touch()

    def change_description(
        self,
        description: str | None,
    ) -> None:
        """
        Atualiza a descrição da conta.
        """

        self.description = description
        self.touch()

    def change_institution(
        self,
        institution: str | None,
    ) -> None:
        """
        Atualiza a instituição financeira.
        """

        self.institution = institution
        self.touch()

    def activate(self) -> None:
        """
        Ativa a conta.
        """

        if not self.is_active:
            self.is_active = True
            self.touch()

    def deactivate(self) -> None:
        """
        Desativa a conta.
        """

        if self.is_active:
            self.is_active = False
            self.touch()

    def touch(self) -> None:
        """
        Atualiza o instante da última modificação.
        """

        self.updated_at = datetime.now(UTC)