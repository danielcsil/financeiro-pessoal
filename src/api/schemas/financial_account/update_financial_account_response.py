from __future__ import annotations

"""
Update Financial Account Response Schema.

===============================================================================
Purpose
===============================================================================

Defines the HTTP response returned after successfully updating a financial
account.

This schema belongs exclusively to the Presentation Layer and represents the
public REST API contract exposed to client applications.

FastAPI uses this schema to:

    • serialize responses into JSON;

    • validate response payloads;

    • generate the OpenAPI specification;

    • document the endpoint in Swagger UI.

===============================================================================
Architecture
===============================================================================

Application DTO

        │

        ▼

UpdateFinancialAccountResponse

        │

        ▼

HTTP Response

===============================================================================
Design Principles
===============================================================================

• Immutable.

• HTTP-specific.

• Independent from Domain Entities.

• Independent from persistence technologies.

• Serialization-friendly.
"""

from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from src.domain.enums.account_type import AccountType


class UpdateFinancialAccountResponse(BaseModel):
    """
    HTTP response returned after successfully updating a financial account.
    """

    model_config = ConfigDict(
        frozen=True,
    )

    id: UUID = Field(
        description="Unique identifier of the financial account.",
    )

    user_id: UUID = Field(
        description="Identifier of the account owner.",
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
        description="Icon identifier used by the frontend.",
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
        description="Timestamp when the account was created.",
    )

    updated_at: datetime = Field(
        description="Timestamp of the last successful update.",
    )