"""Connecting/setting up the database (SQLite)"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.table import Base

from loguru import logger

logger = logger.opt(colors=True)


def get_db_link(db_file: str) -> str:
    """Get SQLite link from file name"""
    logger.trace("Converting <m>{}</> to SQLite db link", db_file)

    return "sqlite:///" + db_file


def main(db_file: str) -> None:
    """Connect to the given database (SQLite file) and
    create neccesarry tables"""
    db_url = get_db_link(db_file)
    logger.debug("Connecting to <m>{}</>", db_url)

    engine = create_engine(get_db_link(db_file))

    logger.info("Creating missing tables..")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    return session
