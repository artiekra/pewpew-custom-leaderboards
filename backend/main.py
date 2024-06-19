"""Launch both backend and frontend (flask)"""

import sys
import signal
import asyncio

import orjson
from loguru import logger

from a2wsgi import WSGIMiddleware
from uvicorn import Server, Config

import backend.main
import frontend.main

# comment out to not get TRACE logs (default is DEBUG)
logger.remove(0)
logger.add(sys.stderr, level="TRACE")

logger = logger.opt(colors=True)


def sigint_handler(sig, frame):
    """Handle SIGINT signal (e.g. Ctrl+C)"""
    logger.error("Got SIGINT, stopping...")
    logger.trace("sig=<m>{}</>, frame=<m>{}</>", sig, frame)

    sys.exit(0)


class MyServer(Server):

    async def run(self, sockets=None):
        self.config.setup_event_loop()
        return await self.serve(sockets=sockets)


async def main(config_path: str = "config.json") -> None:
    """Run the app (both frontend&backend)"""
    logger.info("Reading config and running the app..")

    logger.debug("Registering signal handler for <y>{}</>", "signal.SIGINT")
    signal.signal(signal.SIGINT, sigint_handler)

    with open(config_path, "r", encoding="UTF-8") as file:
        config = orjson.loads(file.read())
    api = backend.main.get_app(config)

    frontend_app = frontend.main.get_app(config)
    asgi_frontend = WSGIMiddleware(frontend_app)

    config_list = [
        (api, config["uvicorn"]["port_api"]),
        (asgi_frontend, config["uvicorn"]["port_frontend"]),
    ]
    apps = []
    for cfg in config_list:
        server_config = Config(cfg[0], host=config["uvicorn"]["host"], port=cfg[1])
        server = MyServer(config=server_config)
        apps.append(server.run())
    return await asyncio.gather(*apps)
 

if __name__ == "__main__":
    logger.info("Starting the app...")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
