"""Add all the neccesarry middleware to FastAPI"""

from loguru import logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from api.middleware.logging import LoggingMiddleware

logger = logger.opt(colors=True)


def add_cors(app: FastAPI) -> None:
    """Add CORS middleware to a given FastAPI app"""
    logger.trace("Adding CORS middleware..")

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


#[TODO: add RateLimitingMiddleware (for public methods)]
def add_middleware(app: FastAPI, engine) -> None:
    """Adds all the middleware to a given FastAPI app"""
    logger.debug("Adding available middleware to the app..")

    add_cors(app)

    app.add_middleware(LoggingMiddleware, engine=engine)
    app.add_middleware(GZipMiddleware, minimum_size=1000)  # default min 500
