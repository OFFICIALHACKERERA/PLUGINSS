from datetime import datetime

from telethon import Button

from userbot import Config, legend

from ..core.logger import logging
from ..helpers import reply_id
from ..plugins import mention
from ..sql_helper.bot_blacklists import check_is_black_list
from ..sql_helper.globals import gvarstatus
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)

menu_category = "bot"
botusername = Config.BOT_USERNAME


@legend.bot_cmd(
    pattern=f"^/ping({botusername})?([\s]+)?$",
    incoming=True,
)
async def bot_start(event):
    chat = await event.get_chat()
    await legend.get_me()
    if check_is_black_list(chat.id):
        return
    reply_to = await reply_id(event)
    buttons = [(Button.url("⚜ Lêɠêɳ̃dẞø† ⚜", "https://t.me/LegendBot_XD"))]
    PM_IMG = (
        gvarstatus("BOT_PING_PIC")
        or "https://telegra.ph/file/5c898421fdef6f53aab0a.jpg"
    )
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    pm_caption = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{mention}』"
    try:
        await event.client.send_file(
            chat.id,
            PM_IMG,
            caption=pm_caption,
            link_preview=False,
            buttons=buttons,
            reply_to=reply_to,
        )
    except Exception as e:
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"**Error**\nThere was a error while using **alive**. `{e}`",
            )
