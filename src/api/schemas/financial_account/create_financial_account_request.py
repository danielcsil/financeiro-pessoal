from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from src.domain.enums.account_type import AccountType


class CreateFinancialAccountRequest(BaseModel):
    """
    HTTP request model used to create a new financial account.

    ============================================================================
    Purpose
    ============================================================================

    This schema defines the JSON contract expected by the REST API when a client
    requests the creation of a new financial account.

    It belongs exclusively to the Presentation Layer and must never be used as
    a Domain Entity or Application DTO.

    ============================================================================
    Architectural Responsibility
    ============================================================================

        HTTP Request

              ↓

        FastAPI Validation

              ↓

    CreateFinancialAccountRequest

              ↓

        Application DTO

              ↓

        Use Case

    The API schema is responsible only for validating and documenting the HTTP
    contract.

    Business rules are delegated to the Application and Domain layers.

    ============================================================================
    Validation
    ============================================================================

    Basic validation is intentionally limited to structural concerns such as:

        • required fields;

        • string length;

        • numeric ranges;

        • JSON format.

    Business validation (duplicate names, ownership, permissions, etc.) must
    always be performed inside the Use Case.
    """

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    name: str = Field(
        ...,
        min_length=3,
        max_length=120,
        description="User-defined account name.",
        examples=["Conta Corrente"],
    )

    institution: str | None = Field(
        default=None,
        max_length=120,
        description="Financial institution name.",
        examples=["Nubank"],
    )

    account_type: AccountType = Field(
        ...,
        description="Type of financial account.",
        examples=["CHECKING"],
    )

    initial_balance: float = Field(
        default=0,
        description="Opening account balance.",
        examples=[1500.75],
    )

    color: str = Field(
        default="#2563EB",
        max_length=20,
        description="Color used by the frontend.",
        examples=["#2563EB"],
    )

    icon: str = Field(
        default="wallet",
        max_length=50,
        description="Frontend icon identifier.",
        examples=["wallet"],
    )

    include_in_cash_flow: bool = Field(
        default=True,
        description="Whether the account participates in cash flow projections.",
    )

    include_in_net_worth: bool = Field(
        default=True,
        description="Whether the account contributes to net worth calculations.",
    )