# collage plugin for LegendUserBot by @LEGEND_K_BOY

# Copyright (C) 2020 Alfiananda P.A
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.import os

import os

from userbot import legend

from ..core.managers import eod, eor
from ..helpers import reply_id
from ..helpers.utils import _legendutils
from . import make_gif

menu_category = "utils"


@legend.legend_cmd(
    pattern="collage(?:\s|$)([\s\S]*)",
    command=("collage", menu_category),
    info={
        "header": "To create collage from still images extracted from video/gif.",
        "description": "Shows you the grid image of images extracted from video/gif. you can customize the Grid size by giving integer between 1 to 9 to cmd by default it is 3",
        "usage": "{tr}collage <1-9> <reply to  ani sticker/mp4.",
    },
)
async def collage(event):
    "To create collage from still images extracted from video/gif."
    legendinput = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    legendid = await reply_id(event)
    event = await eor(event, "```Wait A Minute Its Collaging😁```")
    if not (reply and (reply.media)):
        await event.edit("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    legendsticker = await reply.download_media(file="./temp/")
    if not legendsticker.endswith((".mp4", ".mkv", ".tgs")):
        os.remove(legendsticker)
        await event.edit("`Media format is not supported...`")
        return
    if legendinput:
        if not legendinput.isdigit():
            os.remove(legendsticker)
            await event.edit("`You input is invalid, check help`")
            return
        legendinput = int(legendinput)
        if not 0 < legendinput < 10:
            os.remove(legendsticker)
            await event.edit(
                "`Why too big grid you cant see images, use size of grid between 1 to 9`"
            )
            return
    else:
        legendinput = 3
    if legendsticker.endswith(".tgs"):
        hmm = await make_gif(event, legendsticker)
        if hmm.endswith(("@tgstogifbot")):
            os.remove(legendsticker)
            return await event.edit(hmm)
        collagefile = hmm
    else:
        collagefile = legendsticker
    endfile = "./temp/collage.png"
    legendcmd = f"vcsi -g {legendinput}x{legendinput} '{collagefile}' -o {endfile}"
    stdout, stderr = (await _legendutils.runcmd(legendcmd))[:2]
    if not os.path.exists(endfile):
        for files in (legendsticker, collagefile):
            if files and os.path.exists(files):
                os.remove(files)
        return await eod(
            event, "`media is not supported or try with smaller grid size`", 5
        )

    await event.client.send_file(
        event.chat_id,
        endfile,
        reply_to=legendid,
    )
    await event.delete()
    for files in (legendsticker, collagefile, endfile):
        if files and os.path.exists(files):
            os.remove(files)
