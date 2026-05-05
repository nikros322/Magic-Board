from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Story(Base):
    __tablename__ = "stories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    author: Mapped[str] = mapped_column(String(255), default="Шарль Перро", nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    audio_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    cover_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    map_url: Mapped[str | None] = mapped_column(String(500), nullable=True)

    route_points = relationship(
        "RoutePoint",
        back_populates="story",
        cascade="all, delete-orphan",
        order_by="RoutePoint.t",
    )
