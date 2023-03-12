import os

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

dir_path = os.path.dirname(os.path.realpath(__file__))
root_dir = dir_path[:-3]
config = Config(f'{root_dir}.env')

#DATABASE_URL = f'postgresql+psycopg2://app:123qwe@127.0.0.1:5432/fastapi_app.db'
DATABASE_URL = f'postgresql://app:123qwe@127.0.0.1:5432/' + config('DB_NAME', cast=str)


SECRET_KEY = config('SECRET_KEY', cast=Secret)