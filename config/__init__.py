import os
import dotenv
from os import path, environ

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)


def get_env(key):
    return environ.get(key)


def get_env_default(key, default):
    return os.getenv(key, default)
