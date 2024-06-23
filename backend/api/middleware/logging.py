"""FastAPI Middleware - applied for each request
https://medium.com/@dhavalsavalia/fastapi-logging-middleware- \
logging-requests-and-responses-with-ease-and-style-201b9aa4001a"""

from typing import Callable
from uuid import uuid4

from loguru import logger

from fastapi import FastAPI
from sqlmodel import Session

from starlette.types import Message
from fastapi import Request, Response  # for typing

from starlette.middleware.base import BaseHTTPMiddleware

from api.middleware.helpers import unpack_request, unpack_response

from database.table import ApiRequest, ApiResponse

logger = logger.opt(colors=True)


# [TODO: better way to handle server error (now response=None)]
class LoggingMiddleware(BaseHTTPMiddleware):

    def __init__(self, app: FastAPI, engine) -> None:
        self.engine = engine
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable):
        """Log all requests automatically (with http middleware)"""

        request_id = str(uuid4())

        request_data = await unpack_request(request)
        response, response_data = await unpack_response(call_next, request,
                                                        request_id)

        # to print in logs, take first 50 chars from response json body
        # (if None, keep None)
        response_data_json = response_data["json_body"]
        if response_data_json is not None:
            if len(response_data_json) <= 50:
                short_response_data = response_data_json
            else:
                short_response_data = response_data_json[:50]
        else:
            short_response_data = None

        # log to console (or file), using loguru
        logger.log("API", "Request at <w>{}</> with id <m>{}</> (ip <m>{}</>)",
                   request_data["path"], request_id, request_data["ip"])
        logger.log("API", "Got response to request <m>{}</> (<w>{}</>...)",
                   request_id, short_response_data)

        # put all the neccesarry data into database
        with Session(self.engine) as session:
            request_data["json_body"] = str(request_data["json_body"])
            request_object = ApiRequest(request_id=request_id, **request_data)
            session.add(request_object)

            response_data["json_body"] = str(response_data["json_body"])
            response_object = ApiResponse(request_id=request_id, **response_data)
            session.add(response_object)

            session.commit()

        return response
