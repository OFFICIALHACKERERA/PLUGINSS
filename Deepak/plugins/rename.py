import asyncio
import os
import time
from datetime import datetime

from Deepak import legend

from ..Config import Config
from ..core.managers import eod, eor
from ..helpers.utils import reply_id
from . import progress, reply_id

menu_category = "utils"

thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")


@legend.legend_cmd(
    pattern="rnup ?(-f|-t)? ([\s\S]*)",
    command=("rnup", menu_category),
    info={
        "header": "To rename and upload the replied file.",
        "flags": {
            "f": "will upload as file that is document not streamable.",
            "t": "will upload with thumbnail",
        },
        "description": "If type is not used then will upload as steamable file",
        "usage": [
            "{tr}rnup <new file name>",
            "{tr}rnup -f <new file name>",
        ],
    },
)
async def rnup(event):
    "To rename and upload the file"
    thumb = thumb_image_path if os.path.exists(thumb_image_path) else None
    types = event.pattern_match.group(1)
    forcedoc = bool(types)
    supsstream = not types
    legendevent = await eor(
        event,
        "`Rename & Upload in process 🙄🙇‍♂️🙇‍♂️🙇‍♀️ It might take some time if file size is big`",
    )
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(2)
    if not event.reply_to_msg_id:
        return await legendevent.edit(
            "**Syntax : **`.rnup file name` as reply to a Telegram media"
        )
    start = datetime.now()
    file_name = input_str
    reply_message = await event.get_reply_message()
    c_time = time.time()
    downloaded_file_name = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, file_name)
    downloaded_file_name = await event.client.download_media(
        reply_message,
        downloaded_file_name,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, legendevent, c_time, "trying to download", file_name)
        ),
    )
    end = datetime.now()
    ms_one = (end - start).seconds
    if types == "-t":
        thumb = thumb
    else:
        try:
            thumb = await reply_message.download_media(thumb=-1)
        except Exception:
            thumb = thumb
    if not os.path.exists(downloaded_file_name):
        return await legendevent.edit(f"File Not Found {input_str}")
    c_time = time.time()
    caat = await event.client.send_file(
        event.chat_id,
        downloaded_file_name,
        force_document=forcedoc,
        supports_streaming=supsstream,
        allow_cache=False,
        reply_to=reply_to_id,
        thumb=thumb,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "trying to upload", downloaded_file_name)
        ),
    )
    end_two = datetime.now()
    os.remove(downloaded_file_name)
    ms_two = (end_two - end).seconds
    await eod(
        legendevent,
        f"`Downloaded file in {ms_one} seconds.\nAnd Uploaded in {ms_two} seconds.`",
    )
