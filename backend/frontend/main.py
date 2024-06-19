"""Frontend entry point"""

from loguru import logger
from flask import Flask

from .blueprints.leaderboards import bp as leaderboards_pb

logger = logger.opt(colors=True)


def get_app(config: dict) -> Flask:
    """Setup and get Flask app"""

    # custom logging (loguru) method for frontend-specific stuff
    # debug 10, info 20, error 40
    logger.level("FRONT", no=10, color="<fg #9800ff>")

    app = Flask(__name__)

    app.register_blueprint(leaderboards_pb)

    return app
