# redash-alert
> redash 支持钉钉，企业微信机器人通知

[![HitCount](http://hits.dwyl.com/lishulongVI/redash-alert.svg)](http://hits.dwyl.com/lishulongVI/redash-alert)

### zh

1. redash所支持的webhooks 并不支持钉钉，企业微信机器人通知方式
2. 通过redash支持的webhooks方式，曲线支持钉钉，企业微信
3. redash webhook 实现通知代码：[Redash Webhook](https://github.com/getredash/redash/blob/d0793c4ba8b28fcd0c40dd91453f8b5e19f9eb2d/redash/destinations/webhook.py#L28)
4. 这个项目通过符合redash webhook方式构建 webhook api，然后再进行路由转发给钉钉或者企业微信



### En

1. the webhooks supported by redash do not support the nailing and enterprise weibo bot notification method
2. the webhooks supported by redash support the curve support nails, enterprise WeChat
3. redash webhook implementation notification code: [Redash Webhook](https://github.com/getredash/redash/blob/d0793c4ba8b28fcd0c40dd91453f8b5e19f9eb2d/redash /destinations/webhook.py#L28)
4. This project builds the webhook api by conforming to the redash webhook method, and then routes it to nail or enterprise WeChat
