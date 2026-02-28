from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import crud, external_api, schemas
from app.database import get_db
from typing import Optional
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["Конвертация валют"])

@router.get("/convert", response_model=schemas.ConvertResponse)
async def convert_currency(
    from_currency: str = Query(..., alias='from', min_length=3, max_length=3, description="Код исходной валюты"),
    to_currency: str = Query(..., alias='to', min_length=3, max_length=3, description="Код целевой валюты"),
    amount: float = Query(..., gt=0, description="Сумма"),
    date: Optional[str] = Query(None, description="Дата в формате YYYY-MM-DD (исторический курс)"),
    db: Session = Depends(get_db)
):
    base = from_currency.upper()
    target = to_currency.upper()

    if date:
        try:
            rate = await external_api.fetch_rate(base, target, date)
            last_updated = datetime.strptime(date, "%Y-%m-%d")
        except RuntimeError as e:
            raise HTTPException(status_code=503, detail=str(e))
    else:
        cached = crud.get_cached_rate(db, base, target)
        if cached:
            rate = cached.rate
            last_updated = cached.last_updated
            logger.info(f"Использован кеш для {base}->{target}")
        else:
            try:
                rate = await external_api.fetch_rate(base, target)
                crud.save_rate(db, base, target, rate)
                last_updated = datetime.utcnow()
                logger.info(f"Получен свежий курс для {base}->{target}")
            except RuntimeError as e:
                raise HTTPException(status_code=503, detail=str(e))

    converted = amount * rate
    return schemas.ConvertResponse(
        from_currency=base,
        to_currency=target,
        amount=amount,
        converted=converted,
        rate=rate,
        last_updated=last_updated
    )

@router.get("/currencies", response_model=schemas.CurrencyListResponse)
async def list_currencies():
    try:
        currencies = await external_api.fetch_all_currencies()
        return {"currencies": currencies}
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))