from src.domain.services.token_provider import TokenProvider


def test_should_define_token_provider_interface() -> None:
    assert hasattr(TokenProvider, "generate_access_token")