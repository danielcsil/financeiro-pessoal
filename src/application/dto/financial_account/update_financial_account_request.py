from __future__ import annotations

"""
Update Financial Account Request DTO.

===============================================================================
Purpose
===============================================================================

Represents the input required to update an existing financial account.

This Data Transfer Object carries the data provided by the Presentation Layer
to the UpdateFinancialAccountUseCase.

DTOs define the contract between the Presentation Layer and the Application
Layer without exposing HTTP-specific or persistence-specific concepts.

===============================================================================
Architecture
===============================================================================

Presentation Layer

        │

        ▼

UpdateFinancialAccountRequest

        │

        ▼

UpdateFinancialAccountUseCase

===============================================================================
Design Principles
===============================================================================

• Immutable.

• Independent from FastAPI.

• Independent from SQLAlchemy.

• Contains only business data required by the use case.
"""

from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from src.domain.enums.account_type import AccountType


@dataclass(
    frozen=True,
    slots=True,
)
class UpdateFinancialAccountRequest:
    """
    Input required to update a financial account.
    """

    user_id: UUID

    account_id: UUID

    name: str

    institution: str | None

    account_type: AccountType

    color: str

    icon: str

    include_in_cash_flow: bool

    include_in_net_worth: bool

    current_balance: Decimal