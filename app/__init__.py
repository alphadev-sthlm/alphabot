from flask import Flask, request, jsonify
from config.env import app_env
from app.utils.slackhelper import SlackHelper


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(app_env[config_name])
    app.config.from_pyfile('../config/env.py')
    slackhelper = SlackHelper()

    @app.route("/", methods=["GET"])
    def home():
        # slackhelper.post_message('Test post to channel successful!', 'hackathon')
        # slackhelper.post_message_to_channel('Test post to channel successful!')
        return 'Alphabot running in ' + config_name

    @app.route('/slash', methods=['POST'])
    def slash():
        payload = {
            'response_type': 'in_channel',
            'text': 'Test response successful!'
        }
        return jsonify(payload)

    return app
