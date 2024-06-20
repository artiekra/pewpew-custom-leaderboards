"""Connecting/setting up the database (SQLite)"""

from sqlmodel import SQLModel, Session, create_engine

from database.table import Score

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

    # [TODO: echo=True, when specified so in config]
    engine = create_engine(get_db_link(db_file), echo=False)

    logger.info("Creating missing tables..")
    SQLModel.metadata.create_all(engine)

    session = Session(engine)

    return session
