from fastapi import APIRouter, Depends, status

from src.api.dependencies.auth import get_current_user
from src.api.dependencies.use_cases import (
    get_login_user_use_case,
    get_register_user_use_case,
)
from src.api.schemas.auth.current_user_response import CurrentUserResponse
from src.api.schemas.auth.login_request import LoginRequest
from src.api.schemas.auth.login_response import LoginResponse
from src.api.schemas.auth.register_request import RegisterRequest
from src.api.schemas.auth.register_response import RegisterResponse
from src.application.dto.auth.login_request import LoginRequest as LoginUserRequest
from src.application.dto.auth.register_user_request import RegisterUserRequest
from src.application.use_cases.auth.login_user import LoginUserUseCase
from src.application.use_cases.auth.register_user import RegisterUserUseCase

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=RegisterResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    request: RegisterRequest,
    use_case: RegisterUserUseCase = Depends(get_register_user_use_case),
) -> RegisterResponse:
    response = use_case.execute(
        RegisterUserRequest(
            name=request.name,
            email=request.email,
            password=request.password,
            confirm_password=request.password_confirmation,
            accepted_terms=request.accept_terms,
        )
    )

    return RegisterResponse(
        id=response.id,
        name=response.name,
        email=response.email,
    )


@router.post(
    "/login",
    response_model=LoginResponse,
)
def login(
    request: LoginRequest,
    use_case: LoginUserUseCase = Depends(get_login_user_use_case),
) -> LoginResponse:
    response = use_case.execute(
        LoginUserRequest(
            email=request.email,
            password=request.password,
        )
    )

    return LoginResponse(
        id=response.id,
        name=response.name,
        email=response.email,
        access_token=response.access_token,
        authenticated_at=response.authenticated_at,
    )


@router.get(
    "/me",
    response_model=CurrentUserResponse,
)
def me(
    current_user: CurrentUserResponse = Depends(get_current_user),
) -> CurrentUserResponse:
    return current_user