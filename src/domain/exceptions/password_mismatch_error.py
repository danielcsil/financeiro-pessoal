from __future__ import annotations

from src.domain.exceptions import DomainException


class PasswordMismatchError(DomainException):
    """
    Raised when password confirmation does not match.
    """