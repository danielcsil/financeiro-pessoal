from fastapi import FastAPI

from src.api.routers.health import router as health_router
from src.api.routers.auth import router as auth_router
from src.api.exception_handlers.domain import (
    register_domain_exception_handlers,
)
from src.api.exception_handlers.validation import (
    register_validation_exception_handler,
)

app = FastAPI(
    title="Personal Finance API",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(auth_router)

register_domain_exception_handlers(app)
register_validation_exception_handler(app)