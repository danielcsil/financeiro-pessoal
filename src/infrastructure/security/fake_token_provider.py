from __future__ import annotations

from src.domain.services.token_provider import TokenProvider
from src.domain.value_objects.token_claims import TokenClaims


class FakeTokenProvider(TokenProvider):
    """
    Fake implementation used for tests.
    """

    def generate_access_token(
        self,
        claims: TokenClaims,
    ) -> str:
        return f"token-{claims.user_id}"
