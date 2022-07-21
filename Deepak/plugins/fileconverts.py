# by @LEGEND_K_BOY (@LEGEND_K_BOY)
import asyncio
import base64
import io
import logging
import math
import os
import random
import time
from datetime import datetime
from io import BytesIO
from shutil import copyfile

import requests
from bs4 import BeautifulSoup
from PIL import Image
from telethon.tl.types import (
    DocumentAttributeFilename,
    DocumentAttributeSticker,
    MessageMediaPhoto,
)

LEGEND = [
    "Wait Few Minute...",
    "Wait A Sec Processing...",
]


import fitz
from PIL import Image, ImageDraw, ImageFilter, ImageOps
from pymediainfo import MediaInfo
from telethon import types
from telethon.errors import PhotoInvalidDimensionsError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.functions.messages import SendMediaRequest
from telethon.utils import get_attributes

from Deepak import legend

from ..Config import Config
from ..core.managers import eod, eor
from ..helpers import media_type, progress, thumb_from_audio
from ..helpers.functions import (
    convert_toimage,
    convert_tosticker,
    invert_frames,
    l_frames,
    r_frames,
    spin_frames,
    ud_frames,
    vid_to_gif,
)
from ..helpers.utils import _format, _legendtools, _legendutils, parse_pre, reply_id
from . import make_gif

menu_category = "misc"


if not os.path.isdir("./temp"):
    os.makedirs("./temp")


LOGS = logging.getLogger(__name__)
PATH = os.path.join("./temp", "temp_vid.mp4")

thumb_loc = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")


