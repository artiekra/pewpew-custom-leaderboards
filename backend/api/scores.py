"""Run FastAPI for backend (methods, related to updating scores)"""

import sqlite3

from loguru import logger
from fastapi import APIRouter

from .database.interact import *  # [TODO: fix wildcard import?..]

logger = logger.opt(colors=True)


def get_router(con: sqlite3.Connection) -> APIRouter:
    """Create FastAPI router, given database connection"""
    logger.trace("Creating FastAPI router for score methods")

    router = APIRouter()

    # [TODO: add time period configuration]
    @router.get("/get_scores/", tags=["scores"])
    def get_scores():
        """Get all available records for a particular time period"""
        logger.log("API", "Getting all available scores..")

        result = db_get_all(con)

        return result

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
