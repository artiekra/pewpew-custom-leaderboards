"""Interacting (add/get data) with the database (SQLite)"""

from typing import Tuple, Optional
from datetime import datetime

from loguru import logger
from sqlalchemy import insert
from pydantic import BaseModel

import database.table as dbt

logger = logger.opt(colors=True)


def insert_score(session, score: dbt.Score) -> None:
    """Insert data about a certain score into "score" table"""
    logger.debug("Adding a score: <w>{}</>", repr(score))

    session.add(score)
    session.commit()


def insert_level(session, level: dbt.Level) -> None:
    """Insert data about a certain level into "level" table"""
    logger.debug("Adding a level: <w>{}</>", repr(level))

    session.add(level)
    session.commit()
