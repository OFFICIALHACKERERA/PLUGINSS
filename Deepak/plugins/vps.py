import asyncio
import glob
import os

from userbot import legend

from ..core.managers import eor
from ..helpers.utils import _legendutils

menu_category = "tools"


# ============================@ Constants @===============================
config = "./config.py"
var_checker = [
    "APP_ID",
    "PM_LOGGER_GROUP_ID",
    "PRIVATE_CHANNEL_BOT_API_ID",
    "PRIVATE_GROUP_BOT_API_ID",
]
exts = ["jpg", "png", "webp", "webm", "m4a", "mp4", "mp3", "tgs"]

cmds = [
    "rm -rf downloads",
    "mkdir downloads",
]
# ========================================================================


vlist = [
    "SUDO_USERS",
]


@legend.legend_cmd(
    pattern="var([\s\S]*)",
    command=("var", menu_category),
    info={
        "header": "To check all config vars.",
        "usage": [
            "{tr}var",
        ],
        "examples": [
            "{tr}var",
        ],
    },
)
async def var(event):
    vnlist = "".join(f"{i}. `{each}`\n" for i, each in enumerate(vlist, start=1))
    await eod(
        event, f"**📑 Give correct var name from the list :\n\n**{vnlist}", time=120
    )


@legend.legend_cmd(
    pattern="(set|get|del) var ([\s\S]*)",
    command=("var", menu_category),
    info={
        "header": "To manage config vars.",
        "flags": {
            "set": "To set new var in vps or modify the old var",
            "get": "To show the already existing var value.",
            "del": "To delete the existing value",
        },
        "usage": [
            "{tr}set var <var name> <var value>",
            "{tr}get var <var name>",
            "{tr}del var <var name>",
        ],
        "examples": [
            "{tr}get var ALIVE_NAME",
        ],
    },
)
async def variable(event):  # sourcery no-metrics
    """
    Manage most of ConfigVars setting, set new var, get current var, or delete var...
    """
    if not os.path.exists(config):
        return await eor(event, "`There no Config file , You can't use this plugin.`")
    cmd = event.pattern_match.group(1)
    string = ""
    match = None
    with open(config, "r") as f:
        configs = f.readlines()
    if cmd == "get":
        lol = await eor(event, "`Getting information...`")
        await asyncio.sleep(1)
        variable = event.pattern_match.group(2).split()[0]
        for i in configs:
            if variable in i:
                _, val = i.split("= ")
                return await lol.edit("**ConfigVars**:" f"\n\n`{variable}` = `{val}`")
        await lol.edit(
            "**ConfigVars**:" f"\n\n__Error:\n-> __`{variable}`__ doesn't exists__"
        )
    elif cmd == "set":
        variable = "".join(event.text.split(maxsplit=2)[2:])
        lol = await eor(event, "`Setting information...`")
        if not variable:
            return await lol.edit("`.set var <ConfigVars-name> <value>`")
        value = "".join(variable.split(maxsplit=1)[1:])
        variable = "".join(variable.split(maxsplit=1)[0])
        if variable not in var_checker:
            value = f"'{value}'"
        if not value:
            return await lol.edit("`.set var <ConfigVars-name> <value>`")
        await asyncio.sleep(1)
        for i in configs:
            if variable in i:
                string += f"    {variable} = {value}\n"
                match = True
            else:
                string += f"{i}"
        if match:
            await lol.edit(f"`{variable}` **successfully changed to  ->  **`{value}`")
        else:
            string += f"    {variable} = {value}\n"
            await lol.edit(
                f"`{variable}`**  successfully added with value  ->  **`{value}`"
            )
        with open(config, "w") as f1:
            f1.write(string)
            f1.close()
        await event.client.reload(lol)
    if cmd == "del":
        lol = await eor(event, "`Deleting information...`")
        await asyncio.sleep(1)
        variable = event.pattern_match.group(2).split()[0]
        for i in configs:
            if variable in i:
                match = True
            else:
                string += f"{i}"
        with open(config, "w") as f1:
            f1.write(string)
            f1.close()
        if match:
            await lol.edit(f"`{variable}` **successfully deleted.**")
        else:
            await lol.edit(
                "**ConfigVars**:" f"\n\n__Error:\n-> __`{variable}`__ doesn't exists__"
            )
        await event.client.reload(lol)


@legend.legend_cmd(
    pattern="(re|clean)load$",
    command=("reload", menu_category),
    info={
        "header": "To reload your bot in vps/ similar to restart",
        "flags": {
            "re": "restart your bot without deleting junk files",
            "clean": "delete all junk files & restart",
        },
        "usage": [
            "{tr}reload",
            "{tr}cleanload",
        ],
    },
)
async def _(event):
    "To reload Your bot"
    cmd = event.pattern_match.group(1)
    lol = await eor(event, "`Wait 2-3 min, reloading...`")
    if cmd == "clean":
        for file in exts:
            removing = glob.glob(f"./*.{file}")
            for i in removing:
                os.remove(i)
        for i in cmds:
            await _legendutils.runcmd(i)
    await event.client.reload(lol)
