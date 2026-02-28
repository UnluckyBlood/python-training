from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional

class ConvertRequest(BaseModel):
    from_currency: str = Field(..., alias="from", min_length=3, max_length=3, description="Код исходной валюты (например, RUB)")
    to_currency: str = Field(..., alias="to", min_length=3, max_length=3, description="Код целевой валюты (например, KZT)")
    amount: float = Field(..., gt=0, description="Сумма для конвертации")
    date: Optional[str] = Field(None, description="Дата в формате YYYY-MM-DD")

    @field_validator("from_currency", "to_currency")
    def validate_currency_code(cls, v):
        if not v.isalpha() or len(v) != 3:
            raise ValueError("Код валюты должен состоять из трёх букв")
        return v.upper()

    @field_validator("date")
    def validate_date(cls, v):
        if v:
            try:
                datetime.strptime(v, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Неверный формат даты, используйте YYYY-MM-DD")
        return v

class ConvertResponse(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
    converted: float
    rate: float
    last_updated: datetime

class CurrencyListResponse(BaseModel):
    currencies: list[str]