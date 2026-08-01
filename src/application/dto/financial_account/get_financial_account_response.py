from __future__ import annotations

"""
Get Financial Account Response DTO.

===============================================================================
Purpose
===============================================================================

Represents the data returned by the GetFinancialAccountUseCase.

This Data Transfer Object transports information from the Application Layer to
the Presentation Layer without exposing Domain Entities.

DTOs define the output contract of the Application Layer and remain completely
independent from HTTP, persistence technologies and user interfaces.

===============================================================================
Architecture
===============================================================================

Presentation Layer

        ▲

        │

GetFinancialAccountResponse

        ▲

        │

GetFinancialAccountUseCase

===============================================================================
Design Principles
===============================================================================

• Immutable.

• Serialization-friendly.

• Independent from FastAPI.

• Independent from SQLAlchemy.

• Independent from Domain Entities.

• Contains only the information required by the Presentation Layer.
"""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from src.domain.enums.account_type import AccountType


@dataclass(
    frozen=True,
    slots=True,
)
class GetFinancialAccountResponse:
    """
    Output returned after successfully retrieving a financial account.

    Every field represents the current state of the requested financial account.
    The DTO contains only data and no business behavior.
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