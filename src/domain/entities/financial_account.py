from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC
from datetime import datetime
from decimal import Decimal
from uuid import UUID, uuid4

from src.domain.enums.account_type import AccountType


@dataclass(slots=True)
class FinancialAccount:
    """
    Represents a financial account owned by a user.

    A financial account is the origin or destination of
    financial transactions within the system.

    Examples:
    - Checking account
    - Savings account
    - Cash
    - Digital wallet
    - Investment account
    """

    user_id: UUID

    name: str

    account_type: AccountType

    initial_balance: Decimal

    current_balance: Decimal

    institution: str | None = None

    color: str = "#2563EB"

    icon: str = "wallet"

    include_in_cash_flow: bool = True

    include_in_net_worth: bool = True

    active: bool = True

    id: UUID = field(default_factory=uuid4)

    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def rename(
        self,
        name: str,
    ) -> None:
        """
        Updates the account name.
        """

        self.name = name.strip()

        self.touch()

    def change_institution(
        self,
        institution: str | None,
    ) -> None:
        """
        Updates the financial institution.
        """

        if institution is None:
            self.institution = None
        else:
            self.institution = institution.strip()

        self.touch()

    def change_color(
        self,
        color: str,
    ) -> None:
        """
        Updates the account color.
        """

        self.color = color

        self.touch()

    def change_icon(
        self,
        icon: str,
    ) -> None:
        """
        Updates the account icon.
        """

        self.icon = icon

        self.touch()

    def change_type(
        self,
        account_type: AccountType,
    ) -> None:
        """
        Updates the account type.
        """

        self.account_type = account_type

        self.touch()

    def update_initial_balance(
        self,
        balance: Decimal,
    ) -> None:
        """
        Updates the initial balance.

        This operation should only be allowed before
        financial transactions are registered.
        """

        self.initial_balance = balance

        self.touch()

    def update_current_balance(
        self,
        balance: Decimal,
    ) -> None:
        """
        Updates the current balance.
        """

        self.current_balance = balance

        self.touch()

    def include_in_cashflow(
        self,
    ) -> None:
        """
        Includes this account in cash flow calculations.
        """

        self.include_in_cash_flow = True

        self.touch()

    def exclude_from_cashflow(
        self,
    ) -> None:
        """
        Excludes this account from cash flow calculations.
        """

        self.include_in_cash_flow = False

        self.touch()

    def include_in_networth(
        self,
    ) -> None:
        """
        Includes this account in net worth calculations.
        """

        self.include_in_net_worth = True

        self.touch()

    def exclude_from_networth(
        self,
    ) -> None:
        """
        Excludes this account from net worth calculations.
        """

        self.include_in_net_worth = False

        self.touch()

    def activate(
        self,
    ) -> None:
        """
        Activates the account.
        """

        self.active = True

        self.touch()

    def deactivate(
        self,
    ) -> None:
        """
        Deactivates the account.

        Accounts are never physically deleted.
        """

        self.active = False

        self.touch()

    def touch(
        self,
    ) -> None:
        """
        Updates the last modification timestamp.
        """

        self.updated_at = datetime.now(UTC)
