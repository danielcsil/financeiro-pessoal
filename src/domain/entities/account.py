from __future__ import annotations

from datetime import UTC, datetime

from src.domain.enums import AccountStatus, AccountType
from src.domain.value_objects import Money
from src.domain.value_objects.identifiers.user_id import UserId
from src.domain.value_objects.identifiers.account_id import AccountId
from uuid import UUID


class Account:
    """
    Aggregate root that represents a financial account.
    """

    def __init__(
        self,
        name: str,
        type: AccountType = AccountType.CHECKING,
        user_id: UserId | None = None,
        id: AccountId | None = None,
        description: str | None = None,
        institution: str | None = None,
        status: AccountStatus = AccountStatus.ACTIVE,
        balance: Money | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ) -> None:
        self._id = id or AccountId.new()
        self._user_id = user_id
        self._type = type
        self._status = status
        self._balance = balance or Money.zero()
        self._description = description
        self._institution = institution
        self._created_at = created_at or datetime.now(UTC)
        self._updated_at = updated_at or datetime.now(UTC)
        self.rename(name)

    @property
    def id(self) -> UUID:
        return self._id.value

    @property
    def account_id(self) -> AccountId:
        return self._id

    @property
    def user_id(self) -> UserId | None:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> AccountType:
        return self._type

    @property
    def status(self) -> AccountStatus:
        return self._status

    @property
    def balance(self) -> Money:
        return self._balance

    @property
    def description(self) -> str | None:
        return self._description

    @property
    def institution(self) -> str | None:
        return self._institution

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def rename(self, name: str) -> None:
        name = name.strip()

        if not name:
            raise ValueError("Account name cannot be empty.")

        self._name = name
        self.touch()

    def change_description(self, description: str | None) -> None:
        self._description = description
        self.touch()

    def change_institution(self, institution: str | None) -> None:
        self._institution = institution
        self.touch()

    def activate(self) -> None:
        self._status = AccountStatus.ACTIVE
        self.touch()

    def deactivate(self) -> None:
        self._status = AccountStatus.INACTIVE
        self.touch()

    def close(self) -> None:
        self._status = AccountStatus.CLOSED
        self.touch()

    def touch(self) -> None:
        self._updated_at = datetime.now(UTC)
