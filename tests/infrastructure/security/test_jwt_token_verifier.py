from uuid import uuid4

import pytest

from src.domain.value_objects.token_claims import TokenClaims
from src.domain.exceptions import InvalidCredentialsError
from src.infrastructure.security.jwt_token_provider import JwtTokenProvider
from src.infrastructure.security.jwt_token_verifier import JwtTokenVerifier


SECRET = "my-super-secret-key-with-32-bytes!!"


def test_should_verify_valid_token() -> None:
    provider = JwtTokenProvider(secret_key=SECRET)
    verifier = JwtTokenVerifier(secret_key=SECRET)

    claims = TokenClaims(
        user_id=uuid4(),
        name="Daniel",
        email="daniel@email.com",
    )

    token = provider.generate_access_token(claims)

    verified = verifier.verify_access_token(token)

    assert verified == claims


def test_should_raise_error_for_invalid_token() -> None:
    verifier = JwtTokenVerifier(secret_key=SECRET)

    with pytest.raises(InvalidCredentialsError):
        verifier.verify_access_token("invalid-token")