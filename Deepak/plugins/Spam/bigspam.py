from Deepak import bot

from . import *


async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass


import asyncio

from telethon import functions, types


@legend.bot_cmd(pattern="/bigspam", func=lambda e: e.sender_id == bot.uid)
async def spam(e):
    if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
        return await e.reply(usage, parse_mode=None, link_preview=None)
    legend = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
    smex = await e.get_reply_message()
    if len(legend) == 2:
        message = str(legend[1])
        counter = int(legend[0])
        for _ in range(counter):
            async with e.client.action(e.chat_id, "typing"):
                if e.reply_to_msg_id:
                    await smex.reply(message)
                else:
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)

    elif e.reply_to_msg_id and smex.media:

        counter = int(legend[0])
        for _ in range(counter):
            async with e.client.action(e.chat_id, "document"):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
            await asyncio.sleep(0.1)
    elif e.reply_to_msg_id and smex.text:
        message = smex.text
        counter = int(legend[0])
        for _ in range(counter):
            async with e.client.action(e.chat_id, "typing"):
                await e.client.send_message(e.chat_id, message)
                await asyncio.sleep(0.1)
    else:

        await e.reply(usage, parse_mode=None, link_preview=None)
