"""Launch both backend and frontend"""

import orjson
from loguru import logger

import backend.main

logger = logger.opt(colors=True)


if __name__ == "__main__":
    logger.info("Starting the app...")
    with open("config.json", "r", encoding="UTF-8") as file:
        config = orjson.loads(file.read())
    backend.main.main(config)
