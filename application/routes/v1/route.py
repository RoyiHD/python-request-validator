from datetime import datetime
from flask import Flask, jsonify

from application.decorators import request_dto, response_dto
from application.routes.v1.dtos import FooRequest, FooResponse


def add_foo_route(app: Flask) -> None:

    @app.route('/api/v1/foo', methods = ['POST'])
    @request_dto(FooRequest)
    @response_dto(FooResponse)
    def create_foo(request_dto: FooRequest) -> FooResponse:

        # Process request ...

        return FooResponse(
            message = "Request processed successfuly",
        )
