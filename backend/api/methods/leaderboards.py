"""Run FastAPI for backend (methods, related to leaderboars themselves)"""

from typing import Optional

from loguru import logger
from fastapi import APIRouter
from pydantic import BaseModel

import database.interact as dbi

logger = logger.opt(colors=True)


def get_router(engine) -> APIRouter:
    """Create FastAPI router, given database connection"""
    logger.trace("Creating FastAPI router for score methods")

    router = APIRouter()

    @router.get("/get_leaderboard_data/", tags=["leaderboards"])
    def get_leaderboard_data(
        era: Optional[int] = None,
        mode: Optional[int] = None
    ):
        """Get leaderboard data (variables for each player-level pair)"""
        results = dbi.get_leaderboard_vars(engine, [era, mode])

        return {"response": results, "metadata": None}


    return router
