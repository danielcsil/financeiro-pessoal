from __future__ import annotations

"""
Register User Use Case.

===============================================================================
Purpose
===============================================================================

Registers a new user in the system.

This use case validates the registration request, verifies business rules,
creates the User aggregate and persists it using the application's
transactional Unit of Work.

===============================================================================
Business Rules
===============================================================================

The following rules are enforced:

    • Name is required.

    • Email must be valid.

    • Password must be valid.

    • Password confirmation must match.

    • Terms of use must be accepted.

    • Email must be unique.

===============================================================================
Architecture
===============================================================================

Application Layer

        │

        ▼

RegisterUserUseCase

        │

        ▼

UnitOfWork

        │

        ▼

UserRepository

===============================================================================
Transaction
===============================================================================

The registration process is transactional.

If any validation fails, no data is persisted.
"""

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
from src.domain.repositories.unit_of_work import (
    UnitOfWork,
)
from src.domain.services.password_hasher import (
    PasswordHasher,
)
from src.domain.value_objects.email import (
    Email,
)
from src.domain.value_objects.hashed_password import (
    HashedPassword,
)
from src.domain.value_objects.password import (
    Password,
)


class RegisterUserUseCase:
    """
    Registers a new user.
    """

    def __init__(
        self,
        unit_of_work: UnitOfWork,
        password_hasher: PasswordHasher,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._password_hasher = password_hasher

    def execute(
        self,
        request: RegisterUserRequest,
    ) -> RegisterUserResponse:
        """
        Registers a new user.

        Parameters
        ----------
        request:
            Registration request.

        Returns
        -------
        RegisterUserResponse
            Newly created user.

        Raises
        ------
        RequiredFieldError
            If the name is empty.

        PasswordMismatchError
            If password confirmation does not match.

        TermsNotAcceptedError
            If the terms were not accepted.

        EmailAlreadyExistsError
            If another user already owns the same e-mail.
        """

        name = request.name.strip()

        if not name:
            raise RequiredFieldError(
                "Name is required.",
            )

        email = Email(
            request.email,
        )

        password = Password(
            request.password,
        )

        if request.password != request.confirm_password:
            raise PasswordMismatchError(
                "Passwords do not match.",
            )

        if not request.accepted_terms:
            raise TermsNotAcceptedError(
                "Terms must be accepted.",
            )

        with self._unit_of_work as uow:

            if uow.users.exists_by_email(
                email,
            ):
                raise EmailAlreadyExistsError(
                    "Email already registered.",
                )

            hashed_password = HashedPassword(
                self._password_hasher.hash(
                    password.value,
                ),
            )

            user = User.create(
                name=name,
                email=email,
                password=hashed_password,
            )

            uow.users.add(
                user,
            )

            uow.commit()

            return RegisterUserResponse(
                id=user.id,
                name=user.name,
                email=user.email.value,
                email_verified=user.email_verified,
                created_at=user.created_at,
            )