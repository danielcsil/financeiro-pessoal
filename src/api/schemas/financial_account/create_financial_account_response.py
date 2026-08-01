from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from src.domain.enums.account_type import AccountType


class CreateFinancialAccountResponse(BaseModel):
    """
    HTTP response returned after successfully creating a financial account.

    ============================================================================
    Purpose
    ============================================================================

    This schema defines the JSON returned by the REST API after a successful
    account creation.

    Unlike the Domain Entity or the Application DTO, this object belongs
    exclusively to the Presentation Layer.

    ============================================================================
    Architectural Responsibility
    ============================================================================

        Use Case

             ↓

    Application DTO

             ↓

    API Schema

             ↓

    JSON Response

    The schema is responsible only for exposing the public API contract.

    ============================================================================
    Why not return the Domain Entity?
    ============================================================================

    Domain entities represent business concepts.

    API schemas represent HTTP contracts.

    Keeping both separated provides several advantages:

        • prevents exposing internal business details;

        • allows the API contract to evolve independently;

        • simplifies serialization;

        • keeps architectural boundaries clear.

    ============================================================================
    Swagger Documentation
    ============================================================================

    FastAPI automatically uses this schema to generate the OpenAPI
    specification, making the endpoint self-documented.
    """

    model_config = ConfigDict(
        frozen=True,
    )

    id: UUID = Field(
        description="Unique identifier of the created account.",
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
        description="Financial account type.",
    )

    initial_balance: float = Field(
        description="Initial account balance.",
    )

    current_balance: float = Field(
        description="Current account balance.",
    )

    color: str = Field(
        description="Color associated with the account.",
    )

    icon: str = Field(
        description="Icon displayed by the frontend.",
    )

    include_in_cash_flow: bool = Field(
        description="Indicates whether the account participates in cash flow calculations.",
    )

    include_in_net_worth: bool = Field(
        description="Indicates whether the account contributes to net worth.",
    )

    active: bool = Field(
        description="Indicates whether the account is active.",
    )

    created_at: datetime = Field(
        description="Creation timestamp.",
    )