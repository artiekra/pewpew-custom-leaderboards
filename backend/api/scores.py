"""Run FastAPI for backend (methods, related to updating scores)"""

import sqlite3
from typing import Optional

from loguru import logger
from fastapi import APIRouter
from pydantic import BaseModel

from database.interact import *  # [TODO: fix wildcard import?..]

logger = logger.opt(colors=True)


def get_router(con: sqlite3.Connection) -> APIRouter:
    """Create FastAPI router, given database connection"""
    logger.trace("Creating FastAPI router for score methods")

    router = APIRouter()

    # [TODO: make filters work]
    @router.get("/get_scores/", tags=["scores"])
    def get_scores(
        page: int,
        limit: int,
        timestamp_start: Optional[int] = None,
        timestamp_end: Optional[int] = None,
        era: Optional[int] = 2,
    ):
        """Get all available records for a particular time period"""
        logger.log("API", "Getting all available scores..")

        headers = ["id", "timestamp", "era", "username1", "username2",
                   "level", "score", "country", "platform", "mode"]

        result, metadata = db_get_all(con, page, limit, [timestamp_start,
            timestamp_end, era])
        result_dict = [zip(headers, x) for x in result]

        return {"result": result_dict, "metadata": metadata}


    # [TODO: make filters work]
    # [TODO: do i need to make era Optional[int]? or just int..]
    @router.get("/get_latest_player_scores/", tags=["scores"])
    def get_player_scores(
        player: str,
        era: int = 2,
        mode: Optional[int] = None
    ):
        """Get all latest scores for each level (given the player)"""
        logger.log("API", "Getting all latest scores.. (player=<m>{}</>)",
                   player)

        headers = ["id", "timestamp", "era", "username1", "username2",
                   "level", "score", "country", "platform", "mode"]

        result = db_get_player_latest(con, player, [era, mode])
        result_dict = [zip(headers, x) for x in result]

        return {"result": result_dict, "metadata": None}


    return router
