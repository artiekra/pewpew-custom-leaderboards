"""FastAPI Middleware - applied for each request"""

from typing import Callable

from loguru import logger

from fastapi import FastAPI
from fastapi import Request, Response  # for typing
from starlette.middleware.base import BaseHTTPMiddleware

from api.middleware.helpers import unpack_request

from database.table import ApiRequest

logger = logger.opt(colors=True)


# [TODO: log response, not just request]
# [TODO: consider adding X-API-REQUEST-ID]
class LoggingMiddleware(BaseHTTPMiddleware):

    def __init__(self, app: FastAPI, session) -> None:
        self.session = session
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable):
        """Log all requests automatically (with http middleware)"""

        request_data = await unpack_request(request)

        # log to console (or file), using loguru
        logger.log("API", "Request at <w>{}</> (ip <m>{}</>)",
                   request_data["path"], request_data["ip"])

        # put all the neccesarry data into database
        request_data["json_body"] = str(request_data["json_body"])
        request_object = ApiRequest(**request_data)
        self.session.add(request_object)
        self.session.commit()

        response: Response = await call_next(request)

        return response
