import asyncio

from ..helpers.utils import unsavegif
from . import *


@legend.bot_cmd(pattern="/delayspam", func=lambda e: e.sender_id == bot.uid)
async def delayspam(e):
    usage = "**CMD :**/delayspam <value> <time> <text>"
    if Config.SPAM == "ON":
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        legendboy = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        legendgirl = legendboy[1:]
        if len(legendgirl) == 2:
            message = str(legendgirl[1])
            counter = int(legendgirl[0])
            sleeptime = float(legendboy[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(legendgirl[0])
            sleeptime = float(legendboy[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await unsavegif(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(legendgirl[0])
            sleeptime = float(legendboy[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)
