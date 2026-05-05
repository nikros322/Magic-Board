from pydantic import BaseModel, ConfigDict


class RoutePointRead(BaseModel):
    t: int
    x: int
    y: int
    event: str | None = None

    model_config = ConfigDict(from_attributes=True)
