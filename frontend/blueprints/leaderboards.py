"""Flask blueprint for leaderboard-related pages"""

from pathlib import Path

from loguru import logger
from flask import Blueprint, render_template

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

    return render_template("scores-feed.htm")
