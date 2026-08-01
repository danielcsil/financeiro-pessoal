from __future__ import annotations

"""
Login User Use Case.

===============================================================================
Purpose
===============================================================================

Authenticates an existing user and generates an access token.

This use case validates the supplied credentials and, when successful,
returns the authenticated user together with a JWT access token.

===============================================================================
Business Rules
===============================================================================

The use case validates that:

    • the informed e-mail belongs to an existing user;

    • the supplied password matches the stored password hash.

If any validation fails, an InvalidCredentialsError is raised.

===============================================================================
Architecture
===============================================================================

Application Layer

        │

        ▼

LoginUserUseCase

        │

        ▼

UnitOfWork

        │

        ▼

UserRepository

===============================================================================
Transaction
===============================================================================

This use case performs read operations only.

No transaction is committed.
"""

from datetime import datetime
from datetime import UTC

from src.application.dto.auth.login_request import (
    LoginRequest,
)
from src.application.dto.auth.login_response import (
    LoginResponse,
)
from src.domain.exceptions.invalid_credentials_error import (
    InvalidCredentialsError,
)
from src.domain.repositories.unit_of_work import (
    UnitOfWork,
)
from src.domain.services.password_verifier import (
    PasswordVerifier,
)
from src.domain.services.token_provider import (
    TokenProvider,
)
from src.domain.value_objects.email import (
    Email,
)
from src.domain.value_objects.password import (
    Password,
)
from src.domain.value_objects.token_claims import (
    TokenClaims,
)


class LoginUserUseCase:
    """
    Authenticates an existing user.
    """

    def __init__(
        self,
        unit_of_work: UnitOfWork,
        password_verifier: PasswordVerifier,
        token_provider: TokenProvider,
    ) -> None:
        self._unit_of_work = unit_of_work
        self._password_verifier = password_verifier
        self._token_provider = token_provider

    def execute(
        self,
        request: LoginRequest,
    ) -> LoginResponse:
        """
        Authenticates a user and returns an access token.

        Parameters
        ----------
        request:
            Login credentials.

        Returns
        -------
        LoginResponse
            Authenticated user information and JWT token.

        Raises
        ------
        InvalidCredentialsError
            If the e-mail does not exist or the password is invalid.
        """

        email = Email(
            request.email,
        )

        password = Password(
            request.password,
        )

        with self._unit_of_work as uow:

            user = uow.users.find_by_email(
                email,
            )

            if user is None:
                raise InvalidCredentialsError()

            if not self._password_verifier.verify(
                password=password,
                password_hash=user.password,
            ):
                raise InvalidCredentialsError()

            claims = TokenClaims(
                user_id=user.id,
                name=user.name,
                email=str(user.email),
            )

            access_token = (
                self._token_provider.generate_access_token(
                    claims,
                )
            )

            return LoginResponse(
                id=user.id,
                name=user.name,
                email=str(user.email),
                access_token=access_token,
                authenticated_at=datetime.now(
                    UTC,
                ),
            )