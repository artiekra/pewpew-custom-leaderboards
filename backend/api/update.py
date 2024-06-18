"""Run FastAPI for backend (methods, related to getting score data)"""

from typing import Union

from loguru import logger
from fastapi import APIRouter

logger = logger.opt(colors=True)

router = APIRouter()


@router.get("/insert_score/", tags=["update"])
async def insert_score():
    """Insert a single score into the database"""
    return {"error": "Hi!"}


@router.get("/parse_score/", tags=["update"])
async def parse_score():
    """Parse score message from #scores-feed"""
    return {"error": "Hi!"}
