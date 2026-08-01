from __future__ import annotations

"""
Financial Account Not Found Error.

===============================================================================
Purpose
===============================================================================

Raised when a requested financial account cannot be found.

This exception is intentionally also used when the requested account belongs
to another user. Returning the same error in both situations prevents leaking
information about the existence of resources owned by other users.

===============================================================================
When it is raised
===============================================================================

Typical scenarios include:

    • the account identifier does not exist;

    • the account has been removed;

    • the authenticated user is not the owner of the account.

===============================================================================
Architecture
===============================================================================

Presentation Layer

        │

        ▼

Application Use Case

        │

        ▼

FinancialAccountNotFoundError

        │

        ▼

FastAPI Exception Handler

        │

        ▼

HTTP 404 Not Found

===============================================================================
Security
===============================================================================

Ownership validation intentionally returns the same exception as a nonexistent
resource. This avoids exposing whether a financial account exists but belongs
to another authenticated user.
"""

from src.domain.exceptions.domain_exception import DomainException


class FinancialAccountNotFoundError(DomainException):
    """
    Raised when a financial account cannot be located.
    """

    def __init__(self) -> None:
        super().__init__(
            message="Financial account not found.",
        )