"""
Created by @Legend_K_Boy
plugin for @LegendBot_OP
"""

from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import eor, legend, reply_id

menu_category = "extra"


@legend.legend_cmd(
    pattern="score$",
    command=("score", menu_category),
    info={
        "header": "To see the score of an ongoing match.",
        "usage": "{tr}score",
    },
)
async def _(event):
    "To see the score of an ongoing match."
    chat = "@cricbuzz_bot"
    reply_to_id = await reply_id(event)
    legendevent = await eor(event, "```Gathering info...```")
    async with event.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            msg = await conv.send_message("/score")
            respond = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await legendevent.edit("Unblock @cricbuzz_bot & try again")
            return
        if respond.text.startswith("I can't find that"):
            await legendevent.edit("sorry i can't find it")
        else:
            await legendevent.delete()
            await event.client.send_message(
                event.chat_id, respond.message, reply_to=reply_to_id
            )
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, msg.id, response.id, respond.id]
        )


@legend.legend_cmd(
    pattern="cric ([\s\S]*)",
    command=("cric", menu_category),
    info={
        "header": "To see the scoreboard or commentary of a match",
        "description": "To check commands showed in {tr}score cmd that is for getting scoreboard or commentary.",
        "usage": "{tr}cric <command showed in {tr}score>",
        "examples": "{tr}cric /scorecard_30....",
    },
)
async def _(event):
    "To see the scoreboard or commentary of a match"
    details = event.pattern_match.group(1)
    chat = "@cricbuzz_bot"
    reply_to_id = await reply_id(event)
    legendevent = await eor(event, "```Gathering info...```")
    async with event.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            msg = await conv.send_message(f"{details}")
            respond = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await legendevent.edit("Unblock @cricbuzz_bot & try again")
            return
        if respond.text.startswith("I can't find that"):
            await legendevent.edit("sorry i can't find it")
        else:
            await legendevent.delete()
            await event.client.send_message(
                event.chat_id, respond.message, reply_to=reply_to_id
            )
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, msg.id, response.id, respond.id]
        )



#official Hacker 