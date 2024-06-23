"""API entry point"""

from loguru import logger
from fastapi import APIRouter
from fastapi import FastAPI

from database.connect import main as db_connect

from api.methods.metadata import API_TAGS_METADATA, API_DESCRIPTION
from api.methods.scores import get_router as get_router_scores
from api.methods.leaderboards import get_router as get_router_leaderboards
from api.methods.update import get_router as get_router_update
from api.methods.parse import router as api_parse_router

from api.middleware.main import add_middleware

logger = logger.opt(colors=True)


def include_router_v1(app: FastAPI, router: APIRouter, prefix: str) -> None:
    """Include router with different versioning prefixes
    (without version, "v1" and "latest")
    `prefix` is raw, without any slashes"""
    logger.trace("Including router with prefix <m>{}</>", prefix)

    prefix = "/" + prefix
    prefix2 = "/v1" + prefix
    prefix3 = "/latest" + prefix

    app.include_router(router, prefix=prefix, include_in_schema=False)
    app.include_router(router, prefix=prefix2)
    app.include_router(router, prefix=prefix3, include_in_schema=False)


def get_app(config: dict) -> FastAPI:
    """Setup and get FastAPI app"""
    logger.debug("Creating FastAPI app..")

    is_echo = config["database"]["config"]["echo"]
    engine = db_connect(config["database"]["file"], is_echo)

    # custom logging (loguru) method for API-specific stuff
    # debug 10, info 20, error 40
    logger.level("API", no=10, color="<fg #ff7100>")

    app = FastAPI(title="PewPew Community Portal", description=API_DESCRIPTION,
      openapi_tags=API_TAGS_METADATA, license_info={
        "name": "Apache 2.0"
    })

    add_middleware(app, engine)

    include_router_v1(app, get_router_scores(engine), "scores")
    include_router_v1(app, get_router_leaderboards(engine), "leaderboards")
    include_router_v1(app, api_parse_router, "parse")
    include_router_v1(app, get_router_update(engine), "update")

    return app
