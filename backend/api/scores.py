"""Run FastAPI for backend (methods, related to updating scores)"""

from loguru import logger
from fastapi import APIRouter

logger = logger.opt(colors=True)

router = APIRouter()
