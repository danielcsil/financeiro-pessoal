from __future__ import annotations

from uuid import UUID

from src.domain.services.token_provider import TokenProvider
from domain.value_objects.token_claims import TokenClaims


class FakeTokenProvider(TokenProvider):
    """
    Fake implementation used for tests.
    """

    def generate_access_token(
    self,
    claims: TokenClaims,
    ) -> str:
        return f"token-{claims.user_id}"