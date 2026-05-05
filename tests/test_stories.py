from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app
from app.models.route_point import RoutePoint
from app.models.story import Story

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def seed_story():
    db = TestingSessionLocal()
    db.query(RoutePoint).delete()
    db.query(Story).delete()

    story = Story(
        id=1,
        title="Красная Шапочка",
        author="Шарль Перро",
        description="Интерактивная сказка с маршрутом по карте",
        audio_url="/static/audio/redhood.m4a",
        cover_url="/static/images/redhood-cover.png",
        map_url="/static/images/redhood-map.png",
    )
    story.route_points = [
        RoutePoint(t=0, x=10, y=20, event="Старт"),
        RoutePoint(t=1000, x=30, y=40, event="Путь через лес"),
    ]
    db.add(story)
    db.commit()
    db.close()


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_story_by_id():
    seed_story()

    response = client.get("/stories/1")

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Красная Шапочка"
    assert len(data["route"]) == 2


def test_get_unknown_story_returns_404():
    response = client.get("/stories/999")

    assert response.status_code == 404
