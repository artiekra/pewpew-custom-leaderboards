"""Run FastAPI for backend (methods, related to calculations
and caching them)"""

from loguru import logger
from fastapi import APIRouter

logger = logger.opt(colors=True)

router = APIRouter()


@router.get("/get_player/", tags=["cached"])
def get_player():
    """Get cached data on player for leaderboards"""
    return {"error": "Hi!"}
