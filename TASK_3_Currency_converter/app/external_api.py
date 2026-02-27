import httpx
import xml.etree.ElementTree as ET
from typing import Optional
from datetime import datetime

# URL для получения курсов ЦБ РФ
CBR_URL = "http://www.cbr.ru/scripts/XML_daily.asp"

async def fetch_rate(base: str, target: str, date: Optional[str] = None) -> float:
    """
    Получает курс от base к target через API ЦБ РФ.
    Поддерживает только base=RUB, для других валют вернёт ошибку.
    """
    if base != "RUB":
        raise RuntimeError(f"API ЦБ РФ поддерживает только базовую валюту RUB (запрошена {base})")

    # Формируем URL с датой, если указана
    url = CBR_URL
    params = {}
    if date:
        # ЦБ РФ принимает дату в формате dd/MM/yyyy
        try:
            dt = datetime.strptime(date, "%Y-%m-%d")
            date_str = dt.strftime("%d/%m/%Y")
            params["date_req"] = date_str
        except ValueError:
            raise RuntimeError("Неверный формат даты, используйте YYYY-MM-DD")

    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, params=params, timeout=10.0)
            resp.raise_for_status()

            # Парсим XML
            root = ET.fromstring(resp.text)

            # Ищем валюту по коду (KZT)
            target_rate = None
            for valute in root.findall("Valute"):
                char_code = valute.find("CharCode").text
                if char_code == target:
                    # Номинал (например, 100 тенге)
                    nominal = int(valute.find("Nominal").text)
                    # Курс за номинал (в рублях)
                    value = float(valute.find("Value").text.replace(",", "."))
                    # Курс за 1 единицу target валюты
                    target_rate = value / nominal
                    break

            if target_rate is None:
                raise RuntimeError(f"Валюта {target} не найдена в данных ЦБ РФ")

            # Так как base = RUB, то курс RUB → target = 1 / target_rate
            # Но нам нужен курс сколько target за 1 RUB, то есть 1 / (RUB за 1 target)
            # Например, если 1 KZT = 0.18 RUB, то 1 RUB = 1 / 0.18 ≈ 5.55 KZT
            rate = 1.0 / target_rate
            return rate

        except (httpx.HTTPStatusError, httpx.RequestError, ET.ParseError) as e:
            raise RuntimeError(f"Не удалось получить курс: {e}")

async def fetch_all_currencies() -> list[str]:
    """
    Получает список доступных валют из API ЦБ РФ.
    """
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(CBR_URL, timeout=10.0)
            resp.raise_for_status()

            root = ET.fromstring(resp.text)
            currencies = []
            for valute in root.findall("Valute"):
                char_code = valute.find("CharCode").text
                currencies.append(char_code)

            # Добавляем RUB, так как это базовая валюта
            currencies.append("RUB")
            return sorted(currencies)

        except Exception as e:
            raise RuntimeError(f"Не удалось получить список валют: {e}")