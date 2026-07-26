from __future__ import annotations

from datetime import datetime

from src.application.dto.auth.login_request import LoginRequest
from src.application.dto.auth.login_response import LoginResponse
from src.domain.exceptions.invalid_credentials_error import (
    InvalidCredentialsError,
)
from src.domain.repositories.user_repository import UserRepository
from src.domain.services.password_verifier import PasswordVerifier
from src.domain.services.token_provider import TokenProvider
from src.domain.value_objects.email import Email
from src.domain.value_objects.password import Password
from src.domain.value_objects.token_claims import TokenClaims


class LoginUserUseCase:
    """
    Handles user authentication.
    """

    def __init__(
        self,
        user_repository: UserRepository,
        password_verifier: PasswordVerifier,
        token_provider: TokenProvider,
    ) -> None:
        self._user_repository = user_repository
        self._password_verifier = password_verifier
        self._token_provider = token_provider

    def execute(
        self,
        request: LoginRequest,
    ) -> LoginResponse:
        """
        Authenticates a user.
        """
        email = Email(request.email)
        password = Password(request.password)

        user = self._user_repository.find_by_email(email)

        if user is None:
            raise InvalidCredentialsError()

        if not self._password_verifier.verify(
            password,
            user.password,
        ):
            raise InvalidCredentialsError()

        claims = TokenClaims(
            user_id=user.id,
            name=user.name,
            email=str(user.email),
        )

        access_token = self._token_provider.generate_access_token(
            claims,
        )

        return LoginResponse(
            id=user.id,
            name=user.name,
            email=str(user.email),
            access_token=access_token,
            authenticated_at=datetime.now(),
        )
