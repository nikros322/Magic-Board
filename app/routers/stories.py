from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, selectinload

from app.database import get_db
from app.models.story import Story
from app.schemas.story import StoryRead

router = APIRouter(prefix="/stories", tags=["stories"])


@router.get("/{story_id}", response_model=StoryRead)
def get_story(story_id: int, db: Session = Depends(get_db)):
    story = (
        db.query(Story)
        .options(selectinload(Story.route_points))
        .filter(Story.id == story_id)
        .first()
    )

    if story is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Сказка не найдена",
        )

    return story
