import random
from flask import request

from alphabotapp import app
from alphabotapp.modules.utils.slackhelper import SlackHelper

slackhelper = SlackHelper()


def icebreak(params, **kwargs):
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
        'text': 'Dags för lunch med @' + request.form['user_name'] + ' @' + ' och @'.join(
            [user['name'] for user in buddies])
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
