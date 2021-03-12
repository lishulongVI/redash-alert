from redash_alert.webhook import WebHook


class WechatWorkWebhook(WebHook):

    def __init__(self, access_token):
        super().__init__(webhook='http://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={}'.format(access_token))
