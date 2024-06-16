"""Interacting (add/get data) with the database (SQLite)"""

from datetime import datetime
import sqlite3

from database.query import QUERIES
from loguru import logger

logger = logger.opt(colors=True)


def insert_score(con: sqlite3.Connection, score) -> None:
    """Insert data about a certain score into "score" table"""
    logger.debug("Adding a score: <w>{}</>", repr(score))

    cur = con.cursor()
    cur.execute(QUERIES["insert_score"], score)

    con.commit()


def insert_level(con: sqlite3.Connection, level) -> None:
    """Insert data about a certain level into "level" table"""
    logger.debug("Adding a level: <w>{}</>", repr(level))

    cur = con.cursor()
    cur.execute(QUERIES["insert_level"], level)

    con.commit()
