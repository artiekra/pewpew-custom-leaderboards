"""Run FastAPI for backend (methods, related to getting score data)"""

from typing import Union

from loguru import logger
from fastapi import APIRouter

import parser.parse

logger = logger.opt(colors=True)

router = APIRouter()


@router.put("/insert_score/", tags=["update"])
def insert_score():
    """Insert a single score into the database"""
    return {"error": "Hi!"}


# [TODO: implement separate api logger class]
@router.post("/parse_score/", tags=["update"])
def parse_score(message: str):
    """Parse score message from #scores-feed"""
    logger.debug("Got POST request to parse <w>{}</>", message)

    parsed = parser.parse.parse_score(message)

    return {"responce": parsed}


@router.delete("/delete_score/", tags=["update"])
def delete_score():
    """Delete a particular score from the database"""
    return {"error": "Hi!"}
