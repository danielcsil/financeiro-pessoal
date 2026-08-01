from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from src.domain.enums.account_type import AccountType


class FinancialAccountResponse(BaseModel):
    """
    Represents a single financial account returned by the API.

    =============================================================================
    Purpose
    =============================================================================

    This schema defines the public representation of a financial account exposed
    by the REST API.

    Unlike Domain Entities, this object exists exclusively for serialization and
    OpenAPI documentation.

    It intentionally exposes only the information required by API consumers.

    =============================================================================
    Architectural Notes
    =============================================================================

    Domain Entity
            │
            ▼
    Application DTO
            │
            ▼
    API Schema
            │
            ▼
        JSON Response

    Keeping these layers separated allows the internal domain model to evolve
    without breaking external API contracts.
    """

    model_config = ConfigDict(
        frozen=True,
    )

    id: UUID = Field(
        description="Unique identifier of the financial account.",
    )

    name: str = Field(
        description="Display name of the account.",
    )

    institution: str | None = Field(
        description="Financial institution.",
    )

    account_type: AccountType = Field(
        description="Type of financial account.",
    )

    balance: Decimal = Field(
        description="Current account balance.",
    )

    color: str = Field(
        description="Color associated with the account.",
    )

    icon: str = Field(
        description="Icon identifier used by the frontend.",
    )

    include_in_cash_flow: bool = Field(
        description="Whether the account participates in cash flow calculations.",
    )

    include_in_net_worth: bool = Field(
        description="Whether the account contributes to net worth calculations.",
    )

    active: bool = Field(
        description="Indicates whether the account is active.",
    )

    created_at: datetime = Field(
        description="Account creation timestamp.",
    )


class ListFinancialAccountsResponse(BaseModel):
    """
    Response returned by GET /financial-accounts.

    =============================================================================
    Purpose
    =============================================================================

    Encapsulates the complete result of the account listing operation.

    Returning an object instead of a raw array provides room for future
    enhancements while preserving API compatibility.

    Future versions may include:

        • pagination;

        • sorting information;

        • filters applied;

        • aggregate balances;

        • statistics.

    Example
    -------

    {
        "items": [...],
        "total": 5
    }
    """

    model_config = ConfigDict(
        frozen=True,
    )

    items: list[FinancialAccountResponse] = Field(
        description="Collection of financial accounts.",
    )

    total: int = Field(
        description="Total number of returned accounts.",
    )