from __future__ import annotations

"""
Get Financial Account Response Schema.

===============================================================================
Purpose
===============================================================================

Defines the HTTP response returned when retrieving a single financial account.

Unlike the Application DTO, this schema belongs exclusively to the Presentation
Layer and represents the public REST API contract.

FastAPI uses this schema to:

    • validate responses;

    • serialize objects into JSON;

    • generate the OpenAPI specification;

    • document the endpoint in Swagger UI.

===============================================================================
Architecture
===============================================================================

Application DTO

        │

        ▼

API Response Schema

        │

        ▼

JSON Response

===============================================================================
Design Principles
===============================================================================

• Immutable.

• Serialization-friendly.

• HTTP-specific.

• Independent from the Domain Layer.

• Independent from the persistence layer.
"""

from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from src.domain.enums.account_type import AccountType


class GetFinancialAccountResponse(BaseModel):
    """
    HTTP response returned after successfully retrieving a financial account.
    """

    model_config = ConfigDict(
        frozen=True,
    )

    id: UUID = Field(
        description="Unique identifier of the financial account.",
    )

    user_id: UUID = Field(
        description="Owner of the financial account.",
    )

    name: str = Field(
        description="Financial account name.",
    )

    institution: str | None = Field(
        description="Financial institution.",
    )

    account_type: AccountType = Field(
        description="Type of financial account.",
    )

    initial_balance: Decimal = Field(
        description="Initial balance informed when the account was created.",
    )

    current_balance: Decimal = Field(
        description="Current account balance.",
    )

    color: str = Field(
        description="Color associated with the account.",
    )

    icon: str = Field(
        description="Icon displayed by the user interface.",
    )

    include_in_cash_flow: bool = Field(
        description="Indicates whether this account participates in cash flow calculations.",
    )

    include_in_net_worth: bool = Field(
        description="Indicates whether this account contributes to net worth calculations.",
    )

    active: bool = Field(
        description="Indicates whether the account is active.",
    )

    created_at: datetime = Field(
        description="Date and time when the account was created.",
    )