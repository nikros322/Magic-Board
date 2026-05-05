"""create stories and route_points

Revision ID: 20250101_0001
Revises:
Create Date: 2025-01-01
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "20250101_0001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "stories",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("author", sa.String(length=255), nullable=False, server_default="Шарль Перро"),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("audio_url", sa.String(length=500), nullable=True),
        sa.Column("cover_url", sa.String(length=500), nullable=True),
        sa.Column("map_url", sa.String(length=500), nullable=True),
    )

    op.create_table(
        "route_points",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column("story_id", sa.Integer(), sa.ForeignKey("stories.id", ondelete="CASCADE"), nullable=False),
        sa.Column("t", sa.Integer(), nullable=False),
        sa.Column("x", sa.Integer(), nullable=False),
        sa.Column("y", sa.Integer(), nullable=False),
        sa.Column("event", sa.String(length=255), nullable=True),
    )
    op.create_index("idx_route_points_story_t", "route_points", ["story_id", "t"])


def downgrade() -> None:
    op.drop_index("idx_route_points_story_t", table_name="route_points")
    op.drop_table("route_points")
    op.drop_table("stories")
