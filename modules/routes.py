import random
from flask import jsonify, request
from modules.commands.celebrate import celebrate
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

    @app.route('/help', methods=['POST'])
    def slash():
        payload = {
            'response_type': 'in_channel',
            'text': '''
            > /alphabot icebreak
            '''
        }
        return jsonify(payload)

    @app.route("/alphabot", methods=["POST"])
    def client():
        app.logger.info(request.form)
        args = request.form['text'].split()
        handler = command(args[0])
        payload = handler(args[1:])
        return jsonify(payload)

        # slackhelper.post_message(message, '#hackathon')
        # slackhelper.post_message_to_channel('2- Test post to channel successful!')

    def command(arg):
        switch = {
            'eko': eko,
            'celebrate': celebrate,
            'icebreak': icebreak
        }

        fn = switch.get(arg)
        if fn == None:
            return lambda *v: {'text': arg + ' is not valid command'}
        return fn

    def eko(params):
        return {
            'response_type': 'in_channel',
            'text': ' '.join(params)
        }

    def icebreak(params):
        users = slackhelper.user_list()
        app.logger.info(users['members'])
        number_of_companions = get_size(params[0]) - 1
        friends = [user for user in users['members']
                   if user['name'] != request.form['user_name']
                   and not user['deleted']
                   and not user['is_bot']
                   and user['name'] != 'slackbot']
        buddies = []
        for i in range(0, number_of_companions):
            buddies.append(random.choice(friends))
        payload = {
            'response_type': 'in_channel',
            'text': 'Dags för lunch med @' + request.form['user_name'] + ' @'+ ' och @'.join([user['name'] for user in buddies])
        }
        return payload

    def get_size(number):
        '''
        :param number:string
        :return: number or 2
        '''
        try:
            return int(number)
        except ValueError:
            return 2
