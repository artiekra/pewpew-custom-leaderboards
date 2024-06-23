"""Backend entry point"""

import sys

import orjson
import uvicorn

from loguru import logger

from api.main import get_app

logger = logger.opt(colors=True)


def main(backend_config: dict) -> None:
    """Run FastAPI on uvicorn server"""
    logger.info("Launching uvicorn on 0.0.0.0:8000.. (app: FastAPI)")

    # [TODO: make print_logs affect logs at the start an uvicorn logs too]
    logger.remove(0)
    if backend_config["logs"]["print_logs"]:
        logger.add(sys.stderr, level=backend_config["logs"]["log_level"],
                   enqueue=True)

    app = get_app(backend_config)

    uvicorn.run(app, host="0.0.0.0", port=8000)


# [TODO: everywhere, type hints]
# [TODO: everywhere, handle exceptions properly]
# [TODO: everywhere, main_query/query, ... => statement]
# [TODO: everywhere, consider changing style of how sqla queries are written]
if __name__ == "__main__":
    logger.info("Starting backend...")
    with open("config.json", "r", encoding="UTF-8") as file:
        config = orjson.loads(file.read())  # pylint: disable=no-member
    main(config)
