# ported from uniborg by @spechide
import asyncio
import io
import logging
import os
import time
from datetime import datetime

from userbot import legend

from ..Config import Config
from ..core.managers import eod, eor
from ..helpers import (
    _legendtools,
    fileinfo,
    humanbytes,
    media_type,
    progress,
    readable_time,
    reply_id,
    time_formatter,
)
from ..helpers.progress import progress
from ..helpers.utils import _legendtools

menu_category = "utils"


FF_MPEG_DOWN_LOAD_MEDIA_PATH = os.path.join(
    Config.TMP_DOWNLOAD_DIRECTORY, "LegendUserBot.media.ffmpeg"
)

FINISHED_PROGRESS_STR = Config.FINISHED_PROGRESS_STR
UN_FINISHED_PROGRESS_STR = Config.UNFINISHED_PROGRESS_STR
LOGGER = logging.getLogger(__name__)


async def convert_video(video_file, output_directory, crf, total_time, bot, message):
    # https://stackoverflow.com/a/13891070/4723940
    out_put_file_name = output_directory + "/" + str(round(time.time())) + ".mp4"
    progress = output_directory + "/" + "progress.txt"
    with open(progress, "w") as f:
        pass
    COMPRESSION_START_TIME = time.time()
    process = await asyncio.create_subprocess_shell(
        f'ffmpeg -hide_banner -loglevel quiet -progress {progress} -i """{video_file}""" -preset ultrafast -vcodec libx265 -crf {crf} -c:a copy """{out_put_file_name}"""',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    LOGGER.info("ffmpeg_process: " + str(process.pid))
    while process.returncode != 0:
        await asyncio.sleep(3)
        with open("./temp/progress.txt", "r+") as file:
            text = file.read()
            frame = re.findall("frame=(\d+)", text)
            time_in_us = re.findall("out_time_ms=(\d+)", text)
            progress = re.findall("progress=(\w+)", text)
            speed = re.findall("speed=(\d+\.?\d*)", text)
            if len(frame):
                frame = int(frame[-1])
            else:
                frame = 1
            if len(speed):
                speed = speed[-1]
            else:
                speed = 1
            if len(time_in_us):
                time_in_us = time_in_us[-1]
            else:
                time_in_us = 1
            if len(progress):
                if progress[-1] == "end":
                    LOGGER.info(progress[-1])
                    break
            time_formatter((time.time() - COMPRESSION_START_TIME))
            elapsed_time = int(time_in_us) / 1000000
            difference = math.floor((total_time - elapsed_time) / float(speed))
            ETA = "-"
            if difference > 0:
                ETA = time_formatter(difference)
            percentage = math.floor(elapsed_time * 100 / total_time)
            progress_str = "📊 **Progress :** {0}%\n[{1}{2}]".format(
                round(percentage, 2),
                "".join(
                    [FINISHED_PROGRESS_STR for i in range(math.floor(percentage / 10))]
                ),
                "".join(
                    [
                        UN_FINISHED_PROGRESS_STR
                        for i in range(10 - math.floor(percentage / 10))
                    ]
                ),
            )
            stats = (
                f"📦️ **Compressing CRF-{crf}**\n\n"
                f"⏰️ **ETA :** {ETA}\n\n"
                f"{progress_str}\n"
            )
            try:
                await message.edit(text=stats)
            except Exception:
                pass
    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    return None


# https://github.com/Nekmo/telegram-upload/blob/master/telegram_upload/video.py#L26


async def cult_small_video(
    video_file, output_directory, start_time, end_time, out_put_file_name=None
):
    # https://stackoverflow.com/a/13891070/4723940
    out_put_file_name = out_put_file_name or os.path.join(
        output_directory, f"{round(time.time())}.mp4"
    )
    process = await asyncio.create_subprocess_shell(
        # stdout must a pipe to be accessible as process.stdout
        f'ffmpeg -i """{video_file}""" -ss {start_time} -to {end_time} -async 1 -strict -2 """{out_put_file_name}"""',
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    # Wait for the subprocess to finish
    await process.communicate()
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    return None


@legend.legend_cmd(
    pattern="(|f)compress(?:\s|$)([\s\S]*)",
    command=("compress", menu_category),
    info={
        "header": "Compress the video file.",
        "description": "Will compress the replied video, if not replied to video it will check any video saved by .ffmpegsave or not.",
        "flags": {
            "f": "To Force file the compressed video.",
        },
        "note": "For quality of compress choose CRF value [ 0 - 51 ]\nHigher crf value = less video size = low on quality.\nIf no crf given it will use default value 23.",
        "usage": [
            "{tr}compress < 0 - 51 >",
            "{tr}fcompress < 0 - 51 >",
        ],
        "examples": [
            "{tr}compress",
            "{tr}fcompress",
            "{tr}compress 35",
            "{tr}fcompress 35",
        ],
    },
)
async def ffmpeg_compress(event):
    "Compress the video file."
    crf = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    cmd = event.pattern_match.group(1).lower()
    reply_message = await event.get_reply_message()
    start = datetime.now()
    if not crf:
        crf = "23"
    dlpath = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "swt.media.ffmpeg")
    if not reply_message or not reply_message.media:
        if os.path.exists(FF_MPEG_DOWN_LOAD_MEDIA_PATH):
            media = (await fileinfo(FF_MPEG_DOWN_LOAD_MEDIA_PATH))["type"]
            if media not in ["Video"]:
                return await eod(event, "`Only Video files are supported`")
            dlpath = FF_MPEG_DOWN_LOAD_MEDIA_PATH
            legendevent = await eod(event, "`Processing...`")
            delete = False
        else:
            await eod(event, "`Reply to Video file or save video by .ffmpegsave`")
    elif reply_message:
        media = media_type(reply_message)
        if media not in ["Video", "Round Video", "Gif"]:
            return await eod(event, "`Only Video files are supported`")
        legendevent = await eor(event, "`Saving the file...`")
        try:
            c_time = time.time()
            dl = io.FileIO(dlpath, "a")
            await event.client.fast_download_file(
                location=reply_message.document,
                out=dl,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, legendevent, c_time, "Trying to download")
                ),
            )
            dl.close()
        except Exception as e:
            await eor(legendevent, f"**Error:**\n`{e}`")
        else:
            await eor(legendevent, "`Processing...`")
            delete = True
    else:
        await eod(event, "`Reply to video file`")
    old = await fileinfo(dlpath)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    cstart = datetime.now()
    compress = await convert_video(
        dlpath, "./temp", crf, old["duration"], legend, legendevent
    )
    cend = datetime.now()
    cms = (cend - cstart).seconds
    if delete:
        os.remove(dlpath)
    if compress:
        new = await fileinfo(compress)
        osize = old["size"]
        nsize = new["size"]
        cap = f"**Old Size:** `{humanbytes(osize)}`\n**New Size:** `{humanbytes(nsize)}`\n**Compressed:** `{int(100-(nsize/osize*100))}%`\n\n**Time Taken:-**\n**Compression : **`{time_formatter(cms)}`"
        if cmd == "f":
            try:
                c_time = time.time()
                catt = await event.client.send_file(
                    event.chat_id,
                    compress,
                    thumb=thumb_image_path,
                    caption=cap,
                    force_document=True,
                    supports_streaming=True,
                    allow_cache=False,
                    reply_to=reply_to_id,
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(d, t, legendevent, c_time, "Trying to upload")
                    ),
                )
                os.remove(compress)
            except Exception as e:
                return await eod(legendevent, f"**Error : **`{e}`")
        else:
            thumb = await _legendtools.take_screen_shot(compress, "00:01")
            try:
                c_time = time.time()
                catt = await event.client.send_file(
                    event.chat_id,
                    compress,
                    caption=cap,
                    thumb=thumb,
                    force_document=False,
                    supports_streaming=True,
                    allow_cache=False,
                    reply_to=reply_to_id,
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(d, t, legendevent, c_time, "Trying to upload")
                    ),
                )
                os.remove(compress)
            except Exception as e:
                return await eod(legendevent, f"**Error : **`{e}`")
    else:
        return await eod(legendevent, "**ERROR :: Unalble to Compress**")
    await legendevent.delete()
    end = datetime.now()
    ms = (end - start).seconds
    cap += f"\n**Total :** `{time_formatter(ms)}`"
    await eor(catt, cap)


