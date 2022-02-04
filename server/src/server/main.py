from typing import Optional

from fastapi import FastAPI, HTTPException, Query
import uvicorn

from core.models import Currency, Response
from core import config
from utils import helper

app = FastAPI()


@app.get("/convert/{target}", response_model=Response)
async def convert(
    target: Currency,
    currency: Currency,
    value: float = Query(..., ge=0, example=10.99),
    decimal_place: Optional[int] = 4,
):
    out_value, error = helper.compute_exchange_value(
        target, currency, value, decimal_place
    )
    if error:
        raise HTTPException(
            status_code=error.status_code, detail=error.json()["detail"]
        )
    return Response(value=out_value, currency=target)


if __name__ == "__main__":
    uvicorn.run("main:app", host=config.HOST, port=config.PORT)
