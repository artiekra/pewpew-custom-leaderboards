"""Run FastAPI for backend (methods, related to getting score data)"""

import sqlite3
from typing import Union, Optional

from loguru import logger
from fastapi import APIRouter
from pydantic import BaseModel

import database.interact as dbi
from database.table import ScoreCreate, Score

logger = logger.opt(colors=True)


# [TODO: remove unneccesarry now logging (since logging middleware exists)]
def get_router(con: sqlite3.Connection) -> APIRouter:
    """Create FastAPI router, given database connection"""
    logger.trace("Creating FastAPI router for update methods")

    router = APIRouter()

    @router.post("/insert_score/", tags=["update"])
    def insert_score(score: ScoreCreate):
        """Insert a single score into the database"""
        logger.log("API", "Got POST request to insert score: <w>{}</>",
                   repr(score))

        score_data = score.model_dump(exclude_unset=True)
        new_score = Score(**score_data)

        dbi.insert_score(con, new_score)

    # [TODO: fix]
    @router.put("/update_score/", tags=["update"])
    def update_score(id: int, score: ScoreCreate):
        """Update a single score in the database"""
        logger.log("API",
            "Got PUT request to update score (id <m>{}</>): <w>{}</>",
            id, repr(score))

        score_data = score.model_dump(exclude_unset=True)
        new_score = Score(**score_data)

        dbi.update_score(con, id, new_score)

    @router.delete("/delete_score/", tags=["update"])
    def delete_score(id: int):
        """Delete a particular score from the database"""
        logger.log("API", "Got POST request to delete score, id <m>{}</>",
                   id)

        dbi.delete_score(con, id)

    return router
