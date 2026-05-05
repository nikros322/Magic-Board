from typing import List, Optional

from pydantic import BaseModel

from app.schemas.route_point import RoutePointRead


class StoryRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    audio_url: str
    author: Optional[str] = None
    cover_image_url: Optional[str] = None
    map_image_url: Optional[str] = None

    route_points: List[RoutePointRead] = []

    class Config:
        from_attributes = True