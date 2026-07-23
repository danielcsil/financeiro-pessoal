from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4

from src.domain.enums import AccountStatus, AccountType
from src.domain.value_objects import Money


@dataclass(slots=True)
class Account:

    id: UUID = field(default_factory=uuid4)

    _name: str = field(init=False, repr=False)

    _type: AccountType = field(init=False, repr=False)

    _status: AccountStatus = field(
        default=AccountStatus.ACTIVE,
        init=False,
        repr=False,
    )

    _balance: Money = field(
        default_factory=Money.zero,
        init=False,
        repr=False,
    )

    def __init__(
        self,
        name: str,
        type: AccountType = AccountType.CHECKING,
        id: UUID | None = None,
    ):
        self.id = id or uuid4()

        self._status = AccountStatus.ACTIVE
        self._balance = Money.zero()

        self.rename(name)
        self._type = type

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

    def rename(self, new_name: str) -> None:
        new_name = new_name.strip()

        if not new_name:
            raise ValueError("Account name cannot be empty.")

        self._name = new_name

    def activate(self) -> None:
        self._status = AccountStatus.ACTIVE

    def deactivate(self) -> None:
        self._status = AccountStatus.INACTIVE

    def close(self) -> None:
        self._status = AccountStatus.CLOSED

    def __str__(self) -> str:
        return self._name
