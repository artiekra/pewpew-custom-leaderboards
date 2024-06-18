"""Backend entry point"""

import sys
import signal
from datetime import datetime

import orjson
from loguru import logger

import database.connect as dbc
import database.interact as dbi
from parser.parse import parse_score

logger.remove(0)
logger.add(sys.stderr, level="TRACE")
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

    msg = input()
    parsed = parse_score(msg)
    dbi.insert_score(session, parsed)


if __name__ == "__main__":
    logger.info("Starting backend...")
    with open("config.json", "r", encoding="UTF-8") as file:
        config = orjson.loads(file.read())
    main(config)
