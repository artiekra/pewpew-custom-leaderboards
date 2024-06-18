"""Launch both backend and frontend"""

import orjson
from loguru import logger

import backend.main

logger = logger.opt(colors=True)


def main(config_path: str) -> None:
    """Run the app (both frontend&backend)"""
    logger.info("Reading config and running the app..")

    with open(config_path, "r", encoding="UTF-8") as file:
        config = orjson.loads(file.read())
    backend.main.main(config)
 

if __name__ == "__main__":
    logger.info("Starting the app...")
    main("config.json")
