"""Interacting (add/get data) with the database (SQLite)"""

from sqlalchemy import text

from loguru import logger
from sqlmodel import select

from database.table import Score
from database.query import QUERIES

logger = logger.opt(colors=True)


def insert_score(session, score: Score) -> None:
    """Insert data about a certain score into "score" table"""
    logger.debug("Adding a score: <w>{}</>", repr(score))

    session.add(score)
    session.commit()


def update_score(session, score_id: int, score: Score) -> None:
    """Update data about a certain score in the "score" table"""
    logger.debug("Updating a score (id <m>{}</>): <w>{}</>",
                 score_id, repr(score))

    db_score = session.get(Score, score_id)
    db_score.sqlmodel_update(score)
    session.add(db_score)
    session.commit()


def delete_score(session, score_id: int) -> None:
    """Delete data about a certain score from"score" table,
    given the id"""
    logger.debug("Deleting score with id <m>{}</>", score_id)

    score = session.get(Score, score_id)
    session.delete(score)
    session.commit()


def get_scores(session, page: int, limit: int,
            filters: list[int|None]) -> list[tuple]:
    """Get all available in the database data"""
    logger.debug("Getting everything from the database..")

    timestamp_start, timestamp_end, era = filters
    logger.trace("Filters: <w>{}</>", filters)

    # [TODO: page-based pagination exists as built-in? maybe?]
    query = select(Score).offset(page*limit).limit(limit)
    if era is not None:
        query = query.where(Score.era == era)
    if timestamp_start is not None:
        query = query.where(timestamp_start <= Score.timestamp)
    if timestamp_end is not None:
        query = query.where(Score.timestamp <= timestamp_end)
    result = session.exec(query).all()

    # [TODO: use select(id) and count primary keys only for efficiency]
    count = session.query(Score).count()

    metadata = {
        "total_items": count
    }

    return result, metadata


def get_player_latest(session, player: str,
                      filters: list[int|None]) -> list[tuple]:
    """Get all latest player scores in the database data"""
    logger.debug("Getting latest player (<m>{}</>) scores from the database..",
                 player)

    era, mode = filters
    logger.trace("Filters: <w>{}</>", filters)

    query = select(Score).order_by(Score.timestamp.desc()) \
        .where((Score.username1 == player) | (Score.username2 == player))
    if era is not None:
        query = query.where(Score.era == era)
    if mode is not None:
        query = query.where(Score.mode == mode)

    result = session.exec(query.group_by(Score.level)).all()

    print(result)

    return result
