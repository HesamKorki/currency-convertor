import time
from typing import Tuple

import requests

from utils import api
from core.models import Currency


def get_ttl_hash(ttl_seconds: int = 60 * 60):
    return round(time.time() / ttl_seconds)


def compute_exchange_value(
    target: Currency, currency: Currency, value: float, decimal_place: int
) -> Tuple[float, requests.models.Response]:
    """computes the exchange value of the given value in the given currency.

    Args:
        target (Currency): [The desired target currency
        currency (Currency): [The base currency in which the value is defined]
        value (float): [The value of the given currency]
        decimal_place (int): [decimal places to round the output value]

    Returns:
        Tuple[float, requests.models.Response]: [either returns the value without error or returns none value and the response object for error handling]
    """
    upstream = api.get_exchange_rate(target, currency, ttl_hash=get_ttl_hash())
    if upstream.ok:
        rate: float = upstream.json()["rates"][target]
        out_value: float = round(rate * value, decimal_place)
        return out_value, None

    return None, upstream
