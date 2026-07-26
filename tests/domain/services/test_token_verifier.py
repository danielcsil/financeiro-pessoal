from src.domain.services.token_verifier import TokenVerifier


def test_should_define_token_verifier_interface() -> None:
    assert hasattr(TokenVerifier, "verify_access_token")