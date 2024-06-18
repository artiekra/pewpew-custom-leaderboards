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

    scores = [
        {
          "timestamp": 0,
          "era": 0,
          "username1": "string",
          "username2": "string",
          "level": "string",
          "score": 0,
          "country": "string",
          "platform": "string",
          "mode": 0
        },
        {
          "timestamp": 1,
          "era": 0,
          "username1": "stringss",
          "username2": "string",
          "level": "string",
          "score": 0,
          "country": "string",
          "platform": "string",
          "mode": 0
        }
    ]

    return render_template("scores-feed.htm", scores=scores)
