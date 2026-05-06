from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.routers.stories import router as stories_router

app = FastAPI(
    title="Magic Board API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(stories_router)


@app.get("/")
def root():
    return {
        "message": "Magic Board API is running",
        "docs": "/docs",
    }
@app.get("/health")
def health_check():
    return {"status": "ok"}