"""Frontend entry point"""

from loguru import logger
from flask import Flask

logger = logger.opt(colors=True)


def get_app(config: dict) -> Flask:
    """Setup and get Flask app"""

    # custom logging (loguru) method for frontend-specific stuff
    # debug 10, info 20, error 40
    logger.level("FRONT", no=10, color="<fg #9800ff>")

    app = Flask(__name__)

    @app.route("/")
    @app.route("/scores-feed")
    def scores_feed():
        """Render #scores-feed live"""
        logger.log("FRONT", "Front-end requested: <m>{}</>",
            "/scores-feed")

        return "Hi!"

    return app
