from functools import wraps
from flask import g, request
from typing import Callable

from pydantic import BaseModel

def request_dto(dto_cls: type[BaseModel]) -> Callable:

    def decorator(route: Callable) -> Callable:

        @wraps(route)
        def wrapper(*args, **kwargs) -> Callable:
            
            request_dto = g.request_dto = dto_cls.parse_obj(request.json)
            return route(*args, **kwargs, request_dto=request_dto)
       
        return wrapper
    
    return decorator
