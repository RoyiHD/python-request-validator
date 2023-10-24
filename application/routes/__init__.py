from flask import Flask

from application.routes.v1 import add_foo_route

def add_routes(app: Flask) -> None:

    add_foo_route(app)


__all__ = [
    "add_routes",
]
