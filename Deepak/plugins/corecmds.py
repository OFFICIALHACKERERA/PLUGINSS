import os
from datetime import datetime
from pathlib import Path

from ..Config import Config
from ..utils import load_module, remove_plugin
from . import (
    CMD_HELP,
    CMD_LIST,
    SUDO_LIST,
    chnl_link,
    eod,
    eor,
    hmention,
    legend,
    mention,
    reply_id,
)

menu_category = "tools"

DELETE_TIMEOUT = 5
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")


def plug_checker(plugin):
    plug_path = f"./Deepak/plugins/{plugin}.py"
    if not os.path.exists(plug_path):
        plug_path = f"./xtraplugins/{plugin}.py"
    if not os.path.exists(plug_path):
        plug_path = f"./Deepak/assistant/{plugin}.py"
    return plug_path


@legend.legend_cmd(
    pattern="install$",
    command=("install", menu_category),
    info={
        "header": "To install an external plugin.",
        "description": "Reply to any external plugin(supported by LegendBot) to install it in your bot.",
        "usage": "{tr}install",
    },
)
async def install(event):
    "To install an external plugin."
    b = 1
    owo = event.text[9:]
    legend = await eor(event, "__Installing.__")
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "./Deepak/plugins/",  # pylint:disable=E0602
                )
            )
            op = open(downloaded_file_name, "r")
            rd = op.read()
            op.close()
            try:
                if "session" in rd:
                    os.remove(downloaded_file_name)
                    await legend.edit(
                        f"**⚠️ WARNING !!** \n\n__Replied plugin file contains some harmful codes__."
                    )
                    return
                elif "os.environ" in rd:
                    os.remove(downloaded_file_name)
                    await legend.edit(
                        f"**⚠️ WARNING !!** \n\n__Replied plugin file contains some harmful codes__."
                    )
                    return
                elif "(" not in downloaded_file_name:
                    path1 = Path(downloaded_file_name)
                    shortname = path1.stem
                    load_module(shortname.replace(".py", ""))
                    if shortname in CMD_LIST:
                        string = "**Commands found in** `{}`\n".format(
                            (os.path.basename(downloaded_file_name))
                        )
                        for i in CMD_LIST[shortname]:
                            string += "  •  `" + i
                            string += "`\n"
                            if b == 1:
                                a = "__Installing..__"
                                b = 2
                            else:
                                a = "__Installing...__"
                                b = 1
                            await legend.edit(a)
                        return await legend.edit(
                            f"✅ **Installed module** :- `{shortname}` \n✨ BY :- {mention}\n\n{string}\n\n        ⚡ **[Lêɠêɳ̃dẞø†]({chnl_link})** ⚡",
                            link_preview=False,
                        )

                    return await legend.edit(
                        f"Installed module `{os.path.basename(downloaded_file_name)}`"
                    )
                else:
                    os.remove(downloaded_file_name)
                    return await eod(
                        legend,
                        f"**Failed to Install** \n`Error`, Module already installed",
                    )
            except Exception as e:
                await eod(legend, f"{e}")
                return os.remove(downloaded_file_name)
        except Exception as e:
            await eod(legend, f"**Failed to Install** \n`Error`\n{str(e)}")
            return os.remove(downloaded_file_name)


@legend.legend_cmd(
    pattern="load ([\s\S]*)",
    command=("load", menu_category),
    info={
        "header": "To load a plugin again. if you have unloaded it",
        "description": "To load a plugin again which you unloaded by {tr}unload",
        "usage": "{tr}load <plugin name>",
        "examples": "{tr}load markdown",
    },
)
async def load(event):
    "To load a plugin again. if you have unloaded it"
    shortname = event.pattern_match.group(1)
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await eod(event, f"`Successfully loaded {shortname}`", 10)
    except Exception as e:
        await eor(
            event,
            f"Could not load {shortname} because of the following error.\n{e}",
        )


@legend.legend_cmd(
    pattern="send ([\s\S]*)",
    command=("send", menu_category),
    info={
        "header": "To upload a plugin file to telegram chat",
        "usage": "{tr}send <plugin name>",
        "examples": "{tr}send markdown",
    },
)
async def send(event):
    "To uplaod a plugin file to telegram chat"
    reply_to_id = await reply_id(event)
    thumb = thumb_image_path if os.path.exists(thumb_image_path) else None
    input_str = event.pattern_match.group(1)
    the_plugin_file = plug_checker(input_str)
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        caat = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            thumb=thumb,
        )
        end = datetime.now()
        ms = (end - start).seconds
        await event.delete()
        await caat.edit(
            f"<b><i>➥⍟ Plugin Name :- {input_str} .</i></b>\n<b><i>➥⍟ Uploaded in {ms} seconds.</i></b>\n<b><i>➥⍟ Uploaded by :- {hmention}</i></b>",
            parse_mode="html",
        )
    else:
        await eor(event, f"__There Is no any file with name {input_str}__")


@legend.legend_cmd(
    pattern="upload ([\s\S]*)",
    command=("upload", menu_category),
    info={
        "header": "To unload a plugin temporarily.",
        "description": "You can load this unloaded plugin by restarting or using {tr}load cmd. Useful for cases like seting notes in rose bot({tr}unload markdown).",
        "usage": "{tr}unload <plugin name>",
        "examples": "{tr}unload markdown",
    },
)
async def unload(event):
    "To unload a plugin temporarily."
    shortname = event.pattern_match.group(1)
    try:
        remove_plugin(shortname)
        await eor(event, f"Unloaded {shortname} successfully")
    except Exception as e:
        await eor(event, f"Successfully unload {shortname}\n{e}")


@legend.legend_cmd(
    pattern="uninstall ([\s\S]*)",
    command=("uninstall", menu_category),
    info={
        "header": "To uninstall a plugin temporarily.",
        "description": "To stop functioning of that plugin and remove that plugin from bot.",
        "note": "To unload a plugin permanently from bot set NO_LOAD var in heroku with that plugin name, give space between plugin names if more than 1.",
        "usage": "{tr}uninstall <plugin name>",
        "examples": "{tr}uninstall markdown",
    },
)
async def unload(event):
    "To uninstall a plugin."
    shortname = event.pattern_match.group(1)
    path = plug_checker(shortname)
    if not os.path.exists(path):
        return await eod(event, f"There is no plugin with path {path} to uninstall it")
    os.remove(path)
    if shortname in CMD_LIST:
        CMD_LIST.pop(shortname)
    if shortname in SUDO_LIST:
        SUDO_LIST.pop(shortname)
    if shortname in CMD_HELP:
        CMD_HELP.pop(shortname)
    try:
        remove_plugin(shortname)
        await eor(event, f"{shortname} is Uninstalled successfully")
    except Exception as e:
        await eor(event, f"Successfully uninstalled {shortname}\n{e}")
    if shortname in PLG_INFO:
        for cmd in PLG_INFO[shortname]:
            CMD_INFO.pop(cmd)
        PLG_INFO.pop(shortname)
