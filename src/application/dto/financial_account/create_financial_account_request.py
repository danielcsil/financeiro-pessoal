from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from src.domain.enums.account_type import AccountType


@dataclass(frozen=True, slots=True)
class CreateFinancialAccountRequest:
    """
    Represents the input data required to create a new financial account.

    ----------------------------------------------------------------------------
    Purpose
    ----------------------------------------------------------------------------

    This DTO (Data Transfer Object) defines the contract between the presentation
    layer (API, CLI, Web, etc.) and the application layer.

    The use case receives this object instead of depending on HTTP requests,
    JSON payloads or persistence models, ensuring that the application layer
    remains completely independent of infrastructure concerns.

    ----------------------------------------------------------------------------
    Why use a DTO instead of passing the Entity?
    ----------------------------------------------------------------------------

    A FinancialAccount entity represents a valid business object and should only
    be instantiated after all business validations have been successfully
    executed.

    During the creation process, however, the incoming data still represents
    untrusted input provided by an external actor (user, API client, etc.).

    The responsibility of the use case is to:

    - validate business rules;
    - verify duplicated accounts;
    - instantiate the domain entity;
    - persist the entity.

    Therefore, the request object exists exclusively to transport input data
    into the application layer.

    ----------------------------------------------------------------------------
    Validation
    ----------------------------------------------------------------------------

    This class intentionally contains no validation logic.

    Validation responsibilities are divided as follows:

    - Syntax validation
        Performed by the presentation layer (FastAPI/Pydantic).

    - Business validation
        Performed by the application use case.

    - Domain invariants
        Enforced by the FinancialAccount entity and Value Objects.

    Keeping responsibilities separated prevents business rules from leaking
    into the API layer and preserves a clean architecture.
    """

    name: str

    account_type: AccountType

    initial_balance: Decimal

    institution: str | None = None

    color: str = "#2563EB"

    icon: str = "wallet"

    include_in_cash_flow: bool = True

    include_in_net_worth: bool = True