from telethon import events
from Deepak import legend
from Deepak.helpers.queues import (
    QUEUE,
    add_to_queue,
    clear_queue,
    get_queue,
    pop_an_item,
)








#end
@legend.bot_cmd(events.NewMessage(pattern="^[/?!]end"))
async def vc_end(event, perm):
    chat_id = event.chat_id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await event.reply("**Streaming Ended**")
        except Exception as e:
            await event.reply(f"**ERROR:** `{e}`")
    else:
        await event.reply("**Ntg is Streaming**")

