from pydantic import Field
from application.routes.v1.dtos.base_dto import BaseDto


class User(BaseDto):

    name: str = Field(
        alias = "name",
        description = "name of the user",
        example = "John doe",
        title = "Name"
    )


class FooRequest(BaseDto):

    user: User
