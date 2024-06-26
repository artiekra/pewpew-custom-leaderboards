"""Run FastAPI for backend (methods, related to getting score data)"""

from typing import Union, Optional

from loguru import logger
from fastapi import APIRouter
from pydantic import BaseModel

import database.interact as dbi
from database.table import ScoreCreate, Score

logger = logger.opt(colors=True)


def get_router(engine) -> APIRouter:
    """Create FastAPI router, given database connection"""
    logger.trace("Creating FastAPI router for update methods")

    router = APIRouter()


    @router.post("/insert_score/", tags=["update"])
    def insert_score(score: ScoreCreate):
        """Insert a single score into the database"""
        score_data = score.model_dump(exclude_unset=True)
        new_score = Score(**score_data)

        dbi.insert_score(engine, new_score)


    # [TODO: fix]
    # [TODO: make it also affect the leaderboards]
    @router.put("/update_score/", tags=["update"])
    def update_score(id: int, score: ScoreCreate):
        """Update a single score in the database"""
        score_data = score.model_dump(exclude_unset=True)
        new_score = Score(**score_data)

        dbi.update_score(engine, id, new_score)


    # [TODO: make it also affect the leaderboards]
    @router.delete("/delete_score/", tags=["update"])
    def delete_score(id: int):
        """Delete a particular score from the database"""
        dbi.delete_score(engine, id)


    return router
