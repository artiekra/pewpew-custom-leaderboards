"""Interacting (add/get data) with the database (SQLite)"""

from sqlalchemy import text

from loguru import logger
from sqlmodel import select

from database.table import Score
from database.query import QUERIES

logger = logger.opt(colors=True)


def insert_score(con, score: Score) -> None:
    """Insert data about a certain score into "score" table"""
    logger.debug("Adding a score: <w>{}</>", repr(score))

    con.add(score)
    con.commit()


def update_score(con, score_id: int, score: Score) -> None:
    """Update data about a certain score in the "score" table"""
    logger.debug("Updating a score (id <m>{}</>): <w>{}</>",
                 score_id, repr(score))

    db_score = con.get(Score, score_id)
    db_score.sqlmodel_update(score)
    con.add(db_score)
    con.commit()


def delete_score(con, score_id: int) -> None:
    """Delete data about a certain score from"score" table,
    given the id"""
    logger.debug("Deleting score with id <m>{}</>", score_id)

    score = con.get(Score, score_id)
    con.delete(score)
    con.commit()


def get_all(con, page: int, limit: int,
               filters: list[int|None]) -> list[tuple]:
    """Get all available in the database data"""
    logger.debug("Getting everything from the database..")

    timestamp_start, timestamp_end, era = filters
    logger.trace("Filters: <w>{}</>", filters)

    # [TODO: page-based pagination exists as built-in? maybe?]
    result = con.exec(select(Score).offset(page*limit).limit(limit)).all()

    # [TODO: use select(id) and count primary keys only for efficiency]
    count = con.query(Score).count()

    metadata = {
        "total_items": count
    }

    return result, metadata


def get_player_latest(con, player: str,
               filters: list[int|None]) -> list[tuple]:
    """Get all latest player scores in the database data"""
    logger.debug("Getting latest player (<m>{}</>) scores from the database..",
                 player)

    era, mode = filters
    logger.trace("Filters: <w>{}</>", filters)

    sql = text(QUERIES["get_player_latest"])
    result = con.execute(sql, {"player": player})

    return result.all()
