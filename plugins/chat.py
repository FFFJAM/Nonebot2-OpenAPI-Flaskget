from urllib import request,parse
from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import Message

chatact = on_command("cpt", priority=1)
def gptmes(args):
    text = args[1]
    if len(args) > 2:
        for i in range(2, len(args)):
            text = text + args[i]
    msg = str(text)
    url = "http://yourserverhost:5000/api?text=" + parse.quote(msg)
    res = request.urlopen(url)
    content = res.read().decode()
    return content
@chatact.handle()
async def catrepeat(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).split()
    if len(args) < 2 :                                                                  #
        await chatact.finish(message=f"参数量不正确，请按下列格式提问：/cpt <s/t> xxxxx.....")
    if args[1] != 's':
        content=gptmes(args)
        await chatact.send(content.strip())

    if args[1] == 's' :
        content = gptmes(args)
        rely ='[CQ:tts,text=%s]'%(content)
        await chatact.send(Message(rely))
