"""Flask blueprint for leaderboard-related pages"""

from pathlib import Path

from loguru import logger
from flask import Blueprint, render_template

from .query_api import query_api_get

logger = logger.opt(colors=True)

# templates_path = str(Path(__file__).parent / "templates/")
bp = Blueprint("leaderboards", __name__,
        template_folder="templates")


@bp.route("/")
@bp.route("/scores-feed")
def scores_feed():
    """Render #scores-feed live"""
    logger.log("FRONT", "Front-end requested: <m>{}</>",
        "/scores-feed")

    scores = query_api_get("get_scores/")

    return render_template("scores-feed.htm", scores=scores)
