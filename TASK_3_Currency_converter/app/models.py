from sqlalchemy import Column, Integer, String, Float, DateTime, UniqueConstraint
from app.database import Base
from datetime import datetime

class CurrencyRate(Base):
    __tablename__ = "currency_rates"

    id = Column(Integer, primary_key=True, index=True)
    base_currency = Column(String(3), nullable=False, index=True)
    target_currency = Column(String(3), nullable=False, index=True)
    rate = Column(Float, nullable=False)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)   # было last_update

    __table_args__ = (UniqueConstraint('base_currency', 'target_currency', name='base_target_uc'),)