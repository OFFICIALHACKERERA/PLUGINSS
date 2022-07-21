import asyncio
import io
import os
import re
import time

import lyricsgenius
import requests
from ShazamAPI import Shazam
from telethon import types
from telethon.tl.types import DocumentAttributeAudio
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL
from yt_dlp.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

from userbot import legend

from ..Config import Config
from ..core.logger import logging
from ..core.managers import eod, eor
from ..helpers import progress
from ..helpers.tools import media_type
from ..helpers.utils import reply_id
from ..helpers.yt_helper import *
from . import mention

GENIUS = Config.GENIUS_API_TOKEN

menu_category = "utils"
LOGS = logging.getLogger(__name__)

perf = "LegendBot"


@legend.legend_cmd(
    pattern="lyrics(?:\s|$)([\s\S]*)",
    command=("lyrics", menu_category),
    info={
        "header": "Song lyrics searcher using genius api.",
        "description": "if you want to provide artist name with song name then use this format {tr}lyrics <artist name> - <song name> . if you use this format in your query then types won't work. by default it will show first query.",
        "flags": {
            "-l": "to get list of search lists.",
            "-g": "To get paticular song lyrics.",
        },
        "note": "For functioning of this command set the GENIUS_API_TOKEN in heroku. Get value from  https://genius.com/developers.",
        "usage": [
            "{tr}lyrics <artist name> - <song name>",
            "{tr}lyrics -l <song name>",
            "{tr}lyrics -n<song number> <song name>",
        ],
        "examples": [
            "{tr}lyrics Armaan Malik - butta bomma",
            "{tr}lyrics -l butta bomma",
            "{tr}lyrics -n2 butta bomma",
        ],
    },
)
async def lyrics(event):  # sourcery no-metrics
    "To fetch song lyrics"
    if GENIUS is None:
        return await eor(
            event,
            "`Set genius access token in heroku vars for functioning of this command\n》 VAR :- GENIUS_API_TOKEN\n》 Generate From:- https://genius.com/developers`",
        )
    match = event.pattern_match.group(1)
    songno = re.findall(r"-n\d+", match)
    listview = re.findall(r"-l", match)
    try:
        songno = songno[0]
        songno = songno.replace("-n", "")
        match = match.replace("-n" + songno, "")
        songno = int(songno)
    except IndexError:
        songno = 1
    if songno < 1 or songno > 10:
        return await eor(
            event,
            "`song number must be in between 1 to 10 use -l type to query results`",
        )
    match = match.replace("-l", "")
    listview = bool(listview)
    query = match.strip()
    genius = lyricsgenius.Genius(GENIUS)
    if "-" in query:
        args = query.split("-", 1)
        artist = args[0].strip(" ")
        song = args[1].strip(" ")
        legendevent = await eor(event, f"`Searching lyrics for {artist} - {song}...`")
        try:
            songs = genius.search_song(song, artist)
        except TypeError:
            songs = None
        if songs is None:
            return await legendevent.edit(f"Song **{artist} - {song}** not found!")
        result = f"**Search query**: \n`{artist} - {song}`\n\n```{songs.lyrics}```"
    else:
        legendevent = await eor(event, f"`Searching lyrics for {query}...`")
        response = genius.search_songs(query)
        msg = f"**The songs found for the given query:** `{query}`\n\n"
        if len(response["hits"]) == 0:
            return await eor(
                event, f"**I can't find lyrics for the given query: **`{query}`"
            )
        for i, an in enumerate(response["hits"], start=1):
            msg += f"{i}. `{an['result']['title']}`\n"
        if listview:
            result = msg
        else:
            result = f"**The song found for the given query:** `{query}`\n\n"
            if songno > len(response["hits"]):
                return await eor(
                    event,
                    f"**Invalid song selection for the query select proper number**\n{msg}",
                )
            songtitle = response["hits"][songno - 1]["result"]["title"]
            result += f"`{genius.search_song(songtitle).lyrics}`"
    await eor(legendevent, result)


@legend.legend_cmd(
    pattern="ytlink(?:\s|$)([\s\S]*)",
    command=("ytlink", menu_category),
    info={
        "header": "Get Link of query from youtube limit 7",
        "usage": "{tr}ytlink",
    },
)
async def ytlink(ytwala):
    "Get Link of query from youtube limit 7"
    query = ytwala.pattern_match.group(1)
    if not query:
        await eor(ytwala, "`Enter query to search`")
    await eor(ytwala, "`Processing...`")
    try:
        results = json.loads(YoutubeSearch(query, max_results=7).to_json())
    except KeyError:
        return await eor(ytwala, "Unable to find relevant search queries...")
    output = f"**Search Query:**\n`{query}`\n\n**Results:**\n\n"
    for i in results["videos"]:
        output += f"--> `{i['title']}`\nhttps://www.youtube.com{i['url_suffix']}\n\n"
    await eor(ytwala, output, link_preview=False)


