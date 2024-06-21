"""Interacting (add/get data) with the database (SQLite)"""

from sqlalchemy import text

from loguru import logger
from sqlmodel import select, distinct, func

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
    # [TODO: optimize code? dry?]
    main_query = select(Score).offset(page*limit).limit(limit)
    count_query = session.query(Score)
    count = count_query.count()

    if era is not None:
        main_query = main_query.where(Score.era == era)
        count_query = count_query.where(Score.era == era)
    if timestamp_start is not None:
        main_query = main_query.where(timestamp_start <= Score.timestamp)
        count_query = count_query.where(timestamp_start <= Score.timestamp)
    if timestamp_end is not None:
        main_query = main_query.where(Score.timestamp <= timestamp_end)
        count_query = count_query.where(Score.timestamp <= timestamp_end)

    # [TODO: use select(id) and count primary keys only for efficiency]
    count_filtered = count_query.count()

    result = session.exec(main_query).all()

    metadata = {
        "item_count": count,
        "item_count_filtered": count_filtered
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

    return result


# [TODO: add metadata]
def get_players(session, era: int|None) -> list[tuple]:
    """Get all the players available in the database"""
    logger.debug("Getting all the player pairs from the database, era <m>{}</>",
                 era)

    full_query = select(Score.username1, Score.username2)
    if era is not None:
        full_query = full_query.where(Score.era == era)

    result = session.exec(full_query.group_by(Score.username1,
        Score.username2)).all()

    print(result)

    return result


def get_level_play_count(session, level: str,
                         filters: list[int|None]) -> int:
    """Get the amount of times a particular level was played"""
    logger.debug("Getting level play count for <m>{}</>", level)

    era, mode = filters
    logger.trace("filters: <w>{}</>", filters)

    return 1


# [TODO: make mode filter work]
# [TODO: optimizations (i.e. call cache results of get_level_play_count)]
def get_leaderboard_vars(session, filters: list[int|None]) -> list[tuple]:
    """Get variables (N, R, etc) for leaderboards"""
    logger.debug("Getting leaderboard variables..")

    era, mode = filters
    logger.trace("filters: <w>{}</>", filters)

    players = get_players(session, era)
    
    results = []
    for player in players:
        levels = get_player_latest(session, player[0], [era, None])

        # pb - personal best
        for pb in levels:
            level_name = pb.level

            n = get_level_play_count(session, level_name, filters)
            results.append({
                "players": player,
                "level": level_name, 
                "n": n
            })

    return results
