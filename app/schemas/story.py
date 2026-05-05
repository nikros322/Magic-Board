from pydantic import BaseModel, ConfigDict, Field

from app.schemas.route_point import RoutePointRead


class StoryRead(BaseModel):
    id: int
    title: str
    author: str
    description: str | None = None
    audio_url: str | None = None
    cover_url: str | None = None
    map_url: str | None = None
    route: list[RoutePointRead] = Field(validation_alias="route_points")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
