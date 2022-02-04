from functools import lru_cache

import requests

import core.config as config
from core.models import Currency


@lru_cache(maxsize=9)
def get_exchange_rate(
    target: Currency, currency: Currency, ttl_hash=None
) -> requests.models.Response:
    """calls the exchangerate.host API with query parameters and fetches the desired rates.

    Args:
        target (Currency): [The desired target currency]
        currency (Currency): [The base currency in which the value is defined]

    Returns:
        [Response]: [The object of http response]
    """
    del ttl_hash
    url = config.BASE_URL
    payload = {
        "base": currency,
        "symbols": target,
    }
    response = requests.get(url, params=payload)

    return response
