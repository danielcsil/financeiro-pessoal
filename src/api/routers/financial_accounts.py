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

    • converting Application DTOs into API Schemas;

    • returning HTTP responses.

Business rules, persistence and transaction management belong to the
Application and Domain layers.
"""

from dataclasses import asdict
from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status

from src.api.dependencies.auth import get_current_user
from src.api.dependencies.use_cases import (
    get_create_financial_account_use_case,
    get_get_financial_account_use_case,
    get_list_financial_accounts_use_case,
    get_update_financial_account_use_case,
)

from src.api.schemas.financial_account.create_financial_account_request import (
    CreateFinancialAccountRequest,
)
from src.api.schemas.financial_account.create_financial_account_response import (
    CreateFinancialAccountResponse as CreateFinancialAccountSchema,
)
from src.api.schemas.financial_account.get_financial_account_response import (
    GetFinancialAccountResponse,
)
from src.api.schemas.financial_account.list_financial_accounts_response import (
    ListFinancialAccountsResponse,
)
from src.api.schemas.financial_account.update_financial_account_request import (
    UpdateFinancialAccountRequest,
)
from src.api.schemas.financial_account.update_financial_account_response import (
    UpdateFinancialAccountResponse,
)

from src.application.dto.financial_account.create_financial_account_request import (
    CreateFinancialAccountRequest as CreateFinancialAccountDTO,
)
from src.application.dto.financial_account.update_financial_account_request import (
    UpdateFinancialAccountRequest as UpdateFinancialAccountDTO,
)

from src.application.use_cases.financial_account.create_financial_account import (
    CreateFinancialAccountUseCase,
)
from src.application.use_cases.financial_account.get_financial_account import (
    GetFinancialAccountUseCase,
)
from src.application.use_cases.financial_account.list_financial_accounts import (
    ListFinancialAccountsUseCase,
)
from src.application.use_cases.financial_account.update_financial_account import (
    UpdateFinancialAccountUseCase,
)

from src.domain.value_objects.token_claims import TokenClaims

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
    response_model=CreateFinancialAccountSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Create financial account",
    description="""
Creates a new financial account for the authenticated user.
""",
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
) -> CreateFinancialAccountSchema:
    """
    Creates a new financial account.
    """

    result = use_case.execute(
        CreateFinancialAccountDTO(
            user_id=current_user.id,
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

    return CreateFinancialAccountSchema(
        **asdict(result),
    )


@router.get(
    "",
    response_model=ListFinancialAccountsResponse,
    status_code=status.HTTP_200_OK,
    summary="List financial accounts",
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

    return use_case.execute(
        current_user.id,
    )


@router.get(
    "/{account_id}",
    response_model=GetFinancialAccountResponse,
    status_code=status.HTTP_200_OK,
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
    """

    result = use_case.execute(
        user_id=current_user.id,
        account_id=account_id,
    )

    return GetFinancialAccountResponse(
        **asdict(result),
    )


@router.put(
    "/{account_id}",
    response_model=UpdateFinancialAccountResponse,
    status_code=status.HTTP_200_OK,
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
    """

    result = use_case.execute(
        UpdateFinancialAccountDTO(
            user_id=current_user.id,
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
        **asdict(result),
    )