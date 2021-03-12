import requests


class WebHook:
    session = requests.session()

    def __init__(self, webhook):
        self.webhook = webhook

    def send(self, _json):
        res = self.session.post(url=self.webhook, json=_json)
        if res.status_code != 200:
            raise Exception(f'url:{self.webhook},json:{_json},res_text:{res.text}')
        return True
