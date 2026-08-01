from __future__ import annotations

"""
Get Current User Use Case.

===============================================================================
Purpose
===============================================================================

Retrieves the authenticated user's information.

This use case is typically executed after JWT authentication to obtain the
current user's profile.

===============================================================================
Architecture
===============================================================================

Application Layer

        │

        ▼

GetCurrentUserUseCase

        │

        ▼

UnitOfWork

        │

        ▼

UserRepository
"""

from uuid import UUID

from src.application.dto.auth.current_user_response import (
    CurrentUserResponse,
)
from src.domain.exceptions.invalid_credentials_error import (
    InvalidCredentialsError,
)
from src.domain.repositories.unit_of_work import (
    UnitOfWork,
)


class GetCurrentUserUseCase:
    """
    Retrieves information about the authenticated user.
    """

    def __init__(
        self,
        unit_of_work: UnitOfWork,
    ) -> None:
        self._unit_of_work = unit_of_work

    def execute(
        self,
        user_id: UUID,
    ) -> CurrentUserResponse:
        """
        Retrieves the authenticated user.

        Parameters
        ----------
        user_id:
            Identifier extracted from the authenticated JWT.

        Returns
        -------
        CurrentUserResponse
            Current authenticated user.

        Raises
        ------
        InvalidCredentialsError
            If the user no longer exists.
        """

        with self._unit_of_work as uow:

            user = uow.users.find_by_id(
                user_id,
            )

        if user is None:
            raise InvalidCredentialsError()

        return CurrentUserResponse(
            id=user.id,
            name=user.name,
            email=str(user.email),
        )