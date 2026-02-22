from fastapi import FastAPI, HTTPException, Query, status, Depends
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
from typing import Optional, List
# Создание БД
DataBase_URL = "sqlite:///./tasks.db"
Engine = create_engine (DataBase_URL, connect_args = {"check_same_thread": False})
Session_Local = sessionmaker (autocomit = False, autoflush = False, bind = Engine)
Base = declarative_base ()
# Создаём класс таблиц
class TaskModel (Base):
    __tablename__ = "tasks" # обозначение __****__ используется чтобы выделить так важный атрибут на подобие __init__ называется дандер (double underscore)
    id = Column (Integer, primary_key=True, index=True)
    title = Column (String, nullable=False)
    description = Column (Boolean, nullable=True)
    completed = Column (Boolean,default=False)
    created_at = Column (DateTime, default=datetime.utcnow)

Base.metadata.create_all (bind=Engine)

# Управление таблицой
class TaskCreate (BaseModel):
    title: str = Field (..., min_length=1, max_length=100) # Без Optional и с ... значит что объязательное поле, в данном случае мы можем только дать название, а остальное будет по дефолту или пустое поэтому так
    description: Optional[str] = Field (None, max_length=500)
    completed: Optional[bool] = False

class TaskUpdate (BaseModel):
    title: Optional[str] = Field (None, min_length=1, max_length=100)
    description: Optional[str] = Field (None, max_length=500)
    completed: Optional[bool] = None

class TaskOut (BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime

# Автоматически превращаем в словарь и передаём
    class Config:
        orm_mode = True

