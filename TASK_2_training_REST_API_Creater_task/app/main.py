from fastapi import FastAPI, HTTPException, Query, status, Depends
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
from typing import Optional, List
# Создание БД
DataBase_URL = "sqlite:///./tasks.db"
Engine = create_engine(DataBase_URL, connect_args = {"check_same_thread": False})
Session_Local = sessionmaker(autocommit = False, autoflush = False, bind = Engine)
Base = declarative_base()
# Создаём класс таблиц
class TaskModel(Base):
    __tablename__ = "tasks" # обозначение __****__ используется чтобы выделить так важный атрибут на подобие __init__ называется дандер(double underscore)
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean,default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=Engine)

# Управление таблицой
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100) # Без Optional и с ... значит что объязательное поле, в данном случае мы можем только дать название, а остальное будет по дефолту или пустое поэтому так
    description: Optional[str] = Field(None, max_length=500)
    completed: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    completed: Optional[bool] = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime

# Автоматически превращаем в словарь и передаём
    class Config:
        from_attributes = True

# инициализация FastAPI
app = FastAPI(title="Task API", version="1.0.0")
# открыта бд пока мы её выдаём, потом закрывает для ресурсмэнэджмента
def get_db():
    db = Session_Local()
    try:
        yield db #приостанавливает выполнение сохраняя состояние функции и возвращает промежуточный результат, следующие обращение будет не с нулевой точки отсчёта
    finally:
        db.close()

# создание пост запросов
@app.post("/tasks", response_model=TaskOut, status_code=status.HTTP_201_CREATED) #если успешно то вернётся такой статус status.HTTP_201_CREATED, а респонс заставляет Fast_api автоматически ответ делать по схеме
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = TaskModel(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Получение списка задач
@app.get("/tasks", response_model=List[TaskOut])
def list_tasks(completed: Optional[bool] = Query(None), db: Session = Depends(get_db)): #если состояние не передано то по дефолту будет равно None
    query = db.query(TaskModel)
    # Если есть статус о выполнении то мы конструируем объект, это не прямое сравнение, ну или если нету данных, то прост все выдаём сразу
    if completed is not None:
        query = query.filter(TaskModel.completed == completed)
    return query.all()

# Получение одной задачи
@app.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found") # raise, когда программа натыкается на него то реагирует как ошибка и ищет подходящий except , если не найдёт то аварийно завершится программа, если всё норм и задача есть, то возвращаем её
    return task

# Полное обновление
@app.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, task_update: TaskCreate, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task_update.dict().items():
        setattr(task, key, value) # выставляем всем новые значения
    db.commit()
    db.refresh(task)
    return task
# Частичное обновление тасков
@app.patch("/tasks/{task_id}", response_model=TaskOut)
def patch_task(task_id: int, task_patch: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    update_data = task_patch.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

# Удаление задачи
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return

#для запуска нужно будет установить библиотеки данной командой pip install fastapi uvicorn sqlalchemy pydantic
# uvicorn нужен для сервака, его запуск будет командой uvicorn app.main:app --reload        параметр reload автоматически перезагружает приложение при изменинях, app. (название папки если запускаете из корня)