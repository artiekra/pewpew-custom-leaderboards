"""Run FastAPI for backend (methods, related to getting score data)"""

from typing import Union

from loguru import logger
from fastapi import APIRouter

import parser.parse

logger = logger.opt(colors=True)

router = APIRouter()


@router.post("/insert_score/", tags=["update"])
def insert_score():
    """Insert a single score into the database"""
    return {"error": "Hi!"}


@router.delete("/delete_score/", tags=["update"])
def delete_score():
    """Delete a particular score from the database"""
    return {"error": "Hi!"}
