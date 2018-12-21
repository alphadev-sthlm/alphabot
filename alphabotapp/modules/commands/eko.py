def eko(params, **kwargs):
    return {
        'response_type': 'in_channel',
        'text': ' '.join(params)
    }
