import asyncio
import io
import os
import pathlib
import subprocess
import time
from datetime import datetime
from pathlib import Path

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl import types
from telethon.utils import get_attributes

from userbot import legend

from ..Config import Config
from ..core.managers import eod, eor
from ..helpers import progress
from ..helpers.utils import reply_id

menu_category = "misc"

PATH = os.path.join("./temp", "temp_vid.mp4")
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
menu_category = "misc"
downloads = pathlib.Path("./downloads/").absolute()
NAME = "untitled"


class UPLOAD:
    def __init__(self):
        self.uploaded = 0


UPLOAD_ = UPLOAD()


async def lst_of_files(path):
    files = []
    for dirname, dirnames, filenames in os.walk(path):
        # print path to all filenames.
        for filename in filenames:
            files.append(os.path.join(dirname, filename))
    return files


def get_video_thumb(file, output=None, width=320):
    output = file + ".jpg"
    metadata = extractMetadata(createParser(file))
    cmd = [
        "ffmpeg",
        "-i",
        file,
        "-ss",
        str(int((0, metadata.get("duration").seconds)[metadata.has("duration")] / 2)),
        # '-filter:v', 'scale={}:-1'.format(width),
        "-vframes",
        "1",
        output,
    ]
    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    p.communicate()
    if not p.returncode and os.path.lexists(file):
        return output


def sortthings(contents, path):
    lolsort = []
    contents.sort()
    for file in contents:
        swtpath = os.path.join(path, file)
        if os.path.isfile(swtpath):
            lolsort.append(file)
    for file in contents:
        swtpath = os.path.join(path, file)
        if os.path.isdir(swtpath):
            lolsort.append(file)
    return lolsort


async def _get_file_name(path: pathlib.Path, full: bool = True) -> str:
    return str(path.absolute()) if full else path.stem + path.suffix


async def upload(path, event, udir_event, sweetiepe=None):  # sourcery no-metrics
    sweetiepe = sweetiepe or False
    reply_to_id = await reply_id(event)
    if os.path.isdir(path):
        await event.client.send_message(event.chat_id, f"**Folder : **`{path}`")
        Files = os.listdir(path)
        Files = sortthings(Files, path)
        for file in Files:
            swtpath = os.path.join(path, file)
            await upload(Path(swtpath), event, udir_event)
    elif os.path.isfile(path):
        fname = os.path.basename(path)
        c_time = time.time()
        thumb = thumb_image_path if os.path.exists(thumb_image_path) else None
        f = path.absolute()
        attributes, mime_type = get_attributes(str(f))
        ul = io.open(f, "rb")
        uploaded = await event.client.fast_upload_file(
            file=ul,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, event, c_time, "trying to upload", file_name=fname)
            ),
        )
        ul.close()
        media = types.InputMediaUploadedDocument(
            file=uploaded,
            mime_type=mime_type,
            attributes=attributes,
            force_file=sweetiepe,
            thumb=await event.client.upload_file(thumb) if thumb else None,
        )
        await event.client.send_file(
            event.chat_id,
            file=media,
            caption=f"**File Name : **`{fname}`",
            reply_to=reply_to_id,
        )

        UPLOAD_.uploaded += 1


@legend.legend_cmd(
    pattern="upload( -f)? ([\s\S]*)",
    command=("upload", menu_category),
    info={
        "header": "To upload files from server to telegram",
        "description": "To upload files which are downloaded in your bot.",
        "flags": {"f": "Use this to make upload files as documents."},
        "examples": [
            "{tr}upload <file/folder path>",
            "{tr}upload -f ./downloads",
        ],
    },
)
async def uploadir(event):
    "To upload files to telegram."
    input_str = event.pattern_match.group(2)
    path = Path(input_str)
    start = datetime.now()
    type = event.pattern_match.group(1)
    type = bool(type)
    if not os.path.exists(path):
        return await eor(
            event,
            f"`there is no such directory/file with the name {path} to upload`",
        )
    udir_event = await eor(event, "Uploading....")
    if os.path.isdir(path):
        await eor(udir_event, f"`Gathering file details in directory {path}`")
        UPLOAD_.uploaded = 0
        await upload(path, event, udir_event, sweetiepe=type)
        end = datetime.now()
        ms = (end - start).seconds
        await eod(
            udir_event,
            f"`Uploaded {UPLOAD_.uploaded} files successfully in {ms} seconds. `",
        )
    else:
        await eor(udir_event, "`Uploading file .....`")
        UPLOAD_.uploaded = 0
        await upload(path, event, udir_event, sweetiepe=type)
        end = datetime.now()
        ms = (end - start).seconds
        await eod(
            udir_event,
            f"`Uploaded file {path} successfully in {ms} seconds. `",
        )
