from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import convert
from app.database import engine, Base
import logging

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Настройка логирования
logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Currency Converter API", version="1.0.0")

# Подключаем роутер API
app.include_router(convert.router)

# Подключаем статические файлы (папка static будет доступна по корневому URL)
app.mount("/static", StaticFiles(directory="static"), name="static")

# (Опционально) редирект с корня на статическую страницу
from fastapi.responses import RedirectResponse

@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")