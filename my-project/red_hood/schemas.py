from pydantic import BaseModel
from typing import List, Optional

# Схема для одной точки маршрута
class RoutePointRead(BaseModel):
    t: int
    x: int
    y: int
    event: Optional[str] = None

    class Config:
        from_attributes = True # Позволяет Pydantic читать данные из SQLAlchemy

# Схема для всей сказки (то, что получит фронт)
class StoryRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    audio_url: str
    points: List[RoutePointRead] # Список точек внутри сказки

    class Config:
        from_attributes = True
