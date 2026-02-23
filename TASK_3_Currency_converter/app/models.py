from sqlalchemy import Column, Integer, String, Float, Datetime
from app.database import Base
from datetime import datetime

class CurrencyRate(Base):
    __tablename__ = "currency_rates"

    id = Column(Integer, primary_key=True, index=True)
    base_currency = Column(String(3), nullable=False, index=True) #primer RUB
    target_currency = Column(String(3), nullable=False, index=True) # naprimer tenge KZT
    rate = Column(Float, nullable=False)
    last_update = Column(Datetime, default=datetime.utcnow, onupdate=datetime.utcnow)

    #specik double (base, target)
    __table_args__=(db.UniqueConstraint("base_currency", "target_currency", name="base_target_uc"),)
