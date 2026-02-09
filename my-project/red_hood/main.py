from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

STORY = {
    "title": "Красная Шапочка",
    "description": "Интерактивная история с перемещением по карте леса",
    "audio_url": "http://127.0.0.1:8000/static/audio/red_hood.mp3",
    "route": [
        {"t": 0, "x": 10, "y": 10, "event": "Начало: Дом мамы, получение корзинки"},
        {"t": 5000, "x": 20, "y": 15, "event": "Выход на тропинку"},
        {"t": 15000, "x": 35, "y": 40, "event": "Вход в густой лес"},
        {"t": 25000, "x": 50, "y": 50, "event": "Встреча с Волком у старого дуба"},
        {"t": 40000, "x": 60, "y": 70, "event": "Разговор о короткой и длинной дороге"},
        {"t": 55000, "x": 80, "y": 60, "event": "Сбор цветов на полянке"},
        {"t": 75000, "x": 90, "y": 85, "event": "Подход к калитке дома бабушки"},
        {"t": 90000, "x": 95, "y": 95, "event": "Финал: Дом бабушки"}
    ]
}

# Подключаем раздачу статических файлов (аудио)
#directory="static" означает, что файлы лежат в папке static в корне проекта
app.mount("/static", StaticFiles(directory="static"), name="static")

# Эндпоинт для получения данных сказки
@app.get("/red-hood")
def get_story():
    return STORY