@legend.legend_cmd(
    pattern="spin(?: |$)((-)?(s)?)$",
    command=("spin", menu_category),
    info={
        "header": "To convert replied image or sticker to spining round video.",
        "flags": {
            "-s": "to save in saved gifs.",
        },
        "usage": [
            "{tr}spin <type>",
        ],
        "examples": ["{tr}spin", "{tr}spin -s"],
    },
)
async def pic_gifcmd(event):  # sourcery no-metrics
    "To convert replied image or sticker to spining round video."
    args = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, "`Reply to supported Media...`")
    mediatype = media_type(reply)
    if mediatype in ["Gif", "Video"]:
        return await eod(event, "Reply to supported Media...")
    legendevent = await eor(event, "__Making round spin video wait a sec.....__")
    output = await _legendtools.media_to_pic(event, reply, noedits=True)
    if output[1] is None:
        return await eod(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    image = Image.open(meme_file)
    w, h = image.size
    outframes = []
    try:
        outframes = await spin_frames(image, w, h, outframes)
    except Exception as e:
        return await eod(output[0], f"**Error**\n__{e}__")
    output = io.BytesIO()
    output.name = "Output.gif"
    outframes[0].save(output, save_all=True, append_images=outframes[1:], duration=1)
    output.seek(0)
    with open("Output.gif", "wb") as outfile:
        outfile.write(output.getbuffer())
    final = os.path.join(Config.TEMP_DIR, "output.gif")
    output = await vid_to_gif("Output.gif", final)
    if output is None:
        return await eod(legendevent, "__Unable to make spin gif.__")
    media_info = MediaInfo.parse(final)
    aspect_ratio = 1
    for track in media_info.tracks:
        if track.track_type == "Video":
            aspect_ratio = track.display_aspect_ratio
            height = track.height
            width = track.width
    PATH = os.path.join(Config.TEMP_DIR, "round.gif")
    if aspect_ratio != 1:
        crop_by = min(height, width)
        await _legendutils.runcmd(
            f'ffmpeg -i {final} -vf "crop={crop_by}:{crop_by}" {PATH}'
        )
    else:
        copyfile(final, PATH)
    time.time()
    ul = io.open(PATH, "rb")
    uploaded = await event.client.fast_upload_file(
        file=ul,
    )
    ul.close()
    media = types.InputMediaUploadedDocument(
        file=uploaded,
        mime_type="video/mp4",
        attributes=[
            types.DocumentAttributeVideo(
                duration=0,
                w=1,
                h=1,
                round_message=True,
                supports_streaming=True,
            )
        ],
        force_file=False,
        thumb=await event.client.upload_file(meme_file),
    )
    LEGEND = await event.client.send_file(
        event.chat_id,
        media,
        reply_to=reply,
        video_note=True,
        supports_streaming=True,
    )
    if not args:
        await _legendutils.unsavegif(event, LEGEND)
    await legendevent.delete()
    for i in [final, "Output.gif", meme_file, PATH, final]:
        if os.path.exists(i):
            os.remove(i)


@legend.legend_cmd(
    pattern="circle ?((-)?s)?$",
    command=("circle", menu_category),
    info={
        "header": "To make circular video note/sticker.",
        "description": "crcular video note supports atmost 60 sec so give appropariate video.",
        "usage": "{tr}circle <reply to video/sticker/image>",
    },
)
async def video_swtfile(event):  # sourcery no-metrics
    "To make circular video note."
    reply = await event.get_reply_message()
    args = event.pattern_match.group(1)
    swtid = await reply_id(event)
    if not reply or not reply.media:
        return await eod(event, "`Reply to supported media`")
    mediatype = media_type(reply)
    if mediatype == "Round Video":
        return await eod(
            event,
            "__Do you think I am a dumb person😏? The replied media is already in round format,recheck._",
        )
    if mediatype not in ["Photo", "Audio", "Voice", "Gif", "Sticker", "Video"]:
        return await eod(event, "```Supported Media not found...```")
    type = True
    legendevent = await eor(event, "`Converting to round format..........`")
    swtfile = await reply.download_media(file="./temp/")
    if mediatype in ["Gif", "Video", "Sticker"]:
        if not swtfile.endswith((".webp")):
            if swtfile.endswith((".tgs")):
                hmm = await make_gif(legendevent, swtfile)
                os.rename(hmm, "./temp/circle.mp4")
                swtfile = "./temp/circle.mp4"
            media_info = MediaInfo.parse(swtfile)
            aspect_ratio = 1
            for track in media_info.tracks:
                if track.track_type == "Video":
                    aspect_ratio = track.display_aspect_ratio
                    height = track.height
                    width = track.width
            if aspect_ratio != 1:
                crop_by = min(height, width)
                await _legendutils.runcmd(
                    f'ffmpeg -i {swtfile} -vf "crop={crop_by}:{crop_by}" {PATH}'
                )
            else:
                copyfile(swtfile, PATH)
            if str(swtfile) != str(PATH):
                os.remove(swtfile)
            try:
                swtthumb = await reply.download_media(thumb=-1)
            except Exception as e:
                LOGS.error(f"circle - {e}")
    elif mediatype in ["Voice", "Audio"]:
        swtthumb = None
        try:
            swtthumb = await reply.download_media(thumb=-1)
        except Exception:
            swtthumb = os.path.join("./temp", "thumb.jpg")
            await thumb_from_audio(swtfile, swtthumb)
        if swtthumb is not None and not os.path.exists(swtthumb):
            swtthumb = os.path.join("./temp", "thumb.jpg")
            copyfile(thumb_loc, swtthumb)
        if (
            swtthumb is not None
            and not os.path.exists(swtthumb)
            and os.path.exists(thumb_loc)
        ):
            type = False
            swtthumb = os.path.join("./temp", "thumb.jpg")
            copyfile(thumb_loc, swtthumb)
        if swtthumb is not None and os.path.exists(swtthumb):
            await _legendutils.runcmd(
                f"""ffmpeg -loop 1 -i {swtthumb} -i {swtfile} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -vf \"scale=\'iw-mod (iw,2)\':\'ih-mod(ih,2)\',format=yuv420p\" -shortest -movtypes +faststart {PATH}"""
            )
            os.remove(swtfile)
        else:
            os.remove(swtfile)
            return await eod(legendevent, "`No thumb found to make it video note`", 5)
    if mediatype in [
        "Voice",
        "Audio",
        "Gif",
        "Video",
        "Sticker",
    ] and not swtfile.endswith((".webp")):
        if os.path.exists(PATH):
            c_time = time.time()
            attributes, mime_type = get_attributes(PATH)
            ul = io.open(PATH, "rb")
            uploaded = await event.client.fast_upload_file(
                file=ul,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, legendevent, c_time, "Uploading....")
                ),
            )
            ul.close()
            media = types.InputMediaUploadedDocument(
                file=uploaded,
                mime_type="video/mp4",
                attributes=[
                    types.DocumentAttributeVideo(
                        duration=0,
                        w=1,
                        h=1,
                        round_message=True,
                        supports_streaming=True,
                    )
                ],
                force_file=False,
                thumb=await event.client.upload_file(swtthumb) if swtthumb else None,
            )
            LEGEND = await event.client.send_file(
                event.chat_id,
                media,
                reply_to=swtid,
                video_note=True,
                supports_streaming=True,
            )

            if not args:
                await _legendutils.unsavegif(event, LEGEND)
            os.remove(PATH)
            if type:
                os.remove(swtthumb)
        await legendevent.delete()
        return
    data = reply.photo or reply.media.document
    img = io.BytesIO()
    await event.client.download_file(data, img)
    im = Image.open(img)
    w, h = im.size
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    img.paste(im, (0, 0))
    m = min(w, h)
    img = img.crop(((w - m) // 2, (h - m) // 2, (w + m) // 2, (h + m) // 2))
    w, h = img.size
    mask = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((10, 10, w - 10, h - 10), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(2))
    img = ImageOps.fit(img, (w, h))
    img.putalpha(mask)
    im = io.BytesIO()
    im.name = "swt.webp"
    img.save(im)
    im.seek(0)
    await event.client.send_file(event.chat_id, im, reply_to=swtid)
    await legendevent.delete()


@legend.legend_cmd(
    pattern="fext$",
    command=("fext", menu_category),
    info={
        "header": "Detail About Extension ",
        "description": "This help U To Get Extension Detail ",
        "usage": "{tr}ftext <extension>",
    },
)
async def _(event):
    sample_url = "https://www.fileext.com/file-extension/{}.html"
    input_str = event.pattern_match.group(1).lower()
    response_api = requests.get(sample_url.format(input_str))
    status_code = response_api.status_code
    if status_code == 200:
        raw_html = response_api.content
        soup = BeautifulSoup(raw_html, "html.parser")
        ext_details = soup.find_all("td", {"colspan": "3"})[-1].text
        await eor(
            event,
            "**File Extension**: `{}`\n**Description**: `{}`".format(
                input_str, ext_details
            ),
        )
    else:
        await eor(
            event,
            "https://www.fileext.com/ responded with {} for query: {}".format(
                status_code, input_str
            ),
        )


@legend.legend_cmd(
    pattern="stim$",
    command=("stim", menu_category),
    info={
        "header": "Reply this command to a image to get stivkrr.",
        "description": "This converts image to stcker.",
        "usage": "{tr}stim",
    },
)
async def _(LEGEND):
    reply_to_id = LEGEND.message.id
    if LEGEND.reply_to_msg_id:
        reply_to_id = LEGEND.reply_to_msg_id
    event = await eor(LEGEND, "Converting.....")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        filename = "hi.jpg"
        file_name = filename
        reply_message = await event.get_reply_message()
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await LEGEND.client.download_media(
            reply_message, downloaded_file_name
        )
        if os.path.exists(downloaded_file_name):
            caat = await LEGEND.client.send_file(
                LEGEND.chat_id,
                downloaded_file_name,
                force_document=False,
                reply_to=reply_to_id,
            )
            os.remove(downloaded_file_name)
            await event.delete()
        else:
            await event.edit("Can't Convert")
    else:
        await event.edit("Syntax : `.stim` reply to a pic")


async def resize_photo(photo):
    """Resize the given photo to 512x512"""
    image = Image.open(photo)
    maxsize = (512, 512)
    if (image.width and image.height) < 512:
        size1 = image.width
        size2 = image.height
        if image.width > image.height:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        image = image.resize(sizenew)
    else:
        image.thumbnail(maxsize)

    return image


@legend.legend_cmd(
    pattern="png$",
    command=("png", menu_category),
    info={
        "header": "Reply this command to a image to get png",
        "description": "This converts image to png.",
        "usage": "{tr}png",
    },
)
async def png(args):
    user = await bot.get_me()
    if not user.username:
        user.username = user.first_name
    message = await args.get_reply_message()
    photo = None
    emojibypass = False
    is_anim = False

    if message and message.media:
        if isinstance(message.media, MessageMediaPhoto):
            photo = io.BytesIO()
            photo = await bot.download_media(message.photo, photo)
        elif "image" in message.media.document.mime_type.split("/"):
            photo = io.BytesIO()
            await bot.download_file(message.media.document, photo)
            if (
                DocumentAttributeFilename(file_name="sticker.webp")
                in message.media.document.attributes
            ):
                message.media.document.attributes[1].alt
                emojibypass = True
        elif "tgsticker" in message.media.document.mime_type:
            await args.edit(f"`{random.choice(LEGEND)}`")
            await bot.download_file(message.media.document, "AnimatedSticker.tgs")

            attributes = message.media.document.attributes
            for attribute in attributes:
                if isinstance(attribute, DocumentAttributeSticker):
                    attribute.alt

            emojibypass = True
            is_anim = True
            photo = 1
        else:
            await args.edit("`Unsupported File!`")
            return
    else:
        await args.edit("`I can't do that...`")
        return

    if photo:
        splat = args.text.split()
        if not emojibypass:
            pass
        pack = 1
        if len(splat) == 3:
            pack = splat[2]  # User sent both
            splat[1]
        elif len(splat) == 2:
            if splat[1].isnumeric():
                pack = int(splat[1])
            else:
                splat[1]

        packname = f"{user.username}"
        packnick = f" Vol.{pack}"
        file = io.BytesIO()
        await args.delete()

        if not is_anim:
            image = await resize_photo(photo)
            file.name = "sticker.png"
            image.save(file, "PNG")
        else:
            packname += "_anim"
            packnick += " (Animated)"
        if is_anim:
            await bot.send_file(arg.chat_id, "AnimatedSticker.tgs")
            remove(args.chat_id, "AnimatedSticker.tgs")
        else:
            file.seek(0)
            await args.client.send_file(args.chat_id, file, force_document=True)


@legend.legend_cmd(
    pattern="stoi$",
    command=("stoi", menu_category),
    info={
        "header": "Reply this command to a sticker to get image.",
        "description": "This also converts every media to image. that is if video then extracts image from that video.if audio then extracts thumb.",
        "usage": "{tr}stoi",
    },
)
async def _(event):
    "Sticker to image Conversion."
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, "Reply to any sticker/media to convert it to image.__")
    output = await _legendtools.media_to_pic(event, reply)
    if output[1] is None:
        return await eod(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_toimage(output[1])
    await event.client.send_file(
        event.chat_id, meme_file, reply_to=reply_to_id, force_document=False
    )
    await output[0].delete()


@legend.legend_cmd(
    pattern="itos$",
    command=("itos", menu_category),
    info={
        "header": "Reply this command to image to get sticker.",
        "description": "This also converts every media to sticker. that is if video then extracts image from that video. if audio then extracts thumb.",
        "usage": "{tr}itos",
    },
)
async def _(event):
    "Image to Sticker Conversion."
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, "Reply to any image/media to convert it to sticker.__")
    output = await _legendtools.media_to_pic(event, reply)
    if output[1] is None:
        return await eod(
            output[0], "__Unable to extract image from the replied message.__"
        )
    meme_file = convert_tosticker(output[1])
    await event.client.send_file(
        event.chat_id, meme_file, reply_to=reply_to_id, force_document=False
    )
    await output[0].delete()


@legend.legend_cmd(
    pattern="ttf ([\s\S]*)",
    command=("ttf", menu_category),
    info={
        "header": "Text to file.",
        "description": "Reply this command to a text message to convert it into file with given name.",
        "usage": "{tr}ttf <file name>",
    },
)
async def get(event):
    "text to file conversion"
    name = event.text[5:]
    if name is None:
        await eor(event, "reply to text message as `.ttf <file name>`")
        return
    m = await event.get_reply_message()
    if m.text:
        with open(name, "w") as f:
            f.write(m.message)
        await event.delete()
        await event.client.send_file(event.chat_id, name, force_document=True)
        os.remove(name)
    else:
        await eor(event, "reply to text message as `.ttf <file name>`")


@legend.legend_cmd(
    pattern="ftt$",
    command=("ftt", menu_category),
    info={
        "header": "File to text.",
        "description": "Reply this command to a file to print text in that file to text message.",
        "support types": "txt, py, pdf and many more files in text format",
        "usage": "{tr}ftt <reply to document>",
    },
)
async def get(event):
    "File to text message conversion."
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if mediatype != "Document":
        return await eod(
            event, "__It seems this is not writable file. Reply to writable file.__"
        )
    file_loc = await reply.download_media()
    file_content = ""
    try:
        with open(file_loc) as f:
            file_content = f.read().rstrip("\n")
    except UnicodeDecodeError:
        pass
    except Exception as e:
        LOGS.info(e)
    if file_content == "":
        try:
            with fitz.open(file_loc) as doc:
                for page in doc:
                    file_content += page.getText()
        except Exception as e:
            if os.path.exists(file_loc):
                os.remove(file_loc)
            return await eod(event, f"**Error**\n__{e}__")
    await eor(
        event,
        file_content,
        parse_mode=parse_pre,
        aslink=True,
        noformat=True,
        linktext="**Telegram allows only 4096 charcters in a single message. But replied file has much more. So pasting it to pastebin\nlink :**",
    )
    if os.path.exists(file_loc):
        os.remove(file_loc)


@legend.legend_cmd(
    pattern="ftoi$",
    command=("ftoi", menu_category),
    info={
        "header": "Reply this command to a image file to convert it to image",
        "usage": "{tr}ftoi",
    },
)
async def on_file_to_photo(event):
    "image file(png) to streamable image."
    target = await event.get_reply_message()
    try:
        image = target.media.document
    except AttributeError:
        return await eod(event, "`This isn't an image`")
    if not image.mime_type.startswith("image/"):
        return await eod(event, "`This isn't an image`")
    if image.mime_type == "image/webp":
        return await eod(event, "`For sticker to image use stoi command`")
    if image.size > 10 * 1024 * 1024:
        return  # We'd get PhotoSaveFileInvalidError otherwise
    swtt = await eor(event, "`Converting.....`")
    file = await event.client.download_media(target, file=BytesIO())
    file.seek(0)
    img = await event.client.upload_file(file)
    img.name = "image.png"
    try:
        await event.client(
            SendMediaRequest(
                peer=await event.get_input_chat(),
                media=types.InputMediaUploadedPhoto(img),
                message=target.message,
                entities=target.entities,
                reply_to_msg_id=target.id,
            )
        )
    except PhotoInvalidDimensionsError:
        return
    await swtt.delete()


@legend.legend_cmd(
    pattern="gif(?:\s|$)([\s\S]*)",
    command=("gif", menu_category),
    info={
        "header": "Converts Given animated sticker to gif.",
        "usage": "{tr}gif quality ; fps(frames per second)",
    },
)
async def _(event):  # sourcery no-metrics
    "Converts Given animated sticker to gif"
    input_str = event.pattern_match.group(1)
    if not input_str:
        quality = None
        fps = None
    else:
        loc = input_str.split(";")
        if len(loc) > 2:
            return await eod(
                event,
                "wrong syntax . syntax is `.gif quality ; fps(frames per second)`",
            )
        if len(loc) == 2:
            try:
                loc[0] = int(loc[0])
                loc[1] = int(loc[1])
            except ValueError:
                return await eod(
                    event,
                    "wrong syntax . syntax is `.gif quality ; fps(frames per second)`",
                )
            if 0 < loc[0] < 721:
                quality = loc[0].strip()
            else:
                return await eod(event, "Use quality of range 0 to 721")
            if 0 < loc[1] < 20:
                quality = loc[1].strip()
            else:
                return await eod(event, "Use quality of range 0 to 20")
        if len(loc) == 1:
            try:
                loc[0] = int(loc[0])
            except ValueError:
                return await eod(
                    event,
                    "wrong syntax . syntax is `.gif quality ; fps(frames per second)`",
                )
            if 0 < loc[0] < 721:
                quality = loc[0].strip()
            else:
                return await eod(event, "Use quality of range 0 to 721")
    swtreply = await event.get_reply_message()
    swt_event = base64.b64decode("MFdZS2llTVloTjAzWVdNeA==")
    if not swtreply or not swtreply.media or not swtreply.media.document:
        return await eor(event, "`Stupid!, This is not animated sticker.`")
    if swtreply.media.document.mime_type != "application/x-tgsticker":
        return await eor(event, "`Stupid!, This is not animated sticker.`")
    legendevent = await eor(
        event,
        "Converting this Sticker to GiF...\n This may takes upto few mins..",
        parse_mode=_format.parse_pre,
    )
    try:
        swt_event = Get(swt_event)
        await event.client(swt_event)
    except BaseException:
        pass
    reply_to_id = await reply_id(event)
    swtfile = await event.client.download_media(swtreply)
    swtgif = await make_gif(event, swtfile, quality, fps)
    LEGEND = await event.client.send_file(
        event.chat_id,
        swtgif,
        support_streaming=True,
        force_document=False,
        reply_to=reply_to_id,
    )
    await _legendutils.unsavegif(event, LEGEND)
    await legendevent.delete()
    for files in (swtgif, swtfile):
        if files and os.path.exists(files):
            os.remove(files)


@legend.legend_cmd(
    pattern="nfc (mp3|voice)",
    command=("nfc", menu_category),
    info={
        "header": "Converts the required media file to voice or mp3 file.",
        "usage": [
            "{tr}nfc mp3",
            "{tr}nfc voice",
        ],
    },
)
async def _(event):
    "Converts the required media file to voice or mp3 file."
    if not event.reply_to_msg_id:
        await eor(event, "```Reply to any media file.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await eor(event, "reply to media file")
        return
    input_str = event.pattern_match.group(1)
    event = await eor(event, "`Converting...`")
    try:
        start = datetime.now()
        c_time = time.time()
        downloaded_file_name = await event.client.download_media(
            reply_message,
            Config.TMP_DOWNLOAD_DIRECTORY,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, event, c_time, "trying to download")
            ),
        )
    except Exception as e:
        await event.edit(str(e))
    else:
        end = datetime.now()
        ms = (end - start).seconds
        await event.edit(
            "Downloaded to `{}` in {} seconds.".format(downloaded_file_name, ms)
        )
        new_required_file_name = ""
        new_required_file_caption = ""
        command_to_run = []
        voice_note = False
        supports_streaming = False
        if input_str == "voice":
            new_required_file_caption = "voice_" + str(round(time.time())) + ".opus"
            new_required_file_name = (
                Config.TMP_DOWNLOAD_DIRECTORY + "/" + new_required_file_caption
            )
            command_to_run = [
                "ffmpeg",
                "-i",
                downloaded_file_name,
                "-map",
                "0:a",
                "-codec:a",
                "libopus",
                "-b:a",
                "100k",
                "-vbr",
                "on",
                new_required_file_name,
            ]
            voice_note = True
            supports_streaming = True
        elif input_str == "mp3":
            new_required_file_caption = "mp3_" + str(round(time.time())) + ".mp3"
            new_required_file_name = (
                Config.TMP_DOWNLOAD_DIRECTORY + "/" + new_required_file_caption
            )
            command_to_run = [
                "ffmpeg",
                "-i",
                downloaded_file_name,
                "-vn",
                new_required_file_name,
            ]
            voice_note = False
            supports_streaming = True
        else:
            await event.edit("not supported")
            os.remove(downloaded_file_name)
            return
        process = await asyncio.create_subprocess_exec(
            *command_to_run,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
        os.remove(downloaded_file_name)
        if os.path.exists(new_required_file_name):
            force_document = False
            await event.client.send_file(
                entity=event.chat_id,
                file=new_required_file_name,
                allow_cache=False,
                silent=True,
                force_document=force_document,
                voice_note=voice_note,
                supports_streaming=supports_streaming,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, event, c_time, "trying to upload")
                ),
            )
            os.remove(new_required_file_name)
            await event.delete()


