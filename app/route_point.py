from pydantic import BaseModel


class RoutePointRead(BaseModel):
    id: int
    story_id: int
    t: int
    x: int
    y: int
    description: str

    class Config:
        from_attributes = True