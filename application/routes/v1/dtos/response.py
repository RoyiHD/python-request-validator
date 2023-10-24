from datetime import datetime
from pydantic import Field
from application.routes.v1.dtos.base_dto import BaseDto


class FooResponse(BaseDto):

    created_at: datetime = Field(
        alias = "createdAt",
        description = "Request datetime",
        default_factory=datetime.now,
        example = "2023-10-24 13:41:09.702907",
        title = "Created At"
    )
    
    message: str = Field(
        alias = "message",
        description = "response message",
        example = "Successful request and response validation",
        title = "Message"
    )
