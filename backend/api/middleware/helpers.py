"""Useful helpers for FastAPI middleware"""

import time

from loguru import logger

logger = logger.opt(colors=True)


async def unpack_request(raw_request) -> dict:
    """Get useful data out of request object"""
    logger.trace("Unpacking request: <m>{}</>", raw_request)

    path = raw_request.url.path
    if raw_request.query_params:
        path += f"?{raw_request.query_params}"

    request = {
        "method": raw_request.method,
        "path": path,
        "ip": raw_request.client.host
    }

    try:
        body = await raw_request.json()
    except:  # [TODO: stop using bare "except" statement]
        body = None
    request["json_body"] = body

    return request
