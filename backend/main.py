"""Backend entry point"""

import sys
import signal
from datetime import datetime

import orjson
from loguru import logger

import database.connect as dbc
import database.interact as dbi

logger = logger.opt(colors=True)


def sigint_handler(sig, frame):
    """Handle SIGINT signal (e.g. Ctrl+C)"""
    logger.error("Got SIGINT, stopping...")
    logger.trace("sig=<m>{}</>, frame=<m>{}</>", sig, frame)

    sys.exit(0)


def main(config: dict) -> None:
    """Start the backend with given config (as dict)"""

    logger.debug("Registering signal handler for <y>{}</>", "signal.SIGINT")
    signal.signal(signal.SIGINT, sigint_handler)

    session = dbc.main(config["database"])

    test_score = dbc.Score(
        timestamp=datetime.now(),
        era=0,
        username1="test",
        username2="test2",
        level_id=0,
        score=0,
        country="test",
        platform="test",
        mode=0,
    )
    dbi.insert_score(session, test_score)


if __name__ == "__main__":
    logger.info("Starting backend...")
    with open("config.json", "r", encoding="UTF-8") as file:
        config = orjson.loads(file.read())
    main(config)
