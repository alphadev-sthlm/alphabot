from flask import jsonify
from config import get_env
from modules.utils.slackhelper import SlackHelper

slackhelper = SlackHelper()


def register_routes(app):
    @app.route("/", methods=["GET"])
    def home():
        return 'Alphabot running in ' + get_env('APP_ENV')

    @app.route("/config", methods=["GET"])
    def health():
        return jsonify({
            'env': get_env('APP_ENV'),
            'channel': get_env('SLACK_CHANNEL')
        })

    @app.route("/users", methods=["GET"])
    def users():
        user_list = slackhelper.user_list()
        users = []
        for user in user_list['members']:
            if not user['deleted'] and not user['is_bot'] and user['name'] != 'slackbot':
                users.append(user['profile']['real_name'])
        return jsonify(users)

    @app.route('/slash', methods=['POST'])
    def slash():
        payload = {
            'response_type': 'in_channel',
            'text': 'Test response successful!'
        }
        return jsonify(payload)

    @app.route("/client", methods=["POST"])
    def client():
        slackhelper.post_message('1- Test post to channel successful!', '#hackathon')
        slackhelper.post_message_to_channel('2- Test post to channel successful!')
        return 'OK'
