from __future__ import annotations

from uuid import UUID

from src.application.dto.auth.current_user_response import (
    CurrentUserResponse,
)
from src.domain.exceptions import InvalidCredentialsError
from src.domain.repositories.user_repository import UserRepository


class GetCurrentUserUseCase:

    def __init__(
        self,
        user_repository: UserRepository,
    ) -> None:
        self._repository = user_repository

    def execute(
        self,
        user_id: UUID,
    ) -> CurrentUserResponse:

        user = self._repository.find_by_id(user_id)

        if user is None:
            raise InvalidCredentialsError()

        return CurrentUserResponse(
            id=user.id,
            name=user.name,
            email=str(user.email),
        )