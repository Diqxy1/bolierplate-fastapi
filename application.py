from fastapi import FastAPI

from src.config import containers
from src.config import routes
from src.config import exceptions


def create_app() -> FastAPI:
    container = containers.init_app()
    container.wire(modules=routes.get_routes())
    app = FastAPI()
    routes.init_app(app)
    exceptions.init_app(app)
    app.container = container
    return app

app = create_app()
