# created by @Legend_K_Boy
# LegendUserBot

import os
import urllib

from userbot import legend

from ..helpers.functions import (
    clippy,
    convert_tosticker,
    higlighted_text,
    soft_deEmojify,
)
from ..helpers.utils import reply_id
from . import eod, legend

menu_category = "useless"


def file_checker(template):
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    tempname = "./temp/cat_temp.png"
    fontname = "./temp/ArialUnicodeMS.ttf"
    urllib.request.urlretrieve(template, tempname)
    if not os.path.exists(fontname):
        urllib.request.urlretrieve(
            "https://github.com/ITS-LEGENDBOT/RESOURCES/blob/master/Spotify/ArialUnicodeMS.ttf?raw=true",
            fontname,
        )
    return tempname, fontname


@legend.legend_cmd(
    pattern="(|b)quby(?:\s|$)([\s\S]*)",
    command=("quby", menu_category),
    info={
        "header": "Make doge say anything.",
        "flags": {
            "b": "Give the sticker on background.",
        },
        "usage": [
            "{tr}quby <text/reply to msg>",
            "{tr}bquby <text/reply to msg>",
        ],
        "examples": [
            "{tr}quby Gib money",
            "{tr}bquby Gib money",
        ],
    },
)
async def quby(event):
    "Make a cool quby text sticker"
    cmd = event.pattern_match.group(1).lower()
    text = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    if not text and event.is_reply:
        text = (await event.get_reply_message()).message
    if not text:
        return await eod(event, "__What is quby supposed to say? Give some text.__")
    await eod(event, "`Wait, processing.....`")
    temp_name, fontname = file_checker(
        "https://telegra.ph/file/09f4df5a129758a2e1c9c.jpg"
    )
    lines = 3
    text = soft_deEmojify(text)
    if len(text) < 80:
        font = 60
        wrap = 1.3
        position = (45, 0)
    else:
        font = 50
        wrap = 1
        position = (-70, 0)
    file, txt = higlighted_text(
        temp_name,
        text,
        text_wrap=wrap,
        font_name=fontname,
        font_size=font,
        linespace="+2",
        position=position,
        lines=lines,
        album=True,
        album_limit=1,
        stroke_width=1,
    )
    if len(txt) >= lines:
        for x in range(0, lines):
            text = text.replace(txt[x], "")
        file, _ = higlighted_text(
            file[0],
            text,
            text_wrap=wrap,
            font_name=fontname,
            font_size=font,
            linespace="+2",
            position=position,
            direction="upwards",
            lines=1,
            album=True,
            album_limit=1,
            stroke_width=1,
        )
    if cmd == "b":
        owo = convert_tosticker(file[0])
        await event.client.send_file(
            event.chat_id, owo, reply_to=reply_to_id, force_document=False
        )
    else:
        await clippy(event.client, file[0], event.chat_id, reply_to_id)
    await event.delete()
    for files in (temp_name, file[0]):
        if files and os.path.exists(files):
            os.remove(files)


@legend.legend_cmd(
    pattern="(|b)(blob|kirby)(?:\s|$)([\s\S]*)",
    command=("blob", menu_category),
    info={
        "header": "Give the sticker on background.",
        "flags": {
            "b": "To create knife sticker transparent.",
        },
        "usage": [
            "{tr}blob <text/reply to msg>",
            "{tr}bblob <text/reply to msg>",
        ],
        "examples": [
            "{tr}blob Gib money",
            "{tr}bblob Gib money",
        ],
    },
)
async def knife(event):
    "Make a blob knife text sticker"
    cmd = event.pattern_match.group(1).lower()
    text = event.pattern_match.group(3)
    reply_to_id = await reply_id(event)
    if not text and event.is_reply:
        text = (await event.get_reply_message()).message
    if not text:
        return await eod(event, "__What is blob supposed to say? Give some text.__")
    await eod(event, "`Wait, processing.....`")
    temp_name, fontname = file_checker(
        "https://telegra.ph/file/2188367c8c5f43c36aa59.jpg"
    )
    text = soft_deEmojify(text)
    if len(text) < 50:
        font = 90
        wrap = 2
        position = (250, -450)
    else:
        font = 60
        wrap = 1.4
        position = (150, 500)
    file, _ = higlighted_text(
        temp_name,
        text,
        text_wrap=wrap,
        font_name=fontname,
        font_size=font,
        linespace="-5",
        position=position,
        direction="upwards",
    )
    if cmd == "b":
        owo = convert_tosticker(file[0])
        await event.client.send_file(
            event.chat_id, owo, reply_to=reply_to_id, force_document=False
        )
    else:
        await clippy(event.client, file[0], event.chat_id, reply_to_id)
    await event.delete()
    for files in (temp_name, file[0]):
        if files and os.path.exists(files):
            os.remove(files)


