from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.routers import stories

app = FastAPI(
    title="Magic Board API",
    description="Backend для интерактивной карты-плеера детских сказок",
    version="1.3.0",
    debug=settings.debug,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(stories.router)


@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok"}


@app.get("/red-hood", response_model=stories.StoryRead, tags=["stories"])
def get_red_hood_story(db=Depends(stories.get_db)):
    # Совместимость со старым фронтендом: раньше была только сказка с id=1.
    return stories.get_story(story_id=1, db=db)
