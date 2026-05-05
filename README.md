# Magic-Board

## Описание

Magic-Board — backend для интерактивной карты-плеера детских сказок.
API отдаёт информацию о сказке, аудио, изображениях и маршруте движения фишки по карте.

Сейчас в проекте есть базовая сказка: **Красная Шапочка**.

## Технологии

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Docker Compose
- Pytest

## Быстрый старт

### 1. Клонировать проект

```bash
git clone https://github.com/nikros322/Magic-Board.git
cd Magic-Board
```

### 2. Создать виртуальное окружение

```bash
python -m venv .venv
```

Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Создать `.env`

```bash
cp .env.example .env
```

Для Windows можно просто скопировать файл `.env.example` и переименовать его в `.env`.

### 5. Запустить PostgreSQL

```bash
docker-compose up -d
```

### 6. Применить миграции

```bash
alembic upgrade head
```

### 7. Запустить сервер

```bash
uvicorn app.main:app --reload
```

API будет доступно здесь:

```text
http://127.0.0.1:8000
```

Swagger-документация:

```text
http://127.0.0.1:8000/docs
```

## Основные эндпоинты

```text
GET /health
GET /stories/{story_id}
GET /red-hood
```

`/red-hood` оставлен для совместимости со старым фронтендом.
Правильный универсальный эндпоинт — `/stories/{story_id}`.

## Структура проекта

```text
magic_board/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   │   ├── story.py
│   │   └── route_point.py
│   ├── schemas/
│   │   ├── story.py
│   │   └── route_point.py
│   └── routers/
│       └── stories.py
├── alembic/
│   ├── env.py
│   └── versions/
├── static/
│   ├── audio/.gitkeep
│   └── images/.gitkeep
├── tests/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Тесты

```bash
pytest
```

## Что исправлено после review

- Заполнен `README.md`.
- Добавлен `requirements.txt`.
- Добавлен `.gitignore`.
- Добавлен `.env.example`.
- Credentials убраны из кода.
- CORS вынесен в настройки.
- `main.py` очищен от бизнес-логики.
- Эндпоинты вынесены в `APIRouter`.
- Модели и схемы разделены по файлам.
- Добавлен `docker-compose.yml` для PostgreSQL.
- Добавлен Alembic.
- Дублирующий SQL заменён миграцией.
- Добавлены базовые тесты.
- Папки `static/audio` и `static/images` зафиксированы через `.gitkeep`.
