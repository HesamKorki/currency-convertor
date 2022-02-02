import requests

import config
from models import Currency


def get_exchange_rate(target: Currency,
                      currency: Currency,
                      amount: float,
                      places: int = 2) -> requests.models.Response:
    """calls the exchangerate.host API with query parameters and fetches the desired rates.

    Args:
        target (Currency): [The desired target currency]
        currency (Currency): [The base currency in which the value is defined]
        amount (float): [the amount of base currency to exchange]
        places (int, optional): [Round numbers to decimal place]. Defaults to 2.

    Returns:
        [Response]: [The object of response]
    """

    url = config.BASE_URL
    payload = {
        'base': currency,
        'symbols': target,
        'amount': amount,
        'places': places,
    }
    response = requests.get(url, params=payload)

    return response
