"""Run FastAPI for backend (methods, related to updating scores)"""

import sqlite3
from typing import Optional

from loguru import logger
from fastapi import APIRouter
from pydantic import BaseModel

from .database.interact import *  # [TODO: fix wildcard import?..]

logger = logger.opt(colors=True)


def get_router(con: sqlite3.Connection) -> APIRouter:
    """Create FastAPI router, given database connection"""
    logger.trace("Creating FastAPI router for score methods")

    router = APIRouter()

    # [TODO: refactor args? make it POST request?]
    @router.get("/get_scores/", tags=["scores"])
    def get_scores(
        page: int,
        limit: int,
        timestamp_start: Optional[int] = None,
        timestamp_end: Optional[int] = None,
        era: Optional[int] = None,
        player: Optional[str] = None,
        level: Optional[str] = None
    ):
        """Get all available records for a particular time period"""
        logger.log("API", "Getting all available scores..")

        headers = ["id", "timestamp", "era", "username1", "username2",
                   "level", "score", "country", "platform", "mode"]

        result, metadata = db_get_all(con, page, limit, [timestamp_start,
            timestamp_end, era, player, level])
        result_dict = [zip(headers, x) for x in result]

        return {"result": result_dict, "metadata": metadata}

    # @router.get("/get_player_scores/", tags=["scores"])
    # def get_player_scores():
    #     """Get all available records for a particular player"""
    #     return {"error": "Hi!"}
    #
    # @router.get("/get_level_scores/", tags=["scores"])
    # def get_level_scores():
    #     """Get all available records for a particular level"""
    #     return {"error": "Hi!"}
    #
    # @router.get("/database_check/", tags=["scores"])
    # def database_check():
    #     """Return some basic stats and misc info from database"""
    #     return {"error": "Hi!"}

    return router
