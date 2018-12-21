import os
import dotenv
from os import path, environ

dir = os.path.dirname
dotenv_path = os.path.join(dir(dir(__file__)), '.env')
dotenv.load_dotenv(dotenv_path)


def get_env(key):
    return environ.get(key)


def get_env_default(key, default):
    return os.getenv(key, default)
