"""Interacting (add/get data) with the database (SQLite)"""

from datetime import datetime
import sqlite3

from loguru import logger

from database.query import QUERIES

logger = logger.opt(colors=True)


def insert_score(con: sqlite3.Connection, score) -> None:
    """Insert data about a certain score into "score" table"""
    logger.debug("Adding a score: <w>{}</>", repr(score))

    cur = con.cursor()
    cur.execute(QUERIES["insert_score"], dict(score))

    con.commit()


def update_score(con: sqlite3.Connection, id, score) -> None:
    """Update data about a certain score in the "score" table"""
    logger.debug("Updating a score (id <m>{}</>): <w>{}</>",
                 id, repr(score))

    data = dict(score)
    data.update({"id": id})

    cur = con.cursor()
    cur.execute(QUERIES["update_score"], data)

    con.commit()


def delete_score(con: sqlite3.Connection, id: int) -> None:
    """Delete data about a certain score from"score" table,
    given the id"""
    logger.debug("Deleting score with id <m>{}</>", id)

    cur = con.cursor()
    cur.execute(QUERIES["remove_score"], {"id": id})

    con.commit()


def get_all(con: sqlite3.Connection, page: int, limit: int,
               filters: list[int|None]) -> list[tuple]:
    """Get all available in the database data"""
    logger.debug("Getting everything from the database..")

    timestamp_start, timestamp_end, era = filters
    logger.trace("Filters: <w>{}</>", filters)

    cur = con.cursor()
    cur.execute(QUERIES["get_all"], {"page": page, "limit": limit})
    result = cur.fetchall()

    cur.execute(QUERIES["get_score_count"])
    count = cur.fetchone()[0]
    
    metadata = {
        "total_items": count
    }

    return result, metadata


def get_player_latest(con: sqlite3.Connection, player: str,
               filters: list[int|None]) -> list[tuple]:
    """Get all latest player scores in the database data"""
    logger.debug("Getting latest player (<m>{}</>) scores from the database..",
                 player)

    era, mode = filters
    logger.trace("Filters: <w>{}</>", filters)

    cur = con.cursor()
    cur.execute(QUERIES["get_player_latest"], {"player": player})
    result = cur.fetchall()

    return result
