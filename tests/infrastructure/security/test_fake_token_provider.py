from uuid import uuid4

from src.domain.value_objects.token_claims import TokenClaims
from src.infrastructure.security.fake_token_provider import (
    FakeTokenProvider,
)


def test_should_generate_access_token() -> None:
    provider = FakeTokenProvider()

    claims = TokenClaims(
        user_id=uuid4(),
        name="Daniel",
        email="daniel@email.com",
    )

    token = provider.generate_access_token(claims)

    assert token == f"token-{claims.user_id}"
