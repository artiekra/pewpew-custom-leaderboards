"""Connection between frontend and backend"""

import requests

from loguru import logger

logger.opt(colors=True)


def query_api_get(method: str) -> any:
    """Query particular method in API (GET)"""
    logger.debug("Frontend queries API at <m>GET {}</>", method)

    # [TODO: improve this.. maybe use config?]
    result = requests.get("http://localhost:8000/" + method)
    result_json = result.json()

    logger.trace("API returned <w>{}</>", result_json)
    return result_json