@legend.legend_cmd(
    pattern="ssong(?:\s|$)([\s\S]*)",
    command=("ssong", menu_category),
    info={
        "header": "Search Song slow mode",
        "usage": "{tr}ssong",
    },
)
async def ssong(event):
    "Search Song slow mode"
    query = event.text[6:]
    max_results = 1
    if query == "":
        return await eod(event, "__Please give a song name to search.__")
    hell = await eor(event, f"__Searching for__ `{query}`")
    hel_ = await song_search(event, query, max_results, details=True)
    x, title, views, duration, thumb = hel_[0], hel_[1], hel_[2], hel_[3], hel_[4]
    thumb_name = f"thumb.jpg"
    thumbnail = requests.get(thumb, allow_redirects=True)
    open(thumb_name, "wb").write(thumbnail.content)
    url = x.replace("\n", "")
    try:
        await event.edit("**Fetching Song**")
        with YoutubeDL(song_opts) as somg:
            hell_data = somg.extract_info(url)
    except DownloadError as DE:
        return await eor(hell, f"`{str(DE)}`")
    except ContentTooShortError:
        return await eor(hell, "`The download content was too short.`")
    except GeoRestrictedError:
        return await eor(
            hell,
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`",
        )
    except MaxDownloadsReached:
        return await eor(hell, "`Max-downloads limit has been reached.`")
    except PostProcessingError:
        return await eor(hell, "`There was an error during post processing.`")
    except UnavailableVideoError:
        return await eor(hell, "`Media is not available in the requested format.`")
    except XAttrMetadataError as XAME:
        return await eor(hell, f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await eor(hell, "`There was an error during info extraction.`")
    c_time = time.time()
    await event.edit(
        f"**🎶 Preparing to upload song 🎶 :** \n\n{hell_data['title']} \n**By :** {hell_data['uploader']}"
    )
    await event.client.send_file(
        event.chat_id,
        f"{hell_data['id']}.mp3",
        supports_streaming=True,
        caption=f"**✘ Song -** `{title}` \n**✘ Views -** `{views}` \n**✘ Duration -** `{duration}` \n\n**✘ By :** {mention}",
        thumb=thumb_name,
        attributes=[
            DocumentAttributeAudio(
                duration=int(hell_data["duration"]),
                title=str(hell_data["title"]),
                performer=perf,
            )
        ],
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "Uploading..", f"{hell_data['title']}.mp3")
        ),
    )
    await event.delete()
    os.remove(f"{hell_data['id']}.mp3")


@legend.legend_cmd(
    pattern="vssong(?:\s|$)([\s\S]*)",
    command=("vssong", menu_category),
    info={
        "header": "Search video Song slow mode",
        "usage": "{tr}vssong",
    },
)
async def vssong(event):
    "Search video Song slow mode"
    query = event.text[7:]
    max_results = 1
    if query == "":
        return await eod(event, "__Please give a song name to search.__")
    hell = await eor(event, f"__Searching for__ `{query}`")
    hel_ = await song_search(event, query, max_results, details=True)
    x, title, views, duration, thumb = hel_[0], hel_[1], hel_[2], hel_[3], hel_[4]
    thumb_name = f"thumb.jpg"
    thumbnail = requests.get(thumb, allow_redirects=True)
    open(thumb_name, "wb").write(thumbnail.content)
    url = x.replace("\n", "")
    try:
        await event.edit("**Fetching Video**")
        with YoutubeDL(video_opts) as somg:
            hell_data = somg.extract_info(url)
    except DownloadError as DE:
        return await eor(hell, f"`{str(DE)}`")
    except ContentTooShortError:
        return await eor(hell, "`The download content was too short.`")
    except GeoRestrictedError:
        return await eor(
            hell,
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website.`",
        )
    except MaxDownloadsReached:
        return await eor(hell, "`Max-downloads limit has been reached.`")
    except PostProcessingError:
        return await eor(hell, "`There was an error during post processing.`")
    except UnavailableVideoError:
        return await eor(hell, "`Media is not available in the requested format.`")
    except XAttrMetadataError as XAME:
        return await eor(hell, f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await eor(hell, "`There was an error during info extraction.`")
    except Exception as e:
        return await eor(hell, e)
    c_time = time.time()
    await event.edit(
        f"**📺 Preparing to upload video 📺 :** \n\n{hell_data['title']}\n**By :** {hell_data['uploader']}"
    )
    await event.client.send_file(
        event.chat_id,
        f"{hell_data['id']}.mp4",
        supports_streaming=True,
        caption=f"**✘ Video :** `{title}` \n\n**✘ By :** {mention}",
        thumb=thumb_name,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "Uploading..", f"{hell_data['title']}.mp4")
        ),
    )
    await event.delete()
    os.remove(f"{hell_data['id']}.mp4")


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


