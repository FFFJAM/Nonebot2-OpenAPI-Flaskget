from urllib import request,parse
from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event


chatact = on_command("cpt", priority=1)


@chatact.handle()
async def catrepeat(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).split()
    if len(args) != 2:                                                                  #
        await chatact.finish(message=f"请按下列格式提问：/cpt xxxxx.....")
    else:
        name =event.get_user_id()
        text =args[1]
        msg = str(text)
        url = "http://serverhost:5000/api?text=" + parse.quote(msg)
        res = request.urlopen(url)
        content = res.read().decode()
        await chatact.send(content.strip())
