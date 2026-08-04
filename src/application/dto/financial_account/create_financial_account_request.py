from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from src.domain.enums.account_type import AccountType


@dataclass(frozen=True, slots=True)
class CreateFinancialAccountRequest:
    """
    Input DTO used to create a financial account.
    """

    user_id: UUID

    name: str

    account_type: AccountType

    initial_balance: Decimal

    institution: str | None = None

    color: str = "#2563EB"

    icon: str = "wallet"

    include_in_cash_flow: bool = True

    include_in_net_worth: bool = True