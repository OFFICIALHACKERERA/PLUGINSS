from telethon.utils import pack_bot_file_id

from Deepak import Config, legend

from ..core.logger import logging

LOGS = logging.getLogger(__name__)

menu_category = "bot"
botusername = Config.BOT_USERNAME


@legend.bot_cmd(
    pattern=f"^/id({botusername})?([\s]+)?$",
    incoming=True,
    func=lambda e: e.is_group,
)
async def bot_start(event):
    "To get id of the group or user."
    if event.reply_to_msg_id:
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await event.reply(
                f"❇ **Current Chat ID : **`{event.chat_id}`\n❇ **From User ID: **`{r_msg.sender_id}`\n**Media File ID: **`{bot_api_file_id}`",
            )

        else:
            await event.reply(
                f"**Current Chat ID : **`{event.chat_id}`\n**From User ID: **`{r_msg.sender_id}`",
            )

    else:
        await event.reply(f"**Current Chat ID : **`{event.chat_id}`")
