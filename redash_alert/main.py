import json
from enum import Enum

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from starlette.responses import JSONResponse
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_500_INTERNAL_SERVER_ERROR

from redash_alert.dingding_webhook import DingDingWebhook
from redash_alert.feishu_webhook import FeishuWorkWebhook
from redash_alert.wechat_webhook import WechatWorkWebhook

tags_metadata = [
    {
        "name": "Readme",
        'description': """### zh

1. redash所支持的webhooks 并不支持钉钉，企业微信机器人通知方式
2. 通过redash支持的webhooks方式，曲线支持钉钉，企业微信
3. redash webhook 实现通知代码：[Redash Webhook](https://github.com/getredash/redash/blob/d0793c4ba8b28fcd0c40dd91453f8b5e19f9eb2d/redash/destinations/webhook.py#L28)
4. 这个项目通过符合redash webhook方式构建 webhook api，然后再进行路由转发给钉钉或者企业微信
"""
    }
]

app = FastAPI(
    title='RedashAlert',
    version='0.1.0',
    openapi_tags=tags_metadata
)

security = HTTPBasic()


class WayEnum(str, Enum):
    """
    """
    WEI_XIN = 'weixin'
    DING_DING = 'dingding'
    FEI_SHU = 'feishu'


@app.post('/webhook/{send_way}/{token}/', include_in_schema=True)
async def webhook(
        send_way: WayEnum,
        request: Request,
        credentials: HTTPBasicCredentials = Depends(security),

        token=None,
):
    if credentials.username != "redash" or credentials.password != "redash_2021":
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    else:
        try:
            bean = await request.json()
            description = bean['alert']['description']
            data = json.loads(description)
            if send_way == WayEnum.DING_DING:
                DingDingWebhook(access_token=token).send(_json=data)
            elif send_way == WayEnum.FEI_SHU:
                FeishuWorkWebhook(access_token=token).send(_json=data)
            else:
                WechatWorkWebhook(access_token=token).send(_json=data)
        except Exception as e:
            return JSONResponse(content={
                'status': 'fail',
                'error_msg': str(e)
            }, status_code=HTTP_500_INTERNAL_SERVER_ERROR)
        return {
            'status': 'success'
        }


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=9998, debug=True)
