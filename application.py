from fastapi import FastAPI

from src.config import routes

app = FastAPI()

routes.init_app(app)
