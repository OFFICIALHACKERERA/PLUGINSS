import asyncio

from telethon import events

from ..helpers.utils import unsavegif
from . import *


@tgbot.on(events.NewMessage(pattern="/spam", func=lambda e: e.sender_id == bot.uid))
async def spam(e):
    usage = "**CMD** :/spam <value> <text>"
    if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
        return await e.reply(usage, parse_mode=None, link_preview=None)
    legend = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    smex = await e.get_reply_message()
    if len(legend) == 2:
        # legendbit
        message = str(legend[1])
        counter = int(legend[0])
        if counter > 100:
            return await e.reply(error, parse_mode=None, link_preview=None)
        await asyncio.wait([e.respond(message) for i in range(counter)])

    elif e.reply_to_msg_id and smex.media:
        counter = int(legend[0])
        if counter > 100:
            return await e.reply(error, parse_mode=None, link_preview=None)
        for _ in range(counter):
            smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
            await unsavegif(e, smex)
    elif e.reply_to_msg_id and smex.text:
        message = smex.text
        counter = int(legend[0])
        if counter > 100:

            return await e.reply(error, parse_mode=None, link_preview=None)
        await asyncio.wait([e.respond(message) for i in range(counter)])
    else:

        await e.reply(usage, parse_mode=None, link_preview=None)



#official Hacker 