# by @LEGEND_K_BOY (@LEGEND_K_BOY)
import io
import os
from io import BytesIO

import requests
from PIL import Image, ImageFilter, ImageOps
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto

from userbot import legend

from ..core.managers import eod, eor
from ..helpers import media_type
from ..helpers.functions import dotify
from ..helpers.utils import _legendtools

menu_category = "fun"


@legend.legend_cmd(
    pattern="imirror(s)? ?(-)?(l|r|u|b)?$",
    command=("imirror", menu_category),
    info={
        "header": "gives to reflected  image of one part on other part.",
        "description": "Additionaly use along with cmd i.e, imirrors to gib out put as sticker.",
        "flags": {
            "-l": "Right half will be reflection of left half.",
            "-r": "Left half will be reflection of right half.",
            "-u": "bottom half will be reflection of upper half.",
            "-b": "upper half will be reflection of bottom half.",
        },
        "usage": [
            "{tr}imirror <type> - gives output as image",
            "{tr}imirrors <type> - gives output as sticker",
        ],
        "examples": [
            "{tr}imirror -l",
            "{tr}imirrors -u",
        ],
    },
)
async def imirror(event):  # sourcery no-metrics
    "imgae refelection fun."
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo", "Sticker"]:
        return await eod(event, "__Reply to photo or sticker to make mirror.__")
    legendevent = await event.edit("__Reflecting the image....__")
    args = event.pattern_match.group(1)
    if args:
        filename = "LegendUserBot.webp"
        f_format = "webp"
    else:
        filename = "LegendUserBot.jpg"
        f_format = "jpeg"
    try:
        imag = await _legendtools.media_to_pic(legendevent, reply, noedits=True)
        if imag[1] is None:
            return await eod(
                imag[0], "__Unable to extract image from the replied message.__"
            )
        image = Image.open(imag[1])
    except Exception as e:
        return await eod(legendevent, f"**Error in identifying image:**\n__{e}__")
    type = event.pattern_match.group(3) or "r"
    w, h = image.size
    if w % 2 != 0 and type in ["r", "l"] or h % 2 != 0 and type in ["u", "b"]:
        image = image.resize((w + 1, h + 1))
        h, w = image.size
    if type == "l":
        left = 0
        upper = 0
        right = w // 2
        lower = h
        nw = right
        nh = left
    elif type == "r":
        left = w // 2
        upper = 0
        right = w
        lower = h
        nw = upper
        nh = upper
    elif type == "u":
        left = 0
        upper = 0
        right = w
        lower = h // 2
        nw = left
        nh = lower
    elif type == "b":
        left = 0
        upper = h // 2
        right = w
        lower = h
        nw = left
        nh = left
    temp = image.crop((left, upper, right, lower))
    temp = ImageOps.mirror(temp) if type in ["l", "r"] else ImageOps.flip(temp)
    image.paste(temp, (nw, nh))
    img = BytesIO()
    img.name = filename
    image.save(img, f_format)
    img.seek(0)
    await event.client.send_file(event.chat_id, img, reply_to=reply)
    await legendevent.delete()


@legend.legend_cmd(
    pattern="trig(?:\s|$)([\s\S]*)",
    command=("trig", menu_category),
    info={
        "header": "To trig the replied image or sticker",
        "usage": [
            "{tr}trig",
        ],
    },
)
async def dc(event):
    await event.edit("Making this image 😡triggered😈")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hmm = f"https://some-random-api.ml/canvas/triggered?avatar={link}"
    r = requests.get(hmm)
    open("legend.gif", "wb").write(r.content)
    hehe = "legend.gif"
    await bot.send_file(event.chat_id, hehe, caption="Got Triggered 😈😂", reply_to=dc)
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()


