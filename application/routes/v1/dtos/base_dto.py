from pydantic import BaseModel, Extra


class BaseDto(BaseModel):

    class Config:
        extra = Extra.forbid
