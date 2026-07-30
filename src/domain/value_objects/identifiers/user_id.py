from __future__ import annotations

from uuid import UUID

from src.domain.value_objects.identifiers.entity_id import (
    EntityId,
)


class UserId(EntityId):
    """
    Strongly typed identifier for the User aggregate.

    This class adds semantic meaning to UUIDs and helps prevent
    mixing identifiers from different aggregates.
    """

    @classmethod
    def new(cls) -> "UserId":
        """
        Creates a new user identifier.
        """
        return cls(super().new().value)

    @classmethod
    def from_uuid(
        cls,
        value: UUID,
    ) -> "UserId":
        """
        Creates a UserId from an existing UUID.
        """
        return cls(value)

    @classmethod
    def from_string(
        cls,
        value: str,
    ) -> "UserId":
        """
        Creates a UserId from a UUID string.
        """
        return cls(UUID(value))