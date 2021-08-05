from fastapi import FastAPI

from src.routes import users

def init_app(app: FastAPI):
    app.include_router(users.router)