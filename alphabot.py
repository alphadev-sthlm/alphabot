from config import get_env

from flask import Flask
from config.env import app_env
from config import get_env
from modules.routes import register_routes


app = Flask(__name__, instance_relative_config=False)
app.config.from_object(app_env[get_env('APP_ENV')])
app.config.from_pyfile('config/env.py')
app.debug=True

register_routes(app)

if __name__ == '__main__':
    app.run()
