from datetime import date


def celebrate(**kwargs):
    today = date.today()
    if today.month == 12 and 20 < today.day < 27:
        celebration = ':christmas_tree:'
    elif (today.month == 12 and today.day > 26) or (today.month == 1 and today.day < 5):
        celebration = ':fireworks:'
    else:
        celebration = ':male-office-worker:'

    return {
        'response_type': 'in_channel',
        'text': celebration
    }
