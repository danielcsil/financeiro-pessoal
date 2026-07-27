from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.value_objects.token_claims import TokenClaims


class TokenProvider(ABC):
    """
    Generates authentication tokens.
    """

    @abstractmethod
    def generate_access_token(
        claims: TokenClaims,
    ) -> str:
        """
        Generates an access token.
        """
