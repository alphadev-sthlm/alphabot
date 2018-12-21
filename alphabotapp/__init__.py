from flask import Flask
from alphabotapp.config.env import app_env
from alphabotapp.config import get_env
from alphabotapp.modules.routes import register_routes


app = Flask(__name__, instance_relative_config=False)
app.config.from_object(app_env[get_env('APP_ENV')])
app.config.from_pyfile('config/env.py')
app.debug=True

register_routes(app)


