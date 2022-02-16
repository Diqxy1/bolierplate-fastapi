from typer import Typer
from src.infra.cli import teste

def init_app(app: Typer):
    app.add_typer(teste.app, name='teste')