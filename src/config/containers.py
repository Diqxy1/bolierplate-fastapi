from dependency_injector import containers, providers
from decouple import config as configEnv

from src.config.database import Database

from src.infra.containers import UserContainer

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    db = providers.Singleton(
        Database, db_url=configEnv('CLEARDB_DATABASE_URL')
    )

    user_contaier = providers.Container(UserContainer, db=db)


def init_app() -> Container:
    return Container()
