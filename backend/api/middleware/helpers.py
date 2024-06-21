"""Useful helpers for FastAPI middleware"""

import time

from loguru import logger

logger = logger.opt(colors=True)

    
class AsyncIteratorWrapper:
    """The following is a utility class that transforms a regular
    iterable to an asynchronous one.
    https://www.python.org/dev/peps/pep-0492/#example-2"""

    def __init__(self, obj):
        self._it = iter(obj)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            value = next(self._it)
        except StopIteration:
            raise StopAsyncIteration
        return value


async def request_execute(call_next, request, request_id: str):
    """Execute given request, and log on exceptions"""

    try:
        response = await call_next(request)

        # kickback X-API-Request-ID
        response.headers["X-API-Request-ID"] = request_id
        return response

    except Exception as e:
        details = {
            "path": request.url.path,
            "method": request.method,
            "reason": e
        }
        logger.opt(exception=True).error(
            "Got error on executing request: <w>{}</>", details)


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


async def unpack_response(call_next, request, request_id: str) -> dict:
    """Get useful data out of api response"""
    logger.trace("Unpacking responce for request: <m>{}</>, with id <m>{}</>",
                 request, request_id)

    start_time = time.perf_counter()
    response = await request_execute(call_next, request, request_id)
    finish_time = time.perf_counter()

    # [TODO: fix when response is none cuz of error in request_execute]
    overall_status = "successful" if response.status_code < 400 else "failed"
    execution_time = finish_time - start_time

    response_data = {
        "status": overall_status,
        "status_code": response.status_code,
        "time_taken": execution_time
    }

    resp_body = [section async for section in response.__dict__["body_iterator"]]
    response.__setattr__("body_iterator", AsyncIteratorWrapper(resp_body))

    try:
        resp_body = json.loads(resp_body[0].decode())
    except:
        resp_body = str(resp_body)

    response_data["json_body"] = resp_body

    return response, response_data
