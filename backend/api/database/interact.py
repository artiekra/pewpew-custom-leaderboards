"""Interacting (add/get data) with the database (SQLite)"""

from datetime import datetime
import sqlite3

from loguru import logger

from .query import QUERIES

logger = logger.opt(colors=True)


def db_insert_score(con: sqlite3.Connection, score) -> None:
    """Insert data about a certain score into "score" table"""
    logger.debug("Adding a score: <w>{}</>", repr(score))

    cur = con.cursor()
    cur.execute(QUERIES["insert_score"], dict(score))

    con.commit()
