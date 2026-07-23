"""Contratos HTTP da API.

Valores monetários devem ser enviados como strings decimais, por exemplo
`"1250.50"`, para preservar precisão entre o navegador e o domínio.
"""

from datetime import date
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, Field


class TransactionInput(BaseModel):
    date: date
    amount: Decimal = Field(gt=0, decimal_places=2)
    type: Literal["income", "expense", "adjustment"]
    description: str = Field(min_length=1, max_length=200)
    category: str = Field(min_length=1, max_length=100)


class PlanAnalysisRequest(BaseModel):
    start_date: date
    end_date: date
    opening_balance: Decimal = Field(decimal_places=2)
    transactions: list[TransactionInput] = Field(default_factory=list)


class LiquidityResponse(BaseModel):
    minimum_balance: Decimal
    maximum_balance: Decimal
    ending_balance: Decimal
    first_negative_day: date | None
    negative_days: int
    has_negative_balance: bool


class ScoreResponse(BaseModel):
    overall: int
    liquidity: int
    reserve: int
    credit_dependency: int
    stability: int
    risk: int


class PlanAnalysisResponse(BaseModel):
    score: ScoreResponse
    liquidity: LiquidityResponse
    summary: str
    highlights: list[str]