@legend.legend_cmd(
    pattern="ffmpegsave$",
    command=("ffmpegsave", menu_category),
    info={
        "header": "Saves the media file in bot to trim mutliple times",
        "description": "Will download the replied media into the bot so that you an trim it as your needs.",
        "usage": "{tr}ffmpegsave <reply>",
    },
)
async def ff_mpeg_trim_cmd(event):
    "Saves the media file in bot to trim mutliple times"
    mpath = event.pattern_match.group(1)
    if not os.path.exists(FF_MPEG_DOWN_LOAD_MEDIA_PATH):
        if mpath and os.path.exists(mpath):
            media = (await fileinfo(mpath))["type"]
            if media not in ["Video", "Audio"]:
                return await eod(event, "`Only media files are supported`", 5)
            await _catutils.runcmd(f"cp -r {mpath} {FF_MPEG_DOWN_LOAD_MEDIA_PATH}")
            return await eor(event, f"Saved file to `{FF_MPEG_DOWN_LOAD_MEDIA_PATH}`")
        if reply_message := await event.get_reply_message():
            start = datetime.now()
            media = media_type(reply_message)
            if media not in ["Video", "Audio", "Voice", "Round Video", "Gif"]:
                return await eod(event, "`Only media files are supported`", 5)
            legendevent = await eor(event, "`Saving the file...`")
            try:
                c_time = time.time()
                dl = io.FileIO(FF_MPEG_DOWN_LOAD_MEDIA_PATH, "a")
                await event.client.fast_download_file(
                    location=reply_message.document,
                    out=dl,
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(d, t, legendevent, c_time, "trying to download")
                    ),
                )
                dl.close()
            except Exception as e:
                await eor(legendevent, f"**Error:**\n`{e}`")
            else:
                end = datetime.now()
                ms = (end - start).seconds
                await eor(
                    legendevent,
                    f"Saved file to `{FF_MPEG_DOWN_LOAD_MEDIA_PATH}` in `{ms}` seconds.",
                )
        else:
            await eod(event, "`Reply to a any media file`")
    else:
        await eod(
            event,
            "A media file already exists in path. Please remove the media and try again!\n`.ffmpegclear`",
        )


