"""Interacting (add/get data) with the database (SQLite)"""

from typing import Tuple, Optional
from datetime import datetime

from loguru import logger
from sqlalchemy import insert
from pydantic import BaseModel

from database.connect import Score

logger = logger.opt(colors=True)


def insert_score(session, score: Score) -> None:
    """Insert data about a certain score into "scores" table"""
    logger.debug("Adding a score: <w>{}</>", repr(score))

    session.add(score)
    session.commit()
