from __future__ import annotations

"""
Update Financial Account Request Schema.

===============================================================================
Purpose
===============================================================================

Defines the HTTP request body used to update an existing financial account.

This schema belongs exclusively to the Presentation Layer and represents the
public REST API contract consumed by client applications.

FastAPI uses this schema to:

    • validate incoming HTTP requests;

    • deserialize JSON payloads;

    • generate the OpenAPI specification;

    • document the endpoint in Swagger UI.

===============================================================================
Architecture
===============================================================================

JSON Request

        │

        ▼

UpdateFinancialAccountRequest

        │

        ▼

Application DTO

===============================================================================
Design Principles
===============================================================================

• HTTP-specific.

• Independent from the Application Layer.

• Independent from Domain Entities.

• Declarative validation using Pydantic.
"""

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from src.domain.enums.account_type import AccountType


class UpdateFinancialAccountRequest(BaseModel):
    """
    HTTP request used to update a financial account.
    """

    model_config = ConfigDict(
        frozen=True,
        str_strip_whitespace=True,
    )

    name: str = Field(
        min_length=1,
        max_length=100,
        description="Financial account name.",
        examples=["Checking Account"],
    )

    institution: str | None = Field(
        default=None,
        max_length=100,
        description="Financial institution.",
        examples=["Nubank"],
    )

    account_type: AccountType = Field(
        description="Type of financial account.",
    )

    color: str = Field(
        min_length=4,
        max_length=20,
        description="Color associated with the account.",
        examples=["#3B82F6"],
    )

    icon: str = Field(
        min_length=1,
        max_length=50,
        description="Icon identifier used by the frontend.",
        examples=["wallet"],
    )

    include_in_cash_flow: bool = Field(
        description=(
            "Indicates whether this account participates in cash flow "
            "calculations."
        ),
    )

    include_in_net_worth: bool = Field(
        description=(
            "Indicates whether this account contributes to net worth "
            "calculations."
        ),
    )