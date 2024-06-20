"""Backend entry point"""

import orjson
import uvicorn

from loguru import logger

from api.main import get_app

logger = logger.opt(colors=True)


def main(backend_config: dict) -> None:
    """Run FastAPI on uvicorn server"""
    logger.info("Launching uvicorn on 0.0.0.0:8000.. (app: FastAPI)")

    app = get_app(backend_config)

    uvicorn.run(app, host="0.0.0.0", port=8000)


# [TODO: everywhere, con => session]
if __name__ == "__main__":
    logger.info("Starting backend...")
    with open("config.json", "r", encoding="UTF-8") as file:
        config = orjson.loads(file.read())  # pylint: disable=no-member
    main(config)
