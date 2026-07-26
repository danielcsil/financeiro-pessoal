from __future__ import annotations

from src.domain.exceptions.domain_exception import DomainException


class InvalidEmailError(DomainException):
    """
    Raised when an e-mail is invalid.
    """