@legend.legend_cmd(
    pattern="waste(?:\s|$)([\s\S]*)",
    command=("waste", menu_category),
    info={
        "header": "To waste the replied image or sticker",
        "usage": [
            "{tr}waste <number>",
        ],
    },
)
async def dc(event):
    await event.edit("What a waste 😒😒")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hmm = f"https://some-random-api.ml/canvas/wasted?avatar={link}"
    r = requests.get(hmm)
    open("legend.png", "wb").write(r.content)
    hehe = "legend.png"
    await bot.send_file(event.chat_id, hehe, caption="Totally wasted⚰️ 😒", reply_to=dc)
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()


@legend.legend_cmd(
    pattern="irotate(?: |$)(\d+)$",
    command=("irortate", menu_category),
    info={
        "header": "To Trig the replied image or sticker",
        "usage": [
            "{tr}irotate <angle>",
        ],
    },
)
async def irotate(event):
    "To convert replied image or sticker to gif"
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo", "Sticker"]:
        return await eod(
            event, "__Reply to photo or sticker to rotate it with given angle.__"
        )
    if mediatype == "Sticker" and reply.document.mime_type == "application/i-tgsticker":
        return await eod(
            event,
            "__Reply to photo or sticker to rotate it with given angle. Animated sticker is not supported__",
        )
    args = event.pattern_match.group(1)
    legendevent = await eor(event, "__Rotating the replied media...__")
    imag = await _legendtools.media_to_pic(legendevent, reply, noedits=True)
    if imag[1] is None:
        return await eod(
            imag[0], "__Unable to extract image from the replied message.__"
        )
    image = Image.open(imag[1])
    try:
        image = image.rotate(int(args), expand=True)
    except Exception as e:
        return await eod(event, "**Error**\n" + str(e))
    await event.delete()
    img = io.BytesIO()
    img.name = "LegendUserBot.png"
    image.save(img, "PNG")
    img.seek(0)
    await event.client.send_file(event.chat_id, img, reply_to=reply)
    await legendevent.delete()


@legend.legend_cmd(
    pattern="iresize(?:\s|$)([\s\S]*)$",
    command=("iresize", menu_category),
    info={
        "header": "To resize the replied image/sticker",
        "usage": [
            "{tr}iresize <dimension> will send square image of that dimension",
            "{tr}iresize <width> <height> will send square image of that dimension",
        ],
        "examples": ["{tr}iresize 250", "{tr}iresize 500 250"],
    },
)
async def iresize(event):
    "To resize the replied image/sticker"
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo", "Sticker"]:
        return await eod(event, "__Reply to photo or sticker to resize it.__")
    if mediatype == "Sticker" and reply.document.mime_type == "application/i-tgsticker":
        return await eod(
            event,
            "__Reply to photo or sticker to resize it. Animated sticker is not supported__",
        )
    args = (event.pattern_match.group(1)).split()
    legendevent = await eor(event, "__Resizeing the replied media...__")
    imag = await _legendtools.media_to_pic(legendevent, reply, noedits=True)
    if imag[1] is None:
        return await eod(
            imag[0], "__Unable to extract image from the replied message.__"
        )
    image = Image.open(imag[1])
    w, h = image.size
    nw, nh = None, None
    if len(args) == 1:
        try:
            nw, nh = int(args[0]), int(args[0])
        except ValueError:
            return await eod(legendevent, "**Error:**\n__Invalid dimension.__")
    else:
        try:
            nw = int(args[0])
        except ValueError:
            return await eod(legendevent, "**Error:**\n__Invalid width.__")
        try:
            nh = int(args[1])
        except ValueError:
            return await eod(legendevent, "**Error:**\n__Invalid height.__")
    try:
        image = image.resize((nw, nh))
    except Exception as e:
        return await eod(legendevent, f"**Error:** __While resizing.\n{e}__")
    await event.delete()
    img = io.BytesIO()
    img.name = "LegendUserBot.png"
    image.save(img, "PNG")
    img.seek(0)
    await event.client.send_file(event.chat_id, img, reply_to=reply)
    await legendevent.delete()


