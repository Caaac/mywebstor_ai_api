from fastapi import APIRouter
from .audio import router as audio_router

api_router = APIRouter()
api_router.include_router(audio_router, prefix="/audio", tags=["audio"])