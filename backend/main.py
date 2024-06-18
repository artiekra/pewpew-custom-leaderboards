"""Backend entry point"""

import sys
import signal
from datetime import datetime

import orjson
import uvicorn
from loguru import logger
from fastapi import FastAPI

import database.connect as dbc
import database.interact as dbi
from api.metadata import API_TAGS_METADATA, API_DESCRIPTION

import api.scores
import api.cached
import api.parse
import api.update

logger.remove(0)
logger.add(sys.stderr, level="TRACE")
logger = logger.opt(colors=True)


def sigint_handler(sig, frame):
    """Handle SIGINT signal (e.g. Ctrl+C)"""
    logger.error("Got SIGINT, stopping...")
    logger.trace("sig=<m>{}</>, frame=<m>{}</>", sig, frame)

    sys.exit(0)


def get_app(config: dict) -> FastAPI:
    """Setup and get FastAPI app"""
    logger.debug("Registering signal handler for <y>{}</>", "signal.SIGINT")
    signal.signal(signal.SIGINT, sigint_handler)

    session = dbc.main(config["database"])

    app = FastAPI(title="PewPew Community Portal", description=API_DESCRIPTION,
      openapi_tags=API_TAGS_METADATA, license_info={
        "name": "Apache 2.0"
    })
    app.include_router(api.scores.router)
    app.include_router(api.cached.router)
    app.include_router(api.parse.router, prefix="/parse")
    app.include_router(api.update.router)

    return app


def main(config: dict) -> None:
    """Run FastAPI on uvicorn server"""
    logger.info("Launching uvicorn on 0.0.0.0:8000.. (app: FastAPI)")

    app = get_app(config)

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    logger.info("Starting backend...")
    with open("config.json", "r", encoding="UTF-8") as file:
        config = orjson.loads(file.read())
    main(config)
