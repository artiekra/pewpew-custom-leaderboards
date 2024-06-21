"""FastAPI Middleware - applied for each request
https://medium.com/@dhavalsavalia/fastapi-logging-middleware- \
logging-requests-and-responses-with-ease-and-style-201b9aa4001a"""

from typing import Callable
from uuid import uuid4

from loguru import logger

from fastapi import FastAPI
from fastapi import Request, Response  # for typing
from starlette.middleware.base import BaseHTTPMiddleware

from api.middleware.helpers import unpack_request, unpack_response

from database.table import ApiRequest, ApiResponse

logger = logger.opt(colors=True)


class LoggingMiddleware(BaseHTTPMiddleware):

    def __init__(self, app: FastAPI, session) -> None:
        self.session = session
        super().__init__(app)

    async def set_body(self, request):
        """Allows to get resonse body from the request"""

        receive_ = await request._receive()

        async def receive():
            return receive_

        request._receive = receive

    async def dispatch(self, request: Request, call_next: Callable):
        """Log all requests automatically (with http middleware)"""

        request_id = str(uuid4())

        # [NOTE: awaiting set_body - doesn't work!]
        if request.method == 'POST':
            self.set_body(request)

        request_data = await unpack_request(request)
        response, response_data = await unpack_response(call_next, request,
                                                        request_id)

        response_data_json = response_data["json_body"]
        if len(response_data_json) <= 50:
            short_response_data = response_data_json
        else:
            short_response_data = response_data_json[:50]

        # log to console (or file), using loguru
        logger.log("API", "Request at <w>{}</> with id <m>{}</> (ip <m>{}</>)",
                   request_data["path"], request_id, request_data["ip"])
        logger.log("API", "Got response to request <m>{}</> (<w>{}</>...)",
                   request_id, short_response_data)

        # put all the neccesarry data into database

        request_data["json_body"] = str(request_data["json_body"])
        request_object = ApiRequest(request_id=request_id, **request_data)
        self.session.add(request_object)

        response_data["json_body"] = str(response_data["json_body"])
        response_object = ApiResponse(request_id=request_id, **response_data)
        self.session.add(response_object)

        self.session.commit()

        return response