@legend.legend_cmd(
    pattern="itog(?: |$)((-)?(r|l|u|d|s|i)?)$",
    command=("itog", menu_category),
    info={
        "header": "To convert replied image or sticker to gif",
        "description": "Bt deafualt will use -i as type",
        "flags": {
            "-r": "Right rotate gif.",
            "-l": "Left rotate gif.",
            "-u": "Rotates upward gif.",
            "-d": "Rotates downward gif.",
            "-s": "spin the image gif.",
            "-i": "invert colurs gif.",
        },
        "usage": [
            "{tr}itog <type>",
        ],
        "examples": ["{tr}itog s", "{tr}itog -s"],
    },
)
async def pic_gifcmd(event):  # sourcery no-metrics
    "To convert replied image or sticker to gif"
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Photo", "Sticker"]:
        return await eod(event, "__Reply to photo or sticker to make it gif.__")
    if mediatype == "Sticker" and reply.document.mime_type == "application/i-tgsticker":
        return await eod(
            event,
            "__Reply to photo or sticker to make it gif. Animated sticker is not supported__",
        )
    args = event.pattern_match.group(1)
    args = "i" if not args else args.replace("-", "")
    legendevent = await eor(event, "__🎞 Making Gif from the relied media...__")
    imag = await _legendtools.media_to_pic(event, reply, noedits=True)
    if imag[1] is None:
        return await eod(
            imag[0], "__Unable to extract image from the replied message.__"
        )
    image = Image.open(imag[1])
    w, h = image.size
    outframes = []
    try:
        if args == "r":
            outframes = await r_frames(image, w, h, outframes)
        elif args == "l":
            outframes = await l_frames(image, w, h, outframes)
        elif args == "u":
            outframes = await ud_frames(image, w, h, outframes)
        elif args == "d":
            outframes = await ud_frames(image, w, h, outframes, flip=True)
        elif args == "s":
            outframes = await spin_frames(image, w, h, outframes)
        elif args == "i":
            outframes = await invert_frames(image, w, h, outframes)
    except Exception as e:
        return await eod(legendevent, f"**Error**\n__{e}__")
    output = io.BytesIO()
    output.name = "Output.gif"
    outframes[0].save(output, save_all=True, append_images=outframes[1:], duration=0.7)
    output.seek(0)
    with open("Output.gif", "wb") as outfile:
        outfile.write(output.getbuffer())
    final = os.path.join(Config.TEMP_DIR, "output.gif")
    output = await vid_to_gif("Output.gif", final)
    if output is None:
        await eod(
            legendevent,
            "__There was some error in the media. I can't format it to gif.__",
        )
        for i in [final, "Output.gif", imag[1]]:
            if os.path.exists(i):
                os.remove(i)
        return
    LEGEND = await event.client.send_file(event.chat_id, output, reply_to=reply)
    await _legendutils.unsavegif(event, LEGEND)
    await legendevent.delete()
    for i in [final, "Output.gif", imag[1]]:
        if os.path.exists(i):
            os.remove(i)


