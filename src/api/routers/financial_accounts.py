from __future__ import annotations

"""
Financial Accounts REST API.

===============================================================================
Purpose
===============================================================================

This module exposes the REST endpoints responsible for managing the user's
financial accounts.

A financial account represents the source or destination of financial
resources within the Personal Finance system, such as:

    • Checking accounts;

    • Savings accounts;

    • Investment accounts;

    • Cash wallets;

    • Digital accounts.

Every financial transaction recorded by the application belongs to exactly one
financial account.

===============================================================================
Architectural Responsibilities
===============================================================================

This router belongs exclusively to the Presentation Layer.

Its responsibilities are intentionally limited to:

    • validating HTTP requests;

    • invoking the appropriate Application Use Case;

    • converting API Schemas into Application DTOs;

    • converting Use Case results into API Schemas;

    • returning HTTP responses.

Business rules, persistence and transaction management belong to the
Application and Domain layers.

===============================================================================
Available Endpoints
===============================================================================

POST /financial-accounts

    Creates a new financial account.

GET /financial-accounts

    Lists every active financial account belonging to the authenticated user.

Future versions will include:

GET    /financial-accounts/{id}

PUT    /financial-accounts/{id}

DELETE /financial-accounts/{id}
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status

from uuid import UUID

from src.api.dependencies.use_cases import (
    get_get_financial_account_use_case,
)
from src.api.schemas.financial_account.get_financial_account_response import (
    GetFinancialAccountResponse,
)
from src.application.use_cases.financial_account.get_financial_account import (
    GetFinancialAccountUseCase,
)

from src.api.dependencies.auth import (
    get_current_user,
)
from src.api.dependencies.use_cases import (
    get_create_financial_account_use_case,
    get_list_financial_accounts_use_case,
)
from src.api.schemas.financial_account.create_financial_account_request import (
    CreateFinancialAccountRequest,
)
from src.api.schemas.financial_account.create_financial_account_response import (
    CreateFinancialAccountResponse,
)
from src.api.schemas.financial_account.list_financial_accounts_response import (
    ListFinancialAccountsResponse,
)
from src.application.dto.financial_account.create_financial_account_request import (
    CreateFinancialAccountRequest as CreateFinancialAccountDTO,
)
from src.application.use_cases.financial_account.create_financial_account import (
    CreateFinancialAccountUseCase,
)
from src.application.use_cases.financial_account.list_financial_accounts import (
    ListFinancialAccountsUseCase,
)
from src.domain.value_objects.token_claims import (
    TokenClaims,
)

from src.api.dependencies.use_cases import (
    get_update_financial_account_use_case,
)

from src.api.schemas.financial_account.update_financial_account_request import (
    UpdateFinancialAccountRequest,
)

from src.api.schemas.financial_account.update_financial_account_response import (
    UpdateFinancialAccountResponse,
)

from src.application.dto.financial_account.update_financial_account_request import (
    UpdateFinancialAccountRequest as UpdateFinancialAccountDTO,
)

from src.application.use_cases.financial_account.update_financial_account import (
    UpdateFinancialAccountUseCase,
)

router = APIRouter(
    prefix="/financial-accounts",
    tags=["Financial Accounts"],
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Authentication required.",
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "Operation not permitted.",
        },
    },
)


@router.post(
    "",
    response_model=CreateFinancialAccountResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create financial account",
    description="""
Creates a new financial account for the authenticated user.

A financial account is the primary container used to organize the user's
financial resources.

Examples include:

- Checking Account
- Savings Account
- Investment Account
- Cash Wallet