@legend.legend_cmd(
    pattern="vsong(?:\s|$)([\s\S]*)",
    command=("vsong", menu_category),
    info={
        "header": "Video Search Song Fast Mode",
        "usage": "{tr}vsong",
    },
)
async def vsong(event):
    "Video Search Song Fast Mode"
    ydl_opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "age_limit": 25,
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    reply_to_id = await reply_id(event)
    m = await eor(event, "searching video song")
    query = event.text[6:]
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
        views = results[0]["views"]
    except Exception:
        await m.edit("𝐒𝐨𝐧𝐠 𝐍𝐨𝐭 𝐅𝐨𝐮𝐧𝐝.")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
    except Exception as e:
        await m.edit("**𝐘𝐨𝐮𝐭𝐮𝐛𝐞  𝐄𝐫𝐫𝐨𝐫 **")
        print(e)
    await event.client.send_file(
        event.chat_id,
        audio_file,
        supports_streaming=True,
        caption=f"**✘ Video Song -** `{title}` \n**✘ Views -** `{views}` \n**✘ Duration -** `{duration}` \n\n**✘ By :** {mention}",
        thumb=thumb_name,
        reply_to=reply_to_id,
    )
    await event.delete()
    os.remove(audio_file)
    os.remove(thumb_name)


@legend.legend_cmd(
    pattern="song(?:\s|$)([\s\S]*)",
    command=("song", menu_category),
    info={
        "header": "Search Audio Song Fast Mode",
        "usage": "{tr}song",
    },
)
async def song(event):
    "Search Audio Song Fast Mode"
    reply_to_id = await reply_id(event)
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    m = await eor(event, "searching song")
    query = event.text[6:]
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
        views = results[0]["views"]

    except Exception:
        m.edit("𝐒𝐨𝐧𝐠 🥀 𝐍𝐨𝐭 😔 𝐅𝐨𝐮𝐧𝐝.")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
    except Exception as e:
        m.edit("**𝐘𝐨𝐮𝐭𝐮𝐛𝐞  𝐄𝐫𝐫𝐨𝐫 ❌**")
        print(e)
    await event.client.send_file(
        event.chat_id,
        audio_file,
        supports_streaming=True,
        caption=f"**✘ Song -** `{title}` \n**✘ Views -** `{views}` \n**✘ Duration -** `{duration}` \n\n**✘ By :** {mention}",
        thumb=thumb_name,
        reply_to=reply_to_id,
    )
    await event.delete()
    os.remove(audio_file)
    os.remove(thumb_name)


@legend.legend_cmd(
    pattern="spic$",
    command=("spic", menu_category),
    info={
        "header": "To reverse search song.",
        "description": "Reverse search audio file using shazam api",
        "usage": "{tr}shazam <reply to voice/audio>",
    },
)
async def spic(event):
    "To reverse search song."
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or not mediatype or mediatype not in ["Voice", "Audio"]:
        return await eod(
            event, "__Reply to Voice clip or Audio clip to reverse search that song.__"
        )
    legendevent = await eor(event, "__Downloading the audio clip...__")
    try:
        for attr in getattr(reply.document, "attributes", []):
            if isinstance(attr, types.DocumentAttributeFilename):
                name = attr.file_name
        dl = io.FileIO(name, "a")
        await event.client.fast_download_file(
            location=reply.document,
            out=dl,
        )
        dl.close()
        mp3_fileto_recognize = open(name, "rb").read()
        shazam = Shazam(mp3_fileto_recognize)
        recognize_generator = shazam.recognizeSong()
        track = next(recognize_generator)[1]["track"]
    except Exception as e:
        LOGS.error(e)
        return await eod(
            legendevent, f"**Error while reverse searching song:**\n__{e}__"
        )

    image = track["images"]["background"]
    song = track["share"]["subject"]
    await event.client.send_file(
        event.chat_id, image, caption=f"**Song:** `{song}`", reply_to=reply
    )
    await legendevent.delete()
