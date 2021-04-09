from redash_alert.webhook import WebHook


class FeishuWorkWebhook(WebHook):

    def __init__(self, access_token):
        super().__init__(webhook='https://open.feishu.cn/open-apis/bot/v2/hook/{}'.format(access_token))
