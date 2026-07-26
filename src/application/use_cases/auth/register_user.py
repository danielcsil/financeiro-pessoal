from __future__ import annotations

from src.application.dto.auth.register_user_request import (
    RegisterUserRequest,
)
from src.application.dto.auth.register_user_response import (
    RegisterUserResponse,
)
from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository
from src.domain.services.password_hasher import PasswordHasher
from src.domain.value_objects.email import Email

from src.domain.exceptions import (
    PasswordMismatchError,
    RequiredFieldError,
    TermsNotAcceptedError,
    EmailAlreadyExistsError
)

from src.domain.value_objects.password import Password
from src.domain.value_objects.hashed_password import HashedPassword

class RegisterUserUseCase:
    """
    Handles the user registration process.
    """

    def __init__(
        self,
        user_repository: UserRepository,
        password_hasher: PasswordHasher,
    ) -> None:
        self._user_repository = user_repository
        self._password_hasher = password_hasher

    def execute(
        self,
        request: RegisterUserRequest,
    ) -> RegisterUserResponse:
        """
        Registers a new user.
        """

        name = request.name.strip()
        email = Email(request.email)
        password = Password(request.password)

        if not name:
            raise RequiredFieldError("Name is required.")

        if not email:
            raise RequiredFieldError("Email is required.")

        if request.password != request.confirm_password:
            raise PasswordMismatchError("Passwords do not match.")

        if not request.accepted_terms:
            raise TermsNotAcceptedError("Terms must be accepted.")

        if self._user_repository.exists_by_email(email):
            raise EmailAlreadyExistsError("Email already registered.")

        password_hash = HashedPassword(
            self._password_hasher.hash(password.value)
        )

        user = User(
            name=name,
            email=email,
            password=password_hash,
        )

        self._user_repository.save(user)

        return RegisterUserResponse(
            id=user.id,
            name=user.name,
            email=user.email.value,
            email_verified=user.email_verified,
            created_at=user.created_at,
        )