@legend.legend_cmd(
    pattern="square$",
    command=("square", menu_category),
    info={
        "header": "Converts replied image to square image.",
        "usage": "{tr}square",
    },
)
async def square_cmd(event):
    "Converts replied image to square image."
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo"]:
        return await eod(event, "__Reply to photo to make it square image.__")
    legendevent = await event.edit("__Adding borders to make it square....__")
    try:
        imag = await _legendtools.media_to_pic(legendevent, reply, noedits=True)
        if imag[1] is None:
            return await eod(
                imag[0], "__Unable to extract image from the replied message.__"
            )
        img = Image.open(imag[1])
    except Exception as e:
        return await eod(legendevent, f"**Error in identifying image:**\n__{e}__")
    w, h = img.size
    if w == h:
        return await eod(event, "__The replied image is already in 1:1 ratio__")
    _min, _max = min(w, h), max(w, h)
    bg = img.crop(((w - _min) // 2, (h - _min) // 2, (w + _min) // 2, (h + _min) // 2))
    bg = bg.filter(ImageFilter.GaussianBlur(5))
    bg = bg.resize((_max, _max))
    bg.paste(img, ((_max - w) // 2, (_max - h) // 2))
    img = io.BytesIO()
    img.name = "img.jpg"
    bg.save(img)
    img.seek(0)
    await event.client.send_file(event.chat_id, img, reply_to=reply)
    await legendevent.delete()


pathdc = "./userbot/"
if not os.path.isdir(pathdc):
    os.makedirs(pathdc)


@legend.legend_cmd(
    pattern="bright(?: |$)(\d+)?$",
    command=("bright", menu_category),
    info={
        "header": "To convert image into doted image",
        "usage": [
            "{tr}bright",
        ],
    },
)
async def dc(event):
    await event.edit("Adding Brightness 😎")
    dc = await event.get_reply_message()
    if isinstance(dc.media, MessageMediaPhoto):
        img = await bot.download_media(dc.media, pathdc)
    elif "image" in dc.media.document.mime_type.split("/"):
        img = await bot.download_media(dc.media, pathdc)
    else:
        await event.edit("Reply To any Image only 😅😅")
        return
    url = upload_file(img)
    link = f"https://telegra.ph{url[0]}"
    hehe = f"https://some-random-api.ml/canvas/brightness?avatar={link}"
    r = requests.get(hehe)
    open("legend.png", "wb").write(r.content)
    hehe = "legend.png"
    await bot.send_file(
        event.chat_id, hehe, caption="Brightness increased 😎😎", reply_to=dc
    )
    for files in (hehe, img):
        if files and os.path.exists(files):
            os.remove(files)
    await event.delete()


@legend.legend_cmd(
    pattern="otify(?: |$)(\d+)?$",
    command=("otify", menu_category),
    info={
        "header": "To convert image into doted image",
        "usage": [
            "{tr}otify <number>",
        ],
    },
)
async def pic_gmd(event):
    "To convert image into doted image"
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo", "Sticker"]:
        return await eod(event, "__Reply to photo or sticker to make it doted image.__")
    if mediatype == "Sticker" and reply.document.mime_type == "application/i-tgsticker":
        return await eod(
            event,
            "__Reply to photo or sticker to make it doted image. Animated sticker is not supported__",
        )
    args = event.pattern_match.group(1)
    if args:
        if args.isdigit():
            pix = int(args) if int(args) > 0 else 100
    else:
        pix = 100
    legendevent = await eor(event, "__🎞Dotifying image...__")
    imag = await _legendtools.media_to_pic(legendevent, reply, noedits=True)
    if imag[1] is None:
        return await eod(
            imag[0], "__Unable to extract image from the replied message.__"
        )
    result = await dotify(imag[1], pix, True)
    await event.client.send_file(event.chat_id, result, reply_to=reply)
    await legendevent.delete()
    for i in [imag[1]]:
        if os.path.exists(i):
            os.remove(i)
