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
        email = request.email.strip().lower()

        if not name:
            raise ValueError("Name is required.")

        if not email:
            raise ValueError("Email is required.")

        if not request.password:
            raise ValueError("Password is required.")

        if request.password != request.confirm_password:
            raise ValueError("Passwords do not match.")

        if not request.accepted_terms:
            raise ValueError("Terms must be accepted.")

        if self._user_repository.exists_by_email(email):
            raise ValueError("Email already registered.")

        password_hash = self._password_hasher.hash(
            request.password
        )

        user = User(
            name=name,
            email=email,
            password_hash=password_hash,
        )

        self._user_repository.save(user)

        return RegisterUserResponse(
            id=user.id,
            name=user.name,
            email=user.email,
            email_verified=user.email_verified,
            created_at=user.created_at,
        )