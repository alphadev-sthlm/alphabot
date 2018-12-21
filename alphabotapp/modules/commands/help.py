def help_response(switch, **kwargs):
    return {
        'text': '```' + '\n'.join([help_text(key, switch) for key in switch.keys()]) + '```'
    }


def help_text(key, switch):
    return '- ' + key.ljust(15) + switch[key]['description']
