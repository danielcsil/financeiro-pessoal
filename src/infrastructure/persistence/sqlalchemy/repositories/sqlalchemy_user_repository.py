from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.domain.entities.user import User
from src.domain.exceptions import EmailAlreadyExistsError
from src.domain.repositories.user_repository import UserRepository
from src.domain.value_objects.email import Email
from src.infrastructure.persistence.sqlalchemy.mappers.user_mapper import (
    UserMapper,
)
from src.infrastructure.persistence.sqlalchemy.models.user_model import (
    UserModel,
)


class SqlAlchemyUserRepository(UserRepository):
    """
    SQLAlchemy implementation of UserRepository.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:
        self._session = session

    def add(
        self,
        user: User,
    ) -> None:
        """
        Adds a new user to the current Unit of Work.
        """

        self._session.add(
            UserMapper.to_model(user)
        )

        self._flush()

    def remove(
        self,
        user: User,
    ) -> None:
        """
        Removes a user from the current Unit of Work.
        """

        model = self._session.get(
            UserModel,
            user.id,
        )

        if model is not None:
            self._session.delete(model)

    def find_by_id(
        self,
        user_id: UUID,
    ) -> User | None:
        """
        Finds a user by its identifier.
        """

        model = self._session.get(
            UserModel,
            user_id,
        )

        if model is None:
            return None

        return UserMapper.to_domain(model)

    def find_by_email(
        self,
        email: Email,
    ) -> User | None:
        """
        Finds a user by e-mail.
        """

        statement = (
            select(UserModel)
            .where(UserModel.email == email.value)
        )

        model = (
            self._session.execute(statement)
            .scalar_one_or_none()
        )

        if model is None:
            return None

        return UserMapper.to_domain(model)

    def exists_by_id(
        self,
        user_id: UUID,
    ) -> bool:
        """
        Checks whether a user exists.
        """

        statement = (
            select(UserModel.id)
            .where(UserModel.id == user_id)
            .limit(1)
        )

        return (
            self._session.execute(statement)
            .scalar_one_or_none()
            is not None
        )

    def exists_by_email(
        self,
        email: Email,
    ) -> bool:
        """
        Checks whether an e-mail is already registered.
        """

        statement = (
            select(UserModel.id)
            .where(UserModel.email == email.value)
            .limit(1)
        )

        return (
            self._session.execute(statement)
            .scalar_one_or_none()
            is not None
        )

    def _flush(self) -> None:
        """
        Flushes pending SQL statements.

        Commit remains the responsibility of the Unit of Work.
        """

        try:
            self._session.flush()

        except IntegrityError as exc:
            raise EmailAlreadyExistsError(
                "Email already registered."
            ) from exc