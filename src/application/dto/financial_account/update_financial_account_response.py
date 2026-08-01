from __future__ import annotations

"""
Update Financial Account Response DTO.

===============================================================================
Purpose
===============================================================================

Represents the result returned after successfully updating a financial account.

This Data Transfer Object defines the output contract of the
UpdateFinancialAccountUseCase and transports the updated account information
from the Application Layer to the Presentation Layer.

The DTO is intentionally independent from HTTP, persistence technologies and
Domain Entities.

===============================================================================
Architecture
===============================================================================

Presentation Layer

        ▲

        │

UpdateFinancialAccountResponse

        ▲

        │

UpdateFinancialAccountUseCase

===============================================================================
Design Principles
===============================================================================

• Immutable.

• Serialization-friendly.

• Independent from FastAPI.

• Independent from SQLAlchemy.

• Independent from Domain Entities.

• Contains only data required by the Presentation Layer.
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
class UpdateFinancialAccountResponse:
    """
    Output returned after successfully updating a financial account.

    The object represents the latest persisted state of the financial account.
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

    updated_at: datetime