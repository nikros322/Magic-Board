from sqlalchemy import ForeignKey, Index, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class RoutePoint(Base):
    __tablename__ = "route_points"
    __table_args__ = (Index("idx_route_points_story_t", "story_id", "t"),)

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    story_id: Mapped[int] = mapped_column(ForeignKey("stories.id", ondelete="CASCADE"), nullable=False)
    t: Mapped[int] = mapped_column(Integer, nullable=False)
    x: Mapped[int] = mapped_column(Integer, nullable=False)
    y: Mapped[int] = mapped_column(Integer, nullable=False)
    event: Mapped[str | None] = mapped_column(String(255), nullable=True)

    story = relationship("Story", back_populates="route_points")