@legend.legend_cmd(
    pattern="(|h)doge(?:\s|$)([\s\S]*)",
    command=("doge", menu_category),
    info={
        "header": "Make doge say anything.",
        "flags": {
            "h": "To create doge sticker with highligted text.",
        },
        "usage": [
            "{tr}doge <text/reply to msg>",
            "{tr}hdoge <text/reply to msg>",
        ],
        "examples": [
            "{tr}dogge Gib money",
            "{tr}hdogge Gib money",
        ],
    },
)
async def doggy(event):
    "Make a cool doggy text sticker"
    event.pattern_match.group(1).lower()
    text = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    if not text and event.is_reply:
        text = (await event.get_reply_message()).message
    if not text:
        return await eod(event, "__What is doge supposed to say? Give some text.__")
    await eod(event, "`Wait, processing.....`")
    text = soft_deEmojify(text)
    temp_name, fontname = file_checker(
        "https://telegra.ph/file/6f621b9782d9c925bd6c4.jpg"
    )
    font, wrap, lines, ls = (
        (90, 1.9, 5, "-75") if len(text) < 140 else (70, 1.3, 6, "-55")
    )
    file, txt = higlighted_text(
        temp_name,
        text,
        text_wrap=wrap,
        font_name=fontname,
        font_size=font,
        linespace=ls,
        position=(-20, 0),
        align="left",
        background="white",
        foreground="black",
        transparency=0,
        lines=lines,
        album=True,
        album_limit=1,
        stroke_width=1,
        stroke_fill="black",
    )
    if len(txt) >= lines:
        for x in range(0, lines):
            text = text.replace(txt[x], "")
        file, _ = higlighted_text(
            file[0],
            text,
            text_wrap=wrap + 2,
            font_name=fontname,
            font_size=font,
            linespace=ls,
            position=(-20, 480),
            align="left",
            background="white",
            foreground="black",
            transparency=0,
            lines=lines,
            album=True,
            album_limit=1,
            stroke_width=1,
            stroke_fill="black",
        )
    owo = convert_tosticker(file[0])
    await event.client.send_file(
        event.chat_id, owo, reply_to=reply_to_id, force_document=False
    )
    await event.delete()
    for files in (temp_name, file[0]):
        if files and os.path.exists(files):
            os.remove(files)


# by Yato
@legend.legend_cmd(
    pattern="(|h)penguin(?:\s|$)([\s\S]*)",
    command=("penguin", menu_category),
    info={
        "header": "To make penguin meme sticker. ",
        "flags": {
            "h": "To create penguin sticker with highligted text.",
        },
        "usage": [
            "{tr}penguin <text/reply to msg>",
            "{tr}hpenguin <text/reply to msg>",
        ],
        "examples": [
            "{tr}penguin Shut up Rash",
            "{tr}hpenguin Shut up Rash",
        ],
    },
)
async def penguin(event):
    "Make a cool penguin text sticker"
    cmd = event.pattern_match.group(1).lower()
    text = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    if not text and event.is_reply:
        text = (await event.get_reply_message()).message
    if not text:
        return await eod(event, "What is penguin supposed to say? Give some text.")
    await eod(event, "Wait, processing.....")
    temp_name, fontname = file_checker(
        "https://telegra.ph/file/ee1fc91bbaef2cc808c7c.png"
    )
    text = soft_deEmojify(text)
    font, wrap, lines = (90, 4, 5) if len(text) < 50 else (70, 4.5, 7)
    bg, fg, alpha, ls, lines = (
        ("black", "white", 255, "-30", lines - 2)
        if cmd == "h"
        else ("white", "black", 0, "-60", lines)
    )
    file, _ = higlighted_text(
        temp_name,
        text,
        text_wrap=wrap,
        font_name=fontname,
        font_size=font,
        linespace=ls,
        position=(0, 10),
        align="left",
        background=bg,
        foreground=fg,
        transparency=alpha,
        lines=lines,
        album=True,
        album_limit=1,
        stroke_width=1,
        stroke_fill=fg,
    )
    owo = convert_tosticker(file[0])
    await event.client.send_file(
        event.chat_id, owo, reply_to=reply_to_id, force_document=False
    )
    await event.delete()
    for files in (temp_name, file[0]):
        if files and os.path.exists(files):
            os.remove(files)


@legend.legend_cmd(
    pattern="(|h)gandhi(?:\s|$)([\s\S]*)",
    command=("gandhi", menu_category),
    info={
        "header": "Make gandhi text sticker.",
        "flags": {
            "h": "To create gandhi sticker with highligted text.",
        },
        "usage": [
            "{tr}gandhi <text/reply to msg>",
            "{tr}hgandhi <text/reply to msg>",
        ],
        "examples": [
            "{tr}gandhi Nathu Killed me",
            "{tr}hgandhi Nathu Killed me",
        ],
    },
)
async def gandhi(event):
    "Make a cool gandhi text sticker"
    cmd = event.pattern_match.group(1).lower()
    text = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    if not text and event.is_reply:
        text = (await event.get_reply_message()).message
    if not text:
        return await eod(event, "What is gandhi supposed to write? Give some text.")
    await eod(event, "Wait, processing.....")
    temp_name, fontname = file_checker(
        "https://telegra.ph/file/3bebc56ee82cce4f300ce.jpg"
    )
    text = soft_deEmojify(text)
    font, wrap, lines = (90, 3, 5) if len(text) < 75 else (70, 2.8, 7)
    bg, fg, alpha, ls, lines = (
        ("white", "black", 255, "-30", lines - 1)
        if cmd == "h"
        else ("black", "white", 0, "-60", lines)
    )
    file, _ = higlighted_text(
        temp_name,
        text,
        text_wrap=wrap,
        font_name=fontname,
        font_size=font,
        linespace=ls,
        position=(470, 10),
        align="center",
        background=bg,
        foreground=fg,
        transparency=alpha,
        lines=lines,
        album=True,
        album_limit=1,
        stroke_width=1,
        stroke_fill=fg,
    )
    owo = convert_tosticker(file[0])
    await event.client.send_file(
        event.chat_id, owo, reply_to=reply_to_id, force_document=False
    )
    await event.delete()
    for files in (temp_name, file[0]):
        if files and os.path.exists(files):
            os.remove(files)
