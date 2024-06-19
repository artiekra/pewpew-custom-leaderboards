"""Run FastAPI for backend (methods, related to getting score data)"""

import sqlite3
from typing import Union, Optional

from loguru import logger
from fastapi import APIRouter
from pydantic import BaseModel

from database.interact import *  # [TODO: fix wildcard import?..]

logger = logger.opt(colors=True)


# [TODO: add additional validation]
# [TODO: consider using this paired with SQLAlchemy]
# [TODO: return _ to sql query for _level and _mode]
class Score(BaseModel):
    timestamp: int
    era: int
    username1: str
    username2: Optional[str] = None
    level: str 
    score: int
    country: Optional[str]
    platform: Optional[str]
    mode: int


def get_router(con: sqlite3.Connection) -> APIRouter:
    """Create FastAPI router, given database connection"""
    logger.trace("Creating FastAPI router for update methods")

    router = APIRouter()

    @router.post("/insert_score/", tags=["update"])
    def insert_score(score: Score):
        """Insert a single score into the database"""
        logger.log("API", "Got POST request to insert score: <w>{}</>",
                   repr(score))

        db_insert_score(con, score)

    @router.delete("/delete_score/", tags=["update"])
    def delete_score(id: int):
        """Delete a particular score from the database"""
        logger.log("API", "Got POST request to delete score, id <m>{}</>",
                   id)

        db_delete_score(con, id)


    return router
