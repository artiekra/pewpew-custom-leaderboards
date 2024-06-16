"""Parse a message from #scores-feed"""

from loguru import logger

from database.table import Score

logger = logger.opt(colors=True)


def parse_score(raw: str) -> Score:
    """Parse given message into Score and Level types"""

    pass
