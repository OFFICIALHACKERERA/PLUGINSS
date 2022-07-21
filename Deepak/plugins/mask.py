# credits to @LEGEND_K_BOY and @LEGEND_K_BOY

import os

from telegraph import exceptions, upload_file
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import legend

from ..Config import Config
from ..core.managers import eor
from . import awooify, baguette, convert_toimage, iphonex, lolice

menu_category = "extra"


@legend.legend_cmd(
    pattern="mask$",
    command=("mask", menu_category),
    info={
        "header": "reply to image to get hazmat suit for that image.",
        "usage": "{tr}mask",
    },
)
async def _(owobot):
    "Hazmat suit maker"
    reply_message = await owobot.get_reply_message()
    if not reply_message.media or not reply_message:
        return await eor(owobot, "```reply to media message```")
    chat = "@hazmat_suit_bot"
    if reply_message.sender.bot:
        return await eor(owobot, "```Reply to actual users message.```")
    event = await owobot.edit("```Processing```")
    async with owobot.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=905164246)
            )
            await owobot.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            return await event.edit(
                "```Please unblock @hazmat_suit_bot and try again```"
            )
        if response.text.startswith("Forward"):
            await event.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await owobot.client.send_file(event.chat_id, response.message.media)
            await event.delete()


@legend.legend_cmd(
    pattern="awooify$",
    command=("awooify", menu_category),
    info={
        "header": "Check yourself by replying to image.",
        "usage": "{tr}awooify",
    },
)
async def owobot(swtmemes):
    "replied Image will be face of other image"
    replied = await swtmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await eor(swtmemes, "reply to a supported media file")
    if replied.media:
        legendevent = await eor(swtmemes, "passing to telegraph...")
    else:
        return await eor(swtmemes, "reply to a supported media file")
    download_location = await swtmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await legendevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await legendevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await legendevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await legendevent.edit("ERROR: " + str(exc))
    legend = f"https://telegra.ph{response[0]}"
    lol = await awooify(legend)
    await legendevent.delete()
    await swtmemes.client.send_file(swtmemes.chat_id, lol, reply_to=replied)


@legend.legend_cmd(
    pattern="lolice$",
    command=("lolice", menu_category),
    info={
        "header": "image masker check your self by replying to image.",
        "usage": "{tr}lolice",
    },
)
async def owobot(swtmemes):
    "replied Image will be face of other image"
    replied = await swtmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await eor(swtmemes, "reply to a supported media file")
    if replied.media:
        legendevent = await eor(swtmemes, "passing to telegraph...")
    else:
        return await eor(swtmemes, "reply to a supported media file")
    download_location = await swtmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await legendevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await legendevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await legendevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await legendevent.edit("ERROR: " + str(exc))
    legend = f"https://telegra.ph{response[0]}"
    lol = await lolice(legend)
    await legendevent.delete()
    await swtmemes.client.send_file(swtmemes.chat_id, lol, reply_to=replied)


@legend.legend_cmd(
    pattern="bun$",
    command=("bun", menu_category),
    info={
        "header": "reply to image and check yourself.",
        "usage": "{tr}bun",
    },
)
async def owobot(swtmemes):
    "replied Image will be face of other image"
    replied = await swtmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await eor(swtmemes, "reply to a supported media file")
    if replied.media:
        legendevent = await eor(swtmemes, "passing to telegraph...")
    else:
        return await eor(swtmemes, "reply to a supported media file")
    download_location = await swtmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await legendevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await legendevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await legendevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await legendevent.edit("ERROR: " + str(exc))
    legend = f"https://telegra.ph{response[0]}"
    lol = await baguette(legend)
    await legendevent.delete()
    await swtmemes.client.send_file(swtmemes.chat_id, lol, reply_to=replied)


@legend.legend_cmd(
    pattern="iphx$",
    command=("iphx", menu_category),
    info={
        "header": "replied image as iphone x wallpaper.",
        "usage": "{tr}iphx",
    },
)
async def owobot(swtmemes):
    "replied image as iphone x wallpaper."
    replied = await swtmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        return await eor(swtmemes, "reply to a supported media file")
    if replied.media:
        legendevent = await eor(swtmemes, "passing to telegraph...")
    else:
        return await eor(swtmemes, "reply to a supported media file")
    download_location = await swtmemes.client.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            os.remove(download_location)
            return await legendevent.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
        await legendevent.edit("generating image..")
    else:
        os.remove(download_location)
        return await legendevent.edit("the replied file is not supported")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        os.remove(download_location)
        return await legendevent.edit("ERROR: " + str(exc))
    legend = f"https://telegra.ph{response[0]}"
    lol = await iphonex(legend)
    await legendevent.delete()
    await swtmemes.client.send_file(swtmemes.chat_id, lol, reply_to=replied)
