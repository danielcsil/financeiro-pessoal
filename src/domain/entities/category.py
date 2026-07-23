
from __future__ import annotations

from uuid import UUID, uuid4

from src.domain.enums import CategoryType


class Category:

    def __init__(
        self,
        name: str,
        type: CategoryType,
        id: UUID | None = None,
    ):
        self._id = id or uuid4()
        self._active = True
        self._type = type
        self.rename(name)

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> CategoryType:
        return self._type

    @property
    def active(self) -> bool:
        return self._active

    def rename(self, new_name: str) -> None:
        new_name = new_name.strip()

        if not new_name:
            raise ValueError("Category name cannot be empty.")

        self._name = new_name

    def activate(self) -> None:
        self._active = True

    def deactivate(self) -> None:
        self._active = False

    def __str__(self) -> str:
        return self._name
