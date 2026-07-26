from src.domain.services.password_verifier import PasswordVerifier


def test_should_define_password_verifier_interface() -> None:
    assert hasattr(PasswordVerifier, "verify")