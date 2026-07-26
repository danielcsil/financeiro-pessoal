from uuid import uuid4

import jwt

from src.domain.value_objects.token_claims import TokenClaims
from src.infrastructure.security.jwt_token_provider import JwtTokenProvider


def test_should_generate_jwt_access_token() -> None:
    provider = JwtTokenProvider(
        secret_key="my-secret-key",
    )

    claims = TokenClaims(
        user_id=uuid4(),
        name="Daniel",
        email="daniel@email.com",
    )

    token = provider.generate_access_token(claims)

    payload = jwt.decode(
        token,
        "my-secret-key",
        algorithms=["HS256"],
    )

    assert payload["sub"] == str(claims.user_id)
    assert payload["name"] == claims.name
    assert payload["email"] == claims.email