"""Backend entry point"""

from loguru import logger
from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from .api.database.connect import main as db_connect
from .api.metadata import API_TAGS_METADATA, API_DESCRIPTION

from .api.scores import get_router as get_router_scores
from .api.cached import get_router as get_router_cached
from .api.update import get_router as get_router_update
from .api.parse import router as api_parse_router

logger = logger.opt(colors=True)


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

    # make API only accessible locally
    app.add_middleware(
        TrustedHostMiddleware, allowed_hosts=["localhost"] 
    )

    app.include_router(get_router_scores(db_con))
    # app.include_router(get_router_cached(db_con))
    app.include_router(api_parse_router, prefix="/parse")
    app.include_router(get_router_update(db_con))

    return app
