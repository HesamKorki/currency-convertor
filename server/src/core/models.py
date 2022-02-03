from enum import Enum

from pydantic import BaseModel, Field


class Currency(str, Enum):
    USD = "USD"
    EUR = "EUR"
    JPY = "JPY"


class Response(BaseModel):
    value: float = Field(description="The value of the currency in the target currency")
    currency: Currency = Field(description="The target currency")