The newly created account becomes immediately available for future
transactions, cash flow projections, financial planning and reporting.
""",
    responses={
        status.HTTP_201_CREATED: {
            "description": "Financial account successfully created.",
        },
        status.HTTP_409_CONFLICT: {
            "description": "Another account with the same name already exists.",
        },
    },
)
def create_financial_account(
    request: CreateFinancialAccountRequest,
    response: Response,
    current_user: TokenClaims = Depends(
        get_current_user,
    ),
    use_case: CreateFinancialAccountUseCase = Depends(
        get_create_financial_account_use_case,
    ),
) -> CreateFinancialAccountResponse:
    """
    Creates a new financial account.

    Authentication
    --------------
    Requires a valid JWT Bearer Token.

    Notes
    -----
    The authenticated user is automatically assigned as the owner of the new
    account. Client applications cannot create accounts for other users.

    Returns
    -------
    HTTP 201 Created

        Newly created financial account.
    """

    result = use_case.execute(
        CreateFinancialAccountDTO(
            user_id=current_user.user_id,
            name=request.name,
            institution=request.institution,
            account_type=request.account_type,
            initial_balance=request.initial_balance,
            color=request.color,
            icon=request.icon,
            include_in_cash_flow=request.include_in_cash_flow,
            include_in_net_worth=request.include_in_net_worth,
        )
    )

    response.headers["Location"] = (
        f"/api/financial-accounts/{result.id}"
    )

    return CreateFinancialAccountResponse(
        **result.__dict__,
    )


@router.get(
    "",
    response_model=ListFinancialAccountsResponse,
    status_code=status.HTTP_200_OK,
    summary="List financial accounts",
    description="""
    Returns every active financial account belonging to the authenticated user.

    Only accounts owned by the current authenticated user are returned.
    """,
    )

def list_financial_accounts(
        current_user: TokenClaims = Depends(
            get_current_user,
        ),
        use_case: ListFinancialAccountsUseCase = Depends(
            get_list_financial_accounts_use_case,
        ),
    ) -> ListFinancialAccountsResponse:
        """
        Lists every financial account owned by the authenticated user.
        """

        result = use_case.execute(
            current_user.user_id,
        )

        return ListFinancialAccountsResponse(
            **result.__dict__,
        )

@router.get(
    "/{account_id}",
    response_model=GetFinancialAccountResponse,
    status_code=status.HTTP_200_OK,
    summary="Get financial account",
    description="""
Retrieves a single financial account belonging to the authenticated user.

The endpoint returns the complete information of a financial account.

If the account does not exist or belongs to another user,
the API returns **404 Not Found**.

Future versions may include additional computed information such as:

- current month's balance;

- pending transactions;

- projected balance;

- account statistics.
""",
    responses={
        status.HTTP_200_OK: {
            "description": "Financial account successfully retrieved.",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Financial account not found.",
        },
    },
)
def get_financial_account(
    account_id: UUID,
    current_user: TokenClaims = Depends(
        get_current_user,
    ),
    use_case: GetFinancialAccountUseCase = Depends(
        get_get_financial_account_use_case,
    ),
) -> GetFinancialAccountResponse:
    """
    Retrieves a single financial account.

    Authentication
    --------------
    Requires a valid JWT Bearer Token.

    Parameters
    ----------
    account_id:
        Unique identifier of the requested financial account.

    Returns
    -------
    HTTP 200 OK

        Complete information about the requested financial account.

    Raises
    ------
    HTTP 404 Not Found

        Returned when the account does not exist or does not belong to the
        authenticated user.
    """

    result = use_case.execute(
        user_id=current_user.user_id,
        account_id=account_id,
    )

    return GetFinancialAccountResponse(
        **result.__dict__,
    )

@router.put(
    "/{account_id}",
    response_model=UpdateFinancialAccountResponse,
    status_code=status.HTTP_200_OK,
    summary="Update financial account",
    description="""
Updates an existing financial account owned by the authenticated user.

Only editable properties may be modified.

The account ownership is always validated before the update is performed.

The current balance is intentionally not editable through this endpoint,
since it is derived from financial transactions.

Future versions may also allow:

- changing account status;

- changing display order;

- configuring synchronization options.
""",
    responses={
        status.HTTP_200_OK: {
            "description": "Financial account successfully updated.",
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Financial account not found.",
        },
        status.HTTP_409_CONFLICT: {
            "description": "Another account with the same name already exists.",
        },
    },
)
def update_financial_account(
    account_id: UUID,
    request: UpdateFinancialAccountRequest,
    current_user: TokenClaims = Depends(
        get_current_user,
    ),
    use_case: UpdateFinancialAccountUseCase = Depends(
        get_update_financial_account_use_case,
    ),
) -> UpdateFinancialAccountResponse:
    """
    Updates an existing financial account.

    Authentication
    --------------
    Requires a valid JWT Bearer Token.

    Parameters
    ----------
    account_id:
        Unique identifier of the financial account.

    request:
        Updated account information.

    Returns
    -------
    HTTP 200 OK

        Updated financial account.
    """

    result = use_case.execute(
        UpdateFinancialAccountDTO(
            user_id=current_user.user_id,
            account_id=account_id,
            name=request.name,
            institution=request.institution,
            account_type=request.account_type,
            color=request.color,
            icon=request.icon,
            include_in_cash_flow=request.include_in_cash_flow,
            include_in_net_worth=request.include_in_net_worth,
        )
    )

    return UpdateFinancialAccountResponse(
        **result.__dict__,
    )