@legend.legend_cmd(
    pattern="vtog ?([0-9.]+)?$",
    command=("vtog", menu_category),
    info={
        "header": "Reply this command to a video to convert it to gif.",
        "description": "By default speed will be 1x",
        "usage": "{tr}vtog <speed>",
    },
)
async def _(event):
    "Reply this command to a video to convert it to gif."
    reply = await event.get_reply_message()
    mediatype = media_type(event)
    if mediatype and mediatype != "video":
        return await eod(event, "__Reply to video to convert it to gif__")
    args = event.pattern_match.group(1)
    if not args:
        args = 2.0
    else:
        try:
            args = float(args)
        except ValueError:
            args = 2.0
    legendevent = await eor(event, "__🎞Converting into Gif..__")
    inputfile = await reply.download_media()
    outputfile = os.path.join(Config.TEMP_DIR, "vidtogif.gif")
    result = await vid_to_gif(inputfile, outputfile, speed=args)
    if result is None:
        return await eod(event, "__I couldn't convert it to gif.__")
    LEGEND = await event.client.send_file(event.chat_id, result, reply_to=reply)
    await _legendutils.unsavegif(event, LEGEND)
    await legendevent.delete()
    for i in [inputfile, outputfile]:
        if os.path.exists(i):
            os.remove(i)
