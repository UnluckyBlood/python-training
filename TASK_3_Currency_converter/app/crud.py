from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import datetime, timedelta
from app.models import CurrencyRate
from app.config import settings

def get_cached_rate(db: Session, base: str, target: str) -> CurrencyRate | None:
    """Возвращает запись курса, если она есть и не устарела."""
    # Считаем устаревшей, если прошло больше cache_ttl_hours часов
    cutoff = datetime.utcnow() - timedelta(hours=settings.cache_ttl_hours)
    return db.query(CurrencyRate).filter(
        and_(
            CurrencyRate.base_currency == base,
            CurrencyRate.target_currency == target,
            CurrencyRate.last_updated >= cutoff
        )
    ).first()

def save_rate(db: Session, base: str, target: str, rate: float):
    """Сохраняет или обновляет курс в БД."""
    # Пытаемся найти существующую запись
    record = db.query(CurrencyRate).filter(
        and_(
            CurrencyRate.base_currency == base,
            CurrencyRate.target_currency == target
        )
    ).first()
    if record:
        record.rate = rate
        record.last_updated = datetime.utcnow()
    else:
        record = CurrencyRate(
            base_currency=base,
            target_currency=target,
            rate=rate,
            last_updated=datetime.utcnow()
        )
        db.add(record)
    db.commit()
    db.refresh(record)
    return record