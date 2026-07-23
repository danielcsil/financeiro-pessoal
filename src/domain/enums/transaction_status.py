
from enum import Enum


class TransactionStatus(str, Enum):
    PENDING = "pending"
    POSTED = "posted"
    CANCELLED = "cancelled"
    REVERSED = "reversed"
