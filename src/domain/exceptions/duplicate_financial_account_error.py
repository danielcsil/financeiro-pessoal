from __future__ import annotations


class DuplicateFinancialAccountError(Exception):
    """
    Raised when a user attempts to create a financial
    account with a name that already exists.

    Account names must be unique per user.
    """

    def __init__(
        self,
        account_name: str,
    ) -> None:
        super().__init__(
            f"A financial account named '{account_name}' already exists."
        )

        self.account_name = account_name