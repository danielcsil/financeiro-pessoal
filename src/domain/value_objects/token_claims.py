from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class TokenClaims:
    """
    Claims used to generate authentication tokens.
    """

    user_id: UUID
    name: str
    email: str