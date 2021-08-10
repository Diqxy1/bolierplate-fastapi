from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import sentry_sdk

from src.shared.exceptions import (
    NotFoundException,
    BadRequestException
)

def init_app(app: FastAPI):

    @app.exception_handler(NotFoundException)
    def not_found_error(request: Request, error: NotFoundException):
        sentry_sdk.capture_exception(error)
        return JSONResponse(
            status_code=error.status_code,
            content={
                "response": error.status_code,
                "data": error.to_dict(),
                "message": error.message
            }
        )

    @app.exception_handler(BadRequestException)
    def bad_request_error(request: Request, error: BadRequestException):
        sentry_sdk.capture_exception(error)
        return JSONResponse(
            status_code=error.status_code,
            content={
                "response": error.status_code,
                "data": error.to_dict(),
                "message": error.message
            }
        )
