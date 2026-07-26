from __future__ import annotations

from src.domain.exceptions import DomainException


class TermsNotAcceptedError(DomainException):
    """
    Raised when terms of use are not accepted.
    """