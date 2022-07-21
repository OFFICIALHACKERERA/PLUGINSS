import random
from os import remove
from random import choice
from urllib import parse

import requests
from telethon import functions, types, utils

from userbot import legend

from ..helpers import reply_id

menu_category = "extra"

BASE_URL = "https://headp.at/pats/{}"
PAT_IMAGE = "pat.webp"

# credit to @r4v4n4


@legend.legend_cmd(
    pattern="dab$",
    command=("dab", menu_category),
    info={
        "header": "To get random dabbing pose stickers.",
        "usage": "{tr}dab",
    },
)
async def dab(event):
    "To get random dabbing pose stickers."
    reply_to_id = await reply_id(event)
    blacklist = {
        1653974154589768377,
        1653974154589768312,
        1653974154589767857,
        1653974154589768311,
        1653974154589767816,
        1653974154589767939,
        1653974154589767944,
        1653974154589767912,
        1653974154589767911,
        1653974154589767910,
        1653974154589767909,
        1653974154589767863,
        1653974154589767852,
        1653974154589768677,
    }
    await event.delete()
    docs = [
        utils.get_input_document(x)
        for x in (
            await event.client(
                functions.messages.GetStickerSetRequest(
                    types.InputStickerSetShortName("DabOnHaters")
                ),
                hash=0,
            )
        ).documents
        if x.id not in blacklist
    ]
    await event.respond(file=random.choice(docs), reply_to=reply_to_id)


@legend.legend_cmd(
    pattern="brain$",
    command=("brain", menu_category),
    info={
        "header": "To get random brain stickers.",
        "usage": "{tr}brain",
    },
)
async def handler(event):
    "To get random brain stickers."
    reply_to_id = await reply_id(event)
    blacklist = {}
    await event.delete()
    docs = [
        utils.get_input_document(x)
        for x in (
            await event.client(
                functions.messages.GetStickerSetRequest(
                    types.InputStickerSetShortName("supermind")
                ),
                hash=0,
            )
        ).documents
        if x.id not in blacklist
    ]
    await event.respond(file=random.choice(docs), reply_to=reply_to_id)


# HeadPat Module for Userbot (http://headp.at)
# cmd:- .pat username or reply to msg
# By:- git: jaskaranSM tg: @Zero_cool7870


@legend.legend_cmd(
    pattern="pat$",
    command=("pat", menu_category),
    info={
        "header": "To get random pat stickers.",
        "usage": "{tr}pat",
    },
)
async def lastfm(event):
    "To get random pat stickers."
    await event.delete()
    reply_to_id = await reply_id(event)
    resp = requests.get("http://headp.at/js/pats.json")
    pats = resp.json()
    pat = BASE_URL.format(parse.quote(choice(pats)))
    with open(PAT_IMAGE, "wb") as f:
        f.write(requests.get(pat).content)
    await event.client.send_file(event.chat_id, PAT_IMAGE, reply_to=reply_to_id)
    remove(PAT_IMAGE)
