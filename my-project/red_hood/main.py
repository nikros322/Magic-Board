from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from database import SessionLocal, Story
import schemas

app = FastAPI(
    title="Сказка Красная Шапочка API",
    description="Финальная версия 2-го спринта с БД и CORS",
    version="1.2.0"
)

# НАСТРОЙКА CORS
origins = [
    "http://localhost:3000",    # React
    "http://localhost:5173",    # Vite/Frontend
    "http://127.0.0.1:5173",
    "*"                         # Разрешить всем
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Разрешаем все методы (GET, POST и т.д.)
    allow_headers=["*"],
)

# ИНЪЕКЦИЯ ЗАВИСИМОСТИ
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.mount("/static", StaticFiles(directory="static"), name="static")

# РЕФАКТОРИНГ ЭНДПОИНТА
@app.get("/red-hood", response_model=schemas.StoryRead)
def get_story(db: Session = Depends(get_db)):
    # Запрос в реальную базу через SQLAlchemy
    story_db = db.query(Story).filter(Story.id == 1).first()

    if not story_db:
        raise HTTPException(status_code=404, detail="Сказка не найдена")

    # Мапим точки в поле route для фронта
    story_db.route = story_db.points
    return story_db
