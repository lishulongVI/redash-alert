from redash_alert.webhook import WebHook


class DingDingWebhook(WebHook):

    def __init__(self, access_token):
        super().__init__(webhook='https://oapi.dingtalk.com/robot/send?access_token={}'.format(access_token))
