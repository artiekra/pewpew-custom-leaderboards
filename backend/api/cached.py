"""Run FastAPI for backend (methods, related to calculations
and caching them)"""

import sqlite3

from loguru import logger
from fastapi import APIRouter

logger = logger.opt(colors=True)


def get_router(con: sqlite3.Connection) -> APIRouter:
    """Create FastAPI router, given database connection"""
    logger.trace("Creating FastAPI router for cached methods")

    router = APIRouter()

    @router.get("/get_player/", tags=["cached"])
    def get_player():
        """Get cached data on player for leaderboards"""
        return {"error": "Hi!"}

    return router
