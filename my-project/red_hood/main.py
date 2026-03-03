from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Сказка Красная Шапочка",
    description="API для управления маршрутом и озвучкой интерактивной сказки",
    version="1.0.0"
)

STORY = {
    "title": "Красная Шапочка",
    "description": "Интерактивная история с перемещением по карте леса",
    "audio_url": "http://127.0.0.1:8000/static/audio/red_hood.m4a",
    "route": [
    {"t": 0, "x": 10, "y": 10, "event": "Начало: Описание Красной Шапочки"},
    {"t": 72000, "x": 40, "y": 50, "event": "Дом: Мама дает корзинку (1:12)"},
    {"t": 126000, "x": 100, "y": 120, "event": "Лес: Встреча с Волком (2:06)"},
    {"t": 180000, "x": 180, "y": 80, "event": "Поляна: Сбор цветов (3:00)"},
    {"t": 240000, "x": 250, "y": 200, "event": "Домик бабушки: Прибытие (4:00)"},
    {"t": 310000, "x": 280, "y": 280, "event": 'Кульминация: "Почему такие зубы?" (5:10)'},
    {"t": 348000, "x": 300, "y": 300, "event": "Финал: Спасение (5:48)"}
    ]
}

# Подключаем раздачу статических файлов (аудио)
#directory="static" означает, что файлы лежат в папке static в корне проекта
app.mount("/static", StaticFiles(directory="static"), name="static")

# Эндпоинт для получения данных сказки
@app.get("/red-hood")
def get_story():
    return STORY
