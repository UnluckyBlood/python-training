import pytest
from httpx import ASGITransport, AsyncClient

@pytest.mark.asyncio
async def test_convert_with_mock(async_client, httpx_mock):
    httpx_mock.add_response(
        url="https://api.frankfurter.app/latest?from=RUB&to=KZT",
        method="GET",
        json={
            "amount": 1.0,
            "base": "RUB",
            "date": "2026-02-23",
            "rates": {"KZT": 5.12}
        }
    )
    response = await async_client.get("/api/convert?from=RUB&to=KZT&amount=100")
    assert response.status_code == 200
    data = response.json()
    assert data["converted"] == 512.0

@pytest.mark.asyncio
async def test_currencies(async_client, httpx_mock):
    httpx_mock.add_response(
        url="https://api.frankfurter.app/currencies",
        method="GET",
        json={"RUB": "Russian Ruble", "KZT": "Kazakhstani Tenge", "USD": "US Dollar"}
    )
    response = await async_client.get("/api/currencies")
    assert response.status_code == 200
    data = response.json()
    assert "currencies" in data
    assert "RUB" in data["currencies"]