@legend.legend_cmd(
    pattern="vtrim(?:\s|$)([\s\S]*)",
    command=("vtrim", menu_category),
    info={
        "header": "Trims the saved media with specific given time internval and outputs as video if it is video",
        "description": "Will trim the saved media with given given time interval.",
        "note": "if you haven't mentioned time interval and just time then will send screenshot at that location.",
        "usage": "{tr}vtrim <time interval>",
        "examples": "{tr}vtrim 00:00 00:10",
    },
)
async def ff_mpeg_trim_cmd(event):
    "Trims the saved media with specific given time internval and outputs as video if it is video"
    if not os.path.exists(FF_MPEG_DOWN_LOAD_MEDIA_PATH):
        return await eod(
            event,
            f"a media file needs to be download, and save to the following path: `{FF_MPEG_DOWN_LOAD_MEDIA_PATH}`",
        )
    reply_to_id = await reply_id(event)
    legendevent = await eor(event, "`Triming the media......`")
    current_message_text = event.raw_text
    cmt = current_message_text.split(" ")
    start = datetime.now()
    if len(cmt) == 3:
        # output should be video
        cmd, start_time, end_time = cmt
        o = await cult_small_video(
            FF_MPEG_DOWN_LOAD_MEDIA_PATH,
            Config.TMP_DOWNLOAD_DIRECTORY,
            start_time,
            end_time,
        )
        if o is None:
            return await eod(legendevent, "**Error : **`Can't complete the process`")
        try:
            c_time = time.time()
            await event.client.send_file(
                event.chat_id,
                o,
                caption=" ".join(cmt[1:]),
                force_document=False,
                supports_streaming=True,
                allow_cache=False,
                reply_to=reply_to_id,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, legendevent, c_time, "trying to upload")
                ),
            )
            os.remove(o)
        except Exception as e:
            return await eod(legendevent, f"**Error : **`{e}`")
    elif len(cmt) == 2:
        # output should be image
        cmd, start_time = cmt
        o = await _legendtools.take_screen_shot(
            FF_MPEG_DOWN_LOAD_MEDIA_PATH, start_time
        )
        if o is None:
            return await eod(legendevent, "**Error : **`Can't complete the process`")
        try:
            c_time = time.time()
            await event.client.send_file(
                event.chat_id,
                o,
                caption=" ".join(cmt[1:]),
                force_document=True,
                supports_streaming=True,
                allow_cache=False,
                reply_to=event.message.id,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, legendevent, c_time, "trying to upload")
                ),
            )
            os.remove(o)
        except Exception as e:
            return await eod(legendevent, f"**Error : **`{e}`")
    else:
        await eod(legendevent, "RTFM")
        return
    end = datetime.now()
    ms = (end - start).seconds
    await eod(legendevent, f"`Completed Process in {ms} seconds`", 3)


@legend.legend_cmd(
    pattern="atrim(?:\s|$)([\s\S]*)",
    command=("atrim", menu_category),
    info={
        "header": "Trims the saved media with specific given time internval and outputs as audio",
        "description": "Will trim the saved media with given given time interval. and output only audio part",
        "usage": "{tr}atrim <time interval>",
        "examples": "{tr}atrim 00:00 00:10",
    },
)
async def ff_mpeg_trim_cmd(event):
    "Trims the saved media with specific given time internval and outputs as audio"
    if not os.path.exists(FF_MPEG_DOWN_LOAD_MEDIA_PATH):
        return await eod(
            event,
            f"a media file needs to be download, and save to the following path: `{FF_MPEG_DOWN_LOAD_MEDIA_PATH}`",
        )
    reply_to_id = await reply_id(event)
    legendevent = await eor(event, "`Triming the media...........`")
    current_message_text = event.raw_text
    cmt = current_message_text.split(" ")
    start = datetime.now()
    out_put_file_name = os.path.join(
        Config.TMP_DOWNLOAD_DIRECTORY, f"{round(time.time())}.mp3"
    )

    if len(cmt) == 3:
        cmd, start_time, end_time = cmt
    else:
        start_time = "00:00"
        duration = (await fileinfo(FF_MPEG_DOWN_LOAD_MEDIA_PATH))["duration"]
        end_time = readable_time(duration)
    o = await cult_small_video(
        FF_MPEG_DOWN_LOAD_MEDIA_PATH,
        Config.TMP_DOWNLOAD_DIRECTORY,
        start_time,
        end_time,
        out_put_file_name,
    )
    if o is None:
        return await eod(legendevent, "**Error : **`Can't complete the process`")
    try:
        c_time = time.time()
        await event.client.send_file(
            event.chat_id,
            o,
            caption=" ".join(cmt[1:]),
            force_document=False,
            supports_streaming=True,
            allow_cache=False,
            reply_to=reply_to_id,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, legendevent, c_time, "trying to upload")
            ),
        )
        os.remove(o)
    except Exception as e:
        return await eod(legendevent, f"**Error : **`{e}`")
    end = datetime.now()
    ms = (end - start).seconds
    await eod(legendevent, f"`Completed Process in {ms} seconds`", 3)


@legend.legend_cmd(
    pattern="ffmpegclear$",
    command=("ffmpegclear", menu_category),
    info={
        "header": "Deletes the saved media so you can save new one",
        "description": "Only after deleting the old saved file you can add new file",
        "usage": "{tr}ffmpegclear",
    },
)
async def ff_mpeg_trim_cmd(event):
    "Deletes the saved media so you can save new one"
    if not os.path.exists(FF_MPEG_DOWN_LOAD_MEDIA_PATH):
        await eod(event, "`There is no media saved in bot for triming`")
    else:
        os.remove(FF_MPEG_DOWN_LOAD_MEDIA_PATH)
        await eod(
            event,
            "`The media saved in bot for triming is deleted now . you can save now new one `",
        )
