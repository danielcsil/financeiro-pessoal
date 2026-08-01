from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Sequence
from uuid import UUID


@dataclass(frozen=True, slots=True)
class FinancialAccountItemResponse:
    """
    Represents a single financial account returned by the
    ListFinancialAccountsUseCase.

    ============================================================================
    Purpose
    ============================================================================

    This Data Transfer Object (DTO) exposes only the information required by
    the presentation layer.

    It intentionally hides internal domain implementation details while
    providing a stable contract for API responses.

    ============================================================================
    Why use a DTO instead of returning the Domain Entity?
    ============================================================================

    Domain entities model business behavior.

    Response DTOs model data exchanged between the application and external
    clients.

    Keeping these concepts separated provides several benefits:

        • prevents accidental modification of domain entities;

        • allows the API contract to evolve independently;

        • avoids exposing internal business implementation;

        • simplifies serialization.

    ============================================================================
    Typical Consumer
    ============================================================================

        ListFinancialAccountsUseCase

                ↓

        FinancialAccountItemResponse

                ↓

        FastAPI Response

                ↓

        Vue Frontend
    """

    id: UUID

    name: str

    institution: str | None

    account_type: str

    balance: Decimal

    color: str

    icon: str

    include_in_cash_flow: bool

    include_in_net_worth: bool

    active: bool

    created_at: datetime


@dataclass(frozen=True, slots=True)
class ListFinancialAccountsResponse:
    """
    Response object returned by ListFinancialAccountsUseCase.

    ============================================================================
    Purpose
    ============================================================================

    Encapsulates the complete result of the listing operation.

    Instead of returning a raw list, this object provides additional metadata
    that may become useful as the application evolves.

    ============================================================================
    Why wrap the collection?
    ============================================================================

    Returning an object instead of a bare list allows future expansion without
    breaking the public contract.

    Future versions may include information such as:

        • pagination;

        • sorting;

        • filters applied;

        • total balance;

        • number of active accounts;

        • grouped statistics.

    Example:

        {
            "items": [...],
            "total": 6,
            "total_balance": 12450.30,
            "active_accounts": 5
        }

    Since clients already receive an object, these fields can be added without
    introducing breaking changes.

    ============================================================================
    Immutability
    ============================================================================

    This DTO is immutable.

    After creation, neither the collection nor its metadata should be modified.
    """

    items: Sequence[FinancialAccountItemResponse]

    total: int