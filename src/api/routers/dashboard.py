from __future__ import annotations

"""
Dashboard Router.

===============================================================================
Purpose
===============================================================================

Provides the initial dashboard information displayed after user
authentication.

Rather than forcing the frontend to perform multiple requests, this endpoint
aggregates the most relevant information required to render the application's
home screen.

Initially the dashboard contains only financial accounts.

Future versions will also include:

    • cash flow summary;

    • monthly balance;

    • pending bills;

    • financial goals;

    • investments;

    • financial health score;

    • AI recommendations.

===============================================================================
Architecture
===============================================================================

Frontend

        │

        ▼

Dashboard Router

        │

        ▼

Dashboard Use Case

        │

        ▼

Application Layer
"""

from fastapi import APIRouter
from fastapi import Depends

from src.api.dependencies.auth import get_current_user
from src.domain.value_objects.token_claims import TokenClaims

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "",
    summary="Dashboard",
    description="""
Returns the information required to render the application's dashboard.

This endpoint is intentionally designed to evolve over time as new financial
modules are introduced.
""",
)
def dashboard(
    current_user: TokenClaims = Depends(
        get_current_user,
    ),
):
    """
    Returns dashboard information.

    Temporary implementation.
    """

    return {
        "user_id": str(current_user.id),
        "message": "Dashboard endpoint available.",
    }