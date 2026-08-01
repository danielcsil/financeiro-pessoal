from __future__ import annotations

from src.application.dto.auth.register_user_request import (
    RegisterUserRequest,
)
from src.application.dto.auth.register_user_response import (
    RegisterUserResponse,
)
from src.domain.entities.user import User
from src.domain.exceptions import (
    EmailAlreadyExistsError,
    PasswordMismatchError,
    RequiredFieldError,
    TermsNotAcceptedError,
)
from src.domain.repositories.unit_of_work import UnitOfWork
from src.domain.services.password_hasher import PasswordHasher
from src.domain.value_objects.email import Email
from src.domain.value_objects.hashed_password import (
    HashedPassword,
)
from src.domain.value_objects.password import Password


class _RepositoryUnitOfWork:
    def __init__(self, user_repository) -> None:
        self.users = user_repository

    def __enter__(self) -> "_RepositoryUnitOfWork":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        return None

    def commit(self) -> None:
        return None

    def rollback(self) -> None:
        return None


class RegisterUserUseCase:
    """
    Use case responsible for registering a new user.
    """

    def __init__(
        self,
        unit_of_work: UnitOfWork | None = None,
        password_hasher: PasswordHasher | None = None,
        user_repository=None,
    ) -> None:
        if unit_of_work is None:
            if user_repository is None:
                raise TypeError(
                    "unit_of_work or user_repository must be provided."
                )

            unit_of_work = _RepositoryUnitOfWork(user_repository)

        if password_hasher is None:
            raise TypeError("password_hasher must be provided.")

        self._uow = unit_of_work
        self._password_hasher = password_hasher

    def execute(
        self,
        request: RegisterUserRequest,
    ) -> RegisterUserResponse:
        """
        Registers a new user.
        """

        name = request.name.strip()

        if not name:
            raise RequiredFieldError(
                "Name is required."
            )

        email = Email(request.email)
        password = Password(request.password)

        if request.password != request.confirm_password:
            raise PasswordMismatchError(
                "Passwords do not match."
            )

        if not request.accepted_terms:
            raise TermsNotAcceptedError(
                "Terms must be accepted."
            )

        with self._uow as uow:

            if uow.users.exists_by_email(email):
                raise EmailAlreadyExistsError(
                    "Email already registered."
                )

            hashed_password = HashedPassword(
                self._password_hasher.hash(
                    password.value
                )
            )

            user = User.create(
                name=name,
                email=email,
                password=hashed_password,
            )

            uow.users.add(user)

            uow.commit()

        return RegisterUserResponse(
            id=user.id,
            name=user.name,
            email=user.email.value,
            email_verified=user.email_verified,
            created_at=user.created_at,
        )
