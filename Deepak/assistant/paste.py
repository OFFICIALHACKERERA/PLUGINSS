from telethon.utils import get_extension

from Deepak import legend

from ..Config import Config
from ..helpers.tools import media_type
from ..helpers.utils import pastetext

botusername = Config.BOT_USERNAME


@legend.bot_cmd(
    pattern=f"^/paste({botusername})?([\s]+)?$",
    incoming=True,
)
async def pasta(event):
    reply = await event.get_reply_message()
    pastetype = "p"
    extension = None
    if reply and reply.media:
        mediatype = media_type(reply)
        if mediatype == "Document":
            d_file_name = await event.client.download_media(reply, Config.TEMP_DIR)
            if extension is None:
                extension = get_extension(reply.document)
            with open(d_file_name, "r") as f:
                text_to_print = f.read()
    if extension and extension.startswith("."):
        extension = extension[1:]
    try:
        response = await pastetext(text_to_print, pastetype, extension)
        if "error" in response:
            return await event.reply(
                "**Error while pasting text:**\n`Unable to process your request may be pastebins are down.`",
            )

        result = ""
        if pastebins[response["bin"]] != pastetype:
            result += f"<b>{get_key(pastetype)} is down, So </b>"
        result += f"<b>Pasted to: <a href={response['url']}>{response['bin']}</a></b>"
        if response["raw"] != "":
            result += f"\n<b>Raw link: <a href={response['raw']}>Raw</a></b>"
        await event.reply(result, link_preview=False, parse_mode="html")
    except Exception as e:
        await event.reply(f"**Error while pasting text:**\n`{e}`")
