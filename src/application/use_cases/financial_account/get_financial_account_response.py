from __future__ import annotations

"""
Get Financial Account Response DTO.

===============================================================================
Purpose
===============================================================================

Represents the data returned by the GetFinancialAccountUseCase.

This Data Transfer Object transports information from the Application Layer to
the Presentation Layer without exposing Domain Entities.

DTOs define the output contract of the Application Layer and are independent
from both HTTP and database technologies.

===============================================================================
Architecture
===============================================================================

Application Layer

        │

        ▼

GetFinancialAccountUseCase

        │

        ▼

GetFinancialAccountResponse

        │

        ▼

Presentation Layer

===============================================================================
Design Principles
===============================================================================

• Immutable.

• Serialization-friendly.

• Independent from HTTP.

• Independent from persistence.

• Contains only data required by the use case.
"""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from src.domain.enums.account_type import AccountType


@dataclass(frozen=True, slots=True)
class GetFinancialAccountResponse:
    """
    Output returned after successfully retrieving a financial account.
    """

    id: UUID

    user_id: UUID

    name: str

    institution: str | None

    account_type: AccountType

    initial_balance: Decimal

    current_balance: Decimal

    color: str

    icon: str

    include_in_cash_flow: bool

    include_in_net_worth: bool

    active: bool

    created_at: datetime