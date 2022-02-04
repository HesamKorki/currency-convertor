from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_convert_success():
    params = {
        "currency": "USD",
        "value": 1,
    }
    response = client.get("/convert/EUR", params=params)
    assert response.status_code == 200
    assert response.json()["value"] < 1
    assert response.json()["currency"] == "EUR"


def test_convert_fail_negative_vale():
    params = {
        "currency": "EUR",
        "value": -1,
    }
    response = client.get("/convert/USD", params=params)
    detail = response.json()["detail"][0]
    assert response.status_code == 422
    assert detail["loc"] == ["query", "value"]
    assert "value is greater than or equal to 0" in detail["msg"]


def test_convert_fail_invalid_currency():
    params = {
        "currency": "IRR",
        "value": 10.99,
    }
    response = client.get("/convert/EUR", params=params)
    detail = response.json()["detail"][0]
    assert response.status_code == 422
    assert detail["loc"] == ["query", "currency"]
    assert "not a valid enumeration member" in detail["msg"]


def test_convert_fail_invalid_target():
    params = {
        "currency": "EUR",
        "value": 10.99,
    }
    response = client.get("/convert/IRR", params=params)
    detail = response.json()["detail"][0]
    assert response.status_code == 422
    assert detail["loc"] == ["path", "target"]
    assert "not a valid enumeration member" in detail["msg"]


def test_convert_fail_invalid_value():
    params = {
        "currency": "USD",
        "value": "abc",
    }
    response = client.get("/convert/EUR", params=params)
    detail = response.json()["detail"][0]
    assert response.status_code == 422
    assert detail["loc"] == ["query", "value"]
    assert "value is not a valid float" in detail["msg"]


def test_convert_fail_null_value():
    params = {
        "currency": "USD",
    }
    response = client.get("/convert/EUR", params=params)
    detail = response.json()["detail"][0]
    assert response.status_code == 422
    assert detail["loc"] == ["query", "value"]
    assert "field required" in detail["msg"]


def test_convert_fail_null_currency():
    params = {
        "value": 10.99,
    }
    response = client.get("/convert/EUR", params=params)
    detail = response.json()["detail"][0]
    assert response.status_code == 422
    assert detail["loc"] == ["query", "currency"]
    assert "field required" in detail["msg"]


def test_convert_fail_null_target():
    params = {
        "currency": "USD",
        "value": 10.99,
    }
    response = client.get("/convert/", params=params)
    detail = response.json()["detail"][0]
    assert response.status_code == 404


def test_convert_fail_invalid_decimal_place():
    params = {
        "currency": "USD",
        "value": 10.99,
        "decimal_place": "abc",
    }
    response = client.get("/convert/EUR", params=params)
    detail = response.json()["detail"][0]
    assert response.status_code == 422
    assert detail["loc"] == ["query", "decimal_place"]
    assert "not a valid integer" in detail["msg"]
