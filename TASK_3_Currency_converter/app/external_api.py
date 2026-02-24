import httpx
from app.config import settings
from datetime import datetime
from typing import Optional

async def fetch_rate(base: str, target: str, date: Optional[str] = None) -> float:
    """
    Получает курс от base к target с внешнего API.
    Если date указана, запрашивает исторический курс на эту дату.
    Возвращает курс (сколько target за 1 base).
    """
    # Frankfurter API: https://api.frankfurter.app/latest?from=USD&to=EUR
    # или для исторической даты: https://api.frankfurter.app/2026-02-20?from=USD&to=EUR
    url = settings.external_api_url
    if date:
        url += f"/{date}"
    else:
        url += "/latest"

    params = {
        "from": base,
        "to": target
    }

    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, params=params, timeout=10.0)
            resp.raise_for_status()
            data = resp.json()
            # Frankfurter возвращает rates как словарь {target: rate}
            rate = data["rates"][target]
            return rate
        except (httpx.HTTPStatusError, httpx.RequestError, KeyError) as e:
            # Пробрасываем исключение, чтобы обработать выше
            raise RuntimeError(f"Не удалось получить курс: {e}")

async def fetch_all_currencies() -> list[str]:
    """
    Получает список доступных валют с внешнего API.
    """
    url = f"{settings.external_api_url}/currencies"
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, timeout=10.0)
            resp.raise_for_status()
            data = resp.json()  # возвращает словарь вида {"USD": "US Dollar", ...}
            return list(data.keys())
        except Exception as e:
            raise RuntimeError(f"Не удалось получить список валют: {e}")