from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from src.domain.enums.account_type import AccountType


@dataclass(frozen=True, slots=True)
class CreateFinancialAccountResponse:
    """
    Represents the result of a successful financial account creation.

    ============================================================================
    Purpose
    ============================================================================

    This DTO defines the output contract of the CreateFinancialAccountUseCase.

    Instead of exposing the domain entity directly, the application layer
    returns a response object containing only the information required by the
    presentation layer.

    This approach prevents external layers from depending on the internal
    structure of domain entities and allows the domain model to evolve without
    impacting APIs, user interfaces or integrations.

    ============================================================================
    Why not return the Entity?
    ============================================================================

    Domain entities encapsulate business behavior and invariants.

    They should never be exposed outside the application boundary because:

    • presentation layers should not manipulate domain objects;

    • infrastructure details must remain isolated;

    • future implementations may expose different views of the same entity
      depending on permissions or business scenarios.

    Returning DTOs keeps the application layer independent and explicit about
    what information leaves the use case.

    ============================================================================
    Immutability
    ============================================================================

    Response DTOs are immutable.

    After a use case finishes its execution, the produced result represents a
    historical snapshot of that operation and must not be modified by callers.
    """

    id: UUID

    user_id: UUID

    name: str

    account_type: AccountType

    institution: str | None

    initial_balance: Decimal

    current_balance: Decimal

    color: str

    icon: str

    include_in_cash_flow: bool

    include_in_net_worth: bool

    active: bool

    created_at: datetime

    updated_at: datetime