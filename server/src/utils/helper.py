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
    upstream = api.get_exchange_rate(target, currency, ttl_hash=get_ttl_hash())
    if upstream.ok:
        rate: float = upstream.json()["rates"][target]
        out_value: float = round(rate * value, decimal_place)
        return out_value, None

    return None, upstream
