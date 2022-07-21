from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ..helpers.functions import age_verification
from ..helpers.nsfw import unsave_gif
from ..helpers.utils import reply_id
from . import legend, useless

menu_category = "useless"


@legend.legend_cmd(
    pattern="hpic$",
    command=("hpic", menu_category),
    info={
        "header": "this will send xnxx anime pic",
        "usage": "{tr}hpic",
    },
)
async def hpic(event):
    """this will send xnxx anime pic"""
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Lolis")
            response = await resp
        except YouBlockedUserError:
            return await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐 I Cant Find that")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@legend.legend_cmd(
    pattern="hfutanari$",
    command=("hfutanari", menu_category),
    info={
        "header": "send u sex girl pic anime",
        "usage": "{tr}hfutanari",
    },
)
async def hfuntari(event):
    "send u sex girl pic anime"
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Futanari")
            response = await resp
        except YouBlockedUserError:
            await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            return await event.edit("😐 I Cant Find that")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@legend.legend_cmd(
    pattern="hshota$",
    command=("hshota", menu_category),
    info={
        "header": "sex hentai anime pic",
        "usage": "{tr}hshota",
    },
)
async def hshota(event):
    "sex hentai anime pic"
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Shota")
            response = await resp
        except YouBlockedUserError:
            return await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@legend.legend_cmd(
    pattern="hvideo$",
    command=("hvideo ", menu_category),
    info={
        "header": "send u sex hentai anime video",
        "usage": "{tr}hvideo",
    },
)
async def hvideo(event):
    "send u sex hentai anime video"
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Hentai Videos")
            response = await resp
        except YouBlockedUserError:
            return await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@legend.legend_cmd(
    pattern="hoppai$",
    command=("hoppai", menu_category),
    info={
        "header": "send u hentai ghopcha anime",
        "usage": "{tr}hoppai",
    },
)
async def hoppai(event):
    "send u hentai ghopcha anime"
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Oppai")
            response = await resp
        except YouBlockedUserError:
            return await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@legend.legend_cmd(
    pattern="htrap$",
    command=("htrap", menu_category),
    info={
        "header": "sex hentai anime 18+ pic",
        "usage": "{tr}htrap",
    },
)
async def htrap(event):
    "sex hentai anime 18+ pic"
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Trap")
            response = await resp
        except YouBlockedUserError:
            return await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@legend.legend_cmd(
    pattern="hbdsm$",
    command=("hbdsm", menu_category),
    info={
        "header": "send u hentai sex back pela",
        "usage": "{tr}hbdsm",
    },
)
async def hbdsm(event):
    "send u hentai sex back pela"
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "BDSM")
            response = await resp
        except YouBlockedUserError:
            return await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@legend.legend_cmd(
    pattern="hgif$",
    command=("hgif", menu_category),
    info={
        "header": "It will send u hentai gifs anime",
        "usage": "{tr}hgif",
    },
)
async def hgif(event):
    "It will send u hentai gifs anime"
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "GIF Hentai")
            response = await resp
        except YouBlockedUserError:
            return await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)


@legend.legend_cmd(
    pattern="hcosplay$",
    command=("hcosplay", menu_category),
    info={
        "header": "It Will send u hentai anime",
        "usage": "{tr}hcosplay",
    },
)
async def hcosplay(event):
    "It Will send u hentai anime"
    chat = "@LoliHeavenBot"
    await event.edit("```Checking...```")
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    type = await useless.importent(event)
    if type:
        return
    async with event.client.conversation(chat) as conv:
        try:
            resp = conv.wait_event(
                events.NewMessage(incoming=True, from_users=986872829)
            )
            await event.client.send_message(chat, "Cosplay")
            response = await resp
        except YouBlockedUserError:
            return await event.edit("```Unblock @LoliHeavenBot```")
        if response.text.startswith("I can't find that"):
            await event.edit("😐")
        else:
            await event.delete()
            xxxx = await event.client.send_file(event.chat_id, response.message)
            await unsave_gif(event, xxxx)




#official Hacker 