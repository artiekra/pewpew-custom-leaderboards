"""Run FastAPI for backend (methods, related to parsing scores from #scores-feed)"""

from typing import Union

from loguru import logger
from fastapi import APIRouter

from parser.parse import apply_regex_raw
from parser.parse import parse_score as parser_parse_score
from parser.metadata import parse_platform as parser_parse_platform

logger = logger.opt(colors=True)

router = APIRouter()


@router.post("/parse_score/", tags=["parse"])
def parse_score(message: str):
    """Parse score message from #scores-feed.
    Pass JUST the message WITH formatting IN MARKDOWN."""
    parsed = parser_parse_score(message)

    return {"response": parsed}


@router.post("/apply_regex/", tags=["parse"])
def apply_regex_to_score(message: str):
    """Apply regex, which is used for parsing scores in #scores-feed.
    Divides given string (Discord message assumed) into capture groups.
    Pass JUST the message WITH formatting IN MARKDOWN."""
    parsed = apply_regex_raw(message)

    return {"response": parsed}


@router.post("/parse_platform/", tags=["parse"])
def parse_platform(message: str):
    """Convert emoji/text into one of the platforms.
    a android, i ios, w windows, b web, u/e unknown
    (e - uknown by parser, u - uknown by #scores-feed)"""
    parsed = parser_parse_platform(message)

    return {"response": parsed}
