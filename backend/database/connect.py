"""Connecting/setting up the database (SQLite)"""

import sqlite3

from database.table import Base

from loguru import logger

logger = logger.opt(colors=True)


def create_tables(con):
    pass


def main(db_file: str) -> None:
    """Connect to the given database (SQLite file) and
    create neccesarry tables"""
    logger.debug("Connecting to <m>{}</>", db_file)

    con = sqlite3.connect(db_file)
    print(type(con))

    logger.info("Creating missing tables..")
    create_tables(con)

    return con
