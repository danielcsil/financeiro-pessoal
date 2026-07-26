from __future__ import annotations

from datetime import UTC, datetime, timedelta

import jwt

from src.domain.value_objects.token_claims import TokenClaims
from src.domain.services.token_provider import TokenProvider


class JwtTokenProvider(TokenProvider):
    """
    Generates JWT access tokens.
    """

    def __init__(
        self,
        secret_key: str,
        algorithm: str = "HS256",
        expiration_minutes: int = 30,
    ) -> None:
        self._secret_key = secret_key
        self._algorithm = algorithm
        self._expiration_minutes = expiration_minutes

    def generate_access_token(
        self,
        claims: TokenClaims,
    ) -> str:
        now = datetime.now(UTC)

        payload = {
            "sub": str(claims.user_id),
            "name": claims.name,
            "email": claims.email,
            "iat": now,
            "exp": now + timedelta(minutes=self._expiration_minutes),
        }

        return jwt.encode(
            payload,
            self._secret_key,
            algorithm=self._algorithm,
        )