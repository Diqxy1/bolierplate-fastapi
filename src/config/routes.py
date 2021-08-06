from fastapi import FastAPI

from src.infra.routes import users

def get_routes() -> list:
    return [users]

def init_app(app: FastAPI):
    app.include_router(users.router)
