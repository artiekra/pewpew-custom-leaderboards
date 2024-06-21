"""Run FastAPI for backend (methods, related to updating scores)"""

from typing import Optional

from loguru import logger
from fastapi import APIRouter
from pydantic import BaseModel

import database.interact as dbi

logger = logger.opt(colors=True)


def get_router(session) -> APIRouter:
    """Create FastAPI router, given database connection"""
    logger.trace("Creating FastAPI router for score methods")

    router = APIRouter()

    @router.get("/get_scores/", tags=["scores"])
    def get_scores(
        page: int,
        limit: int,
        timestamp_start: Optional[int] = None,
        timestamp_end: Optional[int] = None,
        era: Optional[int] = None,
    ):
        """Get all available records for a particular time period"""
        results, metadata = dbi.get_scores(session, page, limit, [timestamp_start,
            timestamp_end, era])

        return {"response": results, "metadata": metadata}


    @router.get("/get_latest_player_scores/", tags=["scores"])
    def get_player_scores(
        player: str,
        era: int = 2,
        mode: Optional[int] = None
    ):
        """Get all latest scores for each level (given the player)"""
        results = dbi.get_player_latest(session, player, [era, mode])

        return {"response": results, "metadata": None}


    return router
