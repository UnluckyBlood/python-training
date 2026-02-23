from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread":False} #only for sqlite
)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()
#gen db zavis FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()