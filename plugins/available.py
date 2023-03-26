from nonebot.plugin import on_keyword
from urllib import request
import json
jrrp = on_keyword(['/账户余额'], priority=50)

@jrrp.handle()
async def jrrp_handle(matcher):
    url = "http://serverhost:5000/api?text=QWEQWEQWEQWE"
    res = request.urlopen(url)
    content = res.read().decode()
    content = json.loads(content)
    text = "OpenAI账户余额：\n总额度 :\t\t\t%.2f$\n已用额度：\t%.2f$\n剩余额度：\t%.2f$"%(content["total_granted"], content["total_used"],
            content["total_available"])
    await matcher.send(str(text))



