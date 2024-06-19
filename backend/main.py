"""Backend entry point"""

import orjson
import uvicorn

from loguru import logger
from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware

from database.connect import main as db_connect
from api.metadata import API_TAGS_METADATA, API_DESCRIPTION

from api.scores import get_router as get_router_scores
from api.cached import get_router as get_router_cached
from api.update import get_router as get_router_update
from api.parse import router as api_parse_router

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

    db_con = db_connect(config["database"])

    # custom logging (loguru) method for API-specific stuff
    # debug 10, info 20, error 40
    logger.level("API", no=10, color="<fg #ff7100>")

    app = FastAPI(title="PewPew Community Portal", description=API_DESCRIPTION,
      openapi_tags=API_TAGS_METADATA, license_info={
        "name": "Apache 2.0"
    })

    # implement CORS
    origins = [
        "http://localhost:5001",  # Flask frontend
        "http://localhost:5173",  # React frontend
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    include_router_v1(app, get_router_scores(db_con), "scores")
    # app.include_router(get_router_cached(db_con))
    include_router_v1(app, api_parse_router, "parse")
    include_router_v1(app, get_router_update(db_con), "update")

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
