from __future__ import annotations

from src.api.dependencies.repositories import (
    get_user_repository,
)
from src.api.dependencies.services import (
    get_password_verifier,
    get_token_provider,
)
from src.application.use_cases.auth.get_current_user import (
    GetCurrentUserUseCase,
)
from src.application.use_cases.auth.login_user import (
    LoginUserUseCase,
)
from src.application.use_cases.auth.register_user import (
    RegisterUserUseCase,
)
from src.domain.repositories.unit_of_work import UnitOfWork
from src.infrastructure.persistence.sqlalchemy.sqlalchemy_unit_of_work import (
    SqlAlchemyUnitOfWork,
)

from .repositories import get_session_factory
from .services import (
    get_password_hasher,
    get_password_verifier,
    get_token_provider,
)


def get_unit_of_work() -> UnitOfWork:
    """
    Creates a new UnitOfWork.

    Every request receives its own transactional scope.
    """

    return SqlAlchemyUnitOfWork(
        session_factory=get_session_factory(),
    )


def get_register_user_use_case() -> RegisterUserUseCase:
    """
    Creates the RegisterUser use case.
    """

    return RegisterUserUseCase(
        unit_of_work=get_unit_of_work(),
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