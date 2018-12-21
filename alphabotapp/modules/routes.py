import random
from flask import jsonify, request
from alphabotapp.config import get_env
from alphabotapp.modules.utils.slackhelper import SlackHelper
slackhelper = SlackHelper()


def register_routes(app):
    from alphabotapp.modules.commands.eko import eko
    from alphabotapp.modules.commands.celebrate import celebrate
    from alphabotapp.modules.commands.icebreak import icebreak
    from alphabotapp.modules.commands.help import help_response

    switch = {
        'help': {
            'description': 'List all commands',
            'handler': help_response},
        'eko': {
            'description': 'Make alphabot behave like a härmapa',
            'handler': eko},
        'celebrate': {
            'description': 'Celebrate the time of year',
            'handler': celebrate},
        'icebreak': {
            'description': 'Break the ice with a lunch. Arg 1: number of lunch participants',
            'handler': icebreak},
    }

    @app.route("/", methods=["GET"])
    def home():
        return 'Alphabot running in ' + get_env('APP_ENV')

    @app.route("/config", methods=["GET"])
    def health():
        return jsonify({
            'env': get_env('APP_ENV'),
            'channel': get_env('SLACK_CHANNEL')
        })

    @app.route("/users", methods=["POST"])
    def users():
        user_list = slackhelper.user_list()
        users_list = []
        for user in user_list['members']:
            if not user['deleted'] and not user['is_bot'] and user['name'] != 'slackbot':
                users_list.append(user['profile']['real_name'].decode('unicode-escape'))
        return jsonify(users_list)

    @app.route('/help', methods=['POST'])
    def list_help():
        return jsonify(help_response(switch))

    @app.route("/alphabot", methods=["POST"])
    def alphabot():
        app.logger.info(request.form)
        args = request.form['text'].split()
        command_string = 'help' if len(args) == 0 else args[0]
        handler = get_command(command_string)
        params = args[1:] if len(args) > 1 else []
        payload = handler(params=params, switch=switch)
        return jsonify(payload)

        # slackhelper.post_message(message, '#hackathon')
        # slackhelper.post_message_to_channel('2- Test post to channel successful!')

    def get_command(arg):
        fn = switch.get(arg)
        if fn is None:
            return lambda *v: {'text': arg + ' is not valid command'}
        return fn['handler']
