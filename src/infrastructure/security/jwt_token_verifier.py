from __future__ import annotations

import jwt

from src.domain.exceptions import InvalidCredentialsError
from src.domain.services.token_verifier import TokenVerifier
from src.domain.value_objects.token_claims import TokenClaims
from uuid import UUID


class JwtTokenVerifier(TokenVerifier):
    """
    Verifies JWT access tokens.
    """

    def __init__(
        self,
        secret_key: str,
        algorithm: str = "HS256",
    ) -> None:
        self._secret_key = secret_key
        self._algorithm = algorithm

    def verify_access_token(
        self,
        token: str,
    ) -> TokenClaims:
        try:
            payload = jwt.decode(
                token,
                self._secret_key,
                algorithms=[self._algorithm],
            )

            return TokenClaims(
                user_id=UUID(payload["sub"]),
                name=payload["name"],
                email=payload["email"],
            )

        except jwt.PyJWTError as exc:
            raise InvalidCredentialsError() from exc