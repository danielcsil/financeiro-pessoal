from __future__ import annotations

from abc import ABC, abstractmethod

from src.domain.value_objects.token_claims import TokenClaims

class TokenVerifier(ABC):
    """
    Verifies and decodes authentication tokens.
    """

    @abstractmethod
    def verify_access_token(
        self,
        token: str,
    ) -> TokenClaims:
        """
        Validates the token and returns its claims.
        """