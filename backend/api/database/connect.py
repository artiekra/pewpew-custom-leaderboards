"""Connecting/setting up the database (SQLite)"""

import sqlite3

from loguru import logger

from .query import QUERIES

logger = logger.opt(colors=True)


def create_tables(con: sqlite3.Connection) -> None:
    """Create all the tables in the database"""
    logger.info("Creating missing tables..")

    cur = con.cursor()
    cur.execute(QUERIES["create_table_score"])

    con.commit()


def main(db_file: str) -> sqlite3.Connection:
    """Connect to the given database (SQLite file) and
    create neccesarry tables"""
    logger.debug("Connecting to <m>{}</>", db_file)

    con = sqlite3.connect(db_file, check_same_thread=False)
    print(type(con))

    create_tables(con)

    return con
