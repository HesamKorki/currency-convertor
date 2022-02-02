from fastapi import FastAPI

from models import Currency
from utils import api

app = FastAPI()

@app.get('/convert/{target}')
async def convert(target: Currency, currency: Currency, value: float):
    upstream = api.get_exchange_rate(target, currency, value)
    if upstream.ok:
        out_value = upstream.json()['rates'][target]
        return {
            'value': out_value,
            'currency': target
        }
    return upstream.text()
