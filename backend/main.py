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

from api.scores import get_router as get_router_scores
from api.cached import get_router as get_router_cached
from api.update import get_router as get_router_update
import api.parse

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

    db_con = dbc.main(config["database"])

    # custom logging (loguru) method for API-specific stuff
    # debug 10, info 20, error 40
    logger.level("API", no=10, color="<fg #ff7100>")

    app = FastAPI(title="PewPew Community Portal", description=API_DESCRIPTION,
      openapi_tags=API_TAGS_METADATA, license_info={
        "name": "Apache 2.0"
    })
    # app.include_router(get_router_scores(db_con))
    # app.include_router(get_router_cached(db_con))
    app.include_router(api.parse.router, prefix="/parse")
    app.include_router(get_router_update(db_con))

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
