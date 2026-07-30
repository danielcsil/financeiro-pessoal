from __future__ import annotations

from src.domain.entities.user import (
    User,
    UserStatus,
)
from src.domain.value_objects.email import Email
from src.domain.value_objects.hashed_password import (
    HashedPassword,
)
from src.infrastructure.persistence.sqlalchemy.models.user_model import (
    UserModel,
)


class UserMapper:
    """
    Maps between the domain User entity and the SQLAlchemy UserModel.
    """

    @staticmethod
    def to_model(user: User) -> UserModel:
        """
        Converts a domain entity into a persistence model.
        """

        return UserModel(
            id=user.id,
            name=user.name,
            email=user.email.value,
            hashed_password=user.password.value,
            is_active=user.status is UserStatus.ACTIVE,
            email_verified=user.email_verified,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    @staticmethod
    def to_domain(model: UserModel) -> User:
        """
        Converts a persistence model into a domain entity.
        """

        user = User(
            id=model.id,
            name=model.name,
            email=Email(model.email),
            password=HashedPassword(model.hashed_password),
            email_verified=model.email_verified,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

        user.status = (
            UserStatus.ACTIVE
            if model.is_active
            else UserStatus.DISABLED
        )

        return user