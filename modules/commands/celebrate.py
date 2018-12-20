from datetime import date


def celebrate(params):
    today = date.today()
    if today.month == 12 and today.day > 20 and today.day < 27:
        celebration = ':christmas_tree:'
    elif (today.month == 12 and today.day > 26) or (today.month == 1 and today.day < 5):
        celebration = ':fireworks:'
    else:
        celebration = ':male-office-worker:'

    return {
        'response_type': 'in_channel',
        'text': celebration
    }
