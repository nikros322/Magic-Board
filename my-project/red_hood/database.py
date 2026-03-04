from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

#  Ссылка для подключения.
DATABASE_URL = "postgresql://postgres:@localhost:5432/red_hood_db"

# Создаем движок подключения
engine = create_engine(DATABASE_URL)

# Создаем фабрику сессий (наш "телефон" для звонков в базу)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()

# --- ОПИСАНИЕ ТАБЛИЦ (МОДЕЛИ) ---
class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    audio_url = Column(String(500))

    # Связь: одна сказка может иметь много точек маршрута
    points = relationship("RoutePoint", back_populates="story")

class RoutePoint(Base):
    __tablename__ = "route_points"

    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey("stories.id"))
    t = Column(Integer, nullable=False)  # Время в мс
    x = Column(Integer, nullable=False)  # Координата X
    y = Column(Integer, nullable=False)  # Координата Y
    event = Column(String(255))

    # Обратная связь к сказке
    story = relationship("Story", back_populates="points")
