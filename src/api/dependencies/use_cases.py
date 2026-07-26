from src.application.use_cases.auth.login_user import LoginUserUseCase
from src.application.use_cases.auth.register_user import RegisterUserUseCase

from .repositories import get_user_repository
from .services import (
    get_password_hasher,
    get_password_verifier,
    get_token_provider,
)

from src.application.use_cases.auth.get_current_user import (
    GetCurrentUserUseCase,
)
from src.application.use_cases.auth.login_user import LoginUserUseCase
from src.application.use_cases.auth.register_user import RegisterUserUseCase


def get_register_user_use_case() -> RegisterUserUseCase:
    return RegisterUserUseCase(
        user_repository=get_user_repository(),
        password_hasher=get_password_hasher(),
    )


def get_login_user_use_case() -> LoginUserUseCase:
    return LoginUserUseCase(
        user_repository=get_user_repository(),
        password_verifier=get_password_verifier(),
        token_provider=get_token_provider(),
    )

def get_current_user_use_case() -> GetCurrentUserUseCase:
    return GetCurrentUserUseCase(
        user_repository=get_user_repository(),
    )