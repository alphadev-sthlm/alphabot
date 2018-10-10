from slackclient import SlackClient
from config import get_env


class SlackHelper:

    def __init__(self):
        self.slack_token = get_env('SLACK_API_TOKEN')
        self.slack_client = SlackClient(self.slack_token)
        self.slack_channel = get_env('SLACK_CHANNEL')

        print(self.slack_token)
        print(self.slack_channel)

    def post_message(self, msg, recipient):
        return self.slack_client.api_call(
            "chat.postMessage",
            channel=recipient,
            text=msg,
            as_user=True
        )

    def post_message_to_channel(self, msg):
        return self.slack_client.api_call(
            "chat.postMessage",
            channel=self.slack_channel,
            text=msg,
            username='alphabot',
            parse='full',
            as_user=False
        )

    def file_upload(self, file_content, file_name, file_type, title=None, ):
        return self.slack_client.api_call(
            "files.upload",
            channels=self.slack_channel,
            content=file_content,
            filename=file_name,
            filetype=file_type,
            initial_comment='{} Log File'.format(file_name),
            title=title
        )

    def user_info(self, uid):
        return self.slack_client.api_call(
            "users.info",
            user=uid,
            token=self.slack_token
        )

    def user_list(self):
        return self.slack_client.api_call("users.list")
