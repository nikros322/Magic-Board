from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database import SessionLocal, Story, RoutePoint

app = FastAPI(
    title="Сказка Красная Шапочка",
    description="API с данными из PostgreSQL",
    version="1.1.0"
)

# Функция для работы с сессией базы
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Подключаем папку со звуком
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/red-hood")
def get_story(db: Session = Depends(get_db)):
# Вытаскиваем сказку и все её точки из базы
    story_db = db.query(Story).filter(Story.id == 1).first()
    points_db = db.query(RoutePoint).filter(RoutePoint.story_id == 1).order_by(RoutePoint.t).all()

 # Формируем ответ для "доски"
    return {
        "title": story_db.title,
        "description": story_db.description,
        "audio_url": story_db.audio_url,
        "route": [
            {
                "t": p.t,
                "x": p.x,
                "y": p.y,
                "event": p.event
            } for p in points_db
        ]
    }
