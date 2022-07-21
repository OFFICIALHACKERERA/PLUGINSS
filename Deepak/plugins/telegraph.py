# telegraph utils for LegendUserBot
import os
import random
import string
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.utils import get_display_name

from userbot import legend

from ..Config import Config
from ..core.logger import logging
from ..core.managers import eod, eor
from ..helpers.functions import delete_conv
from . import legend, mention, reply_id

LOGS = logging.getLogger(__name__)
menu_category = "utils"


telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


@legend.legend_cmd(
    pattern="ctg(?: |$)([\s\S]*)",
    command=("ctg", menu_category),
    info={
        "header": "Reply to link To get link preview using telegrah.s.",
        "usage": "{tr}ctg <reply/text>",
    },
)
async def ctg(event):
    "To get link preview"
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    reply_to_id = await reply_id(event)
    if not input_str and reply:
        input_str = reply.text
    if not input_str:
        return await eod(event, "**ಠ∀ಠ Give me link to search..**", 20)
    urls = extractor.find_urls(input_str)
    if not urls:
        return await eod(event, "**There no link to search in the text..**", 20)
    chat = "@chotamreaderbot"
    legendevent = await eor(event, "```Processing...```")
    async with event.client.conversation(chat) as conv:
        try:
            msg_flag = await conv.send_message(urls[0])
        except YouBlockedUserError:
            await eor(
                legendevent, "**Error:** Trying to unblock & retry, wait a sec..."
            )
            await legend(unblock("chotamreaderbot"))
            msg_flag = await conv.send_message(urls[0])
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        if response.text.startswith(""):
            await eor(legendevent, "Am I Dumb Or Are U Dumb?")
        else:
            await legndevent.delete()
            await event.client.send_message(
                event.chat_id, response, reply_to=reply_to_id, link_preview=True
            )
        await delete_conv(event, chat, msg_flag)


@legend.legend_cmd(
    pattern="(t(ele)?g(raph)?) ?(m|t|media|text)(?:\s|$)([\s\S]*)",
    command=("telegraph", menu_category),
    info={
        "header": "To get telegraph link.",
        "description": "Reply to text message to paste that text on telegraph you can also pass input along with command \
            So that to customize title of that telegraph and reply to media file to get sharable link of that media(atmost 5mb is supported)",
        "options": {
            "m or media": "To get telegraph link of replied sticker/image/video/gif.",
            "t or text": "To get telegraph link of replied text you can use custom title.",
        },
        "usage": [
            "{tr}tgm",
            "{tr}tgt <title(optional)>",
            "{tr}telegraph media",
            "{tr}telegraph text <title(optional)>",
        ],
    },
)  # sourcery no-metrics
async def _(event):
    "To get telegraph link."
    legendevent = await eor(event, "`processing........`")
    optional_title = event.pattern_match.group(5)
    if not event.reply_to_msg_id:
        return await legendevent.edit(
            "`Reply to a message to get a permanent telegra.ph link.`",
        )

    start = datetime.now()
    r_message = await event.get_reply_message()
    input_str = (event.pattern_match.group(4)).strip()
    if input_str in ["media", "m"]:
        downloaded_file_name = await event.client.download_media(
            r_message, Config.TEMP_DIR
        )
        await legendevent.edit(f"`Downloaded to {downloaded_file_name}`")
        if downloaded_file_name.endswith((".webp")):
            resize_image(downloaded_file_name)
        try:
            media_urls = upload_file(downloaded_file_name)
        except exceptions.TelegraphException as exc:
            await legendevent.edit(f"**Error : **\n`{exc}`")
            os.remove(downloaded_file_name)
        else:
            end = datetime.now()
            ms = (end - start).seconds
            os.remove(downloaded_file_name)
            await legendevent.edit(
                f"**✓ Uploaded to :-**[telegraph](https://telegra.ph{media_urls[0]})\
                 \n**✓ Uploaded in {ms} seconds.**\
                 \n**✓ Uploaded by :-** {mention}\
                 \n**✓ Telegraph :** `https://telegra.ph{media_urls[0]}`",
                link_preview=True,
            )
    elif input_str in ["text", "t"]:
        user_object = await event.client.get_entity(r_message.sender_id)
        title_of_page = get_display_name(user_object)
        # apparently, all Users do not have last_name field
        if optional_title:
            title_of_page = optional_title
        page_content = r_message.message
        if r_message.media:
            if page_content != "":
                title_of_page = page_content
            downloaded_file_name = await event.client.download_media(
                r_message, Config.TEMP_DIR
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            for m in m_list:
                page_content += m.decode("UTF-8") + "\n"
            os.remove(downloaded_file_name)
        page_content = page_content.replace("\n", "<br>")
        try:
            response = telegraph.create_page(title_of_page, html_content=page_content)
        except Exception as e:
            LOGS.info(e)
            title_of_page = "".join(
                random.choice(list(string.ascii_lowercase + string.ascii_uppercase))
                for _ in range(16)
            )
            response = telegraph.create_page(title_of_page, html_content=page_content)
        end = datetime.now()
        ms = (end - start).seconds
        legend = f"https://telegra.ph/{response['path']}"
        await legendevent.edit(
            f"**✓ Uploaded to :-** [telegraph]({legend})\
                 \n**✓ Uploaded in {ms} seconds.**\
                 \n**✓ Uploaded by :-** {mention}\
                 \n**✓ Telegraph :-** `{legend}`",
            link_preview=True,
        )
