from userbot import legend

from ..core.managers import eor
from ..helpers.utils import _format

menu_category = "tools"

# yaml_format is ported from uniborg
@legend.legend_cmd(
    pattern="json$",
    command=("json", menu_category),
    info={
        "header": "To get details of that message in json format.",
        "usage": "{tr}json reply to message",
    },
)
async def _(event):
    "To get details of that message in json format."
    legendevent = await event.get_reply_message() if event.reply_to_msg_id else event
    the_real_message = legendevent.stringify()
    await eor(event, the_real_message, parse_mode=_format.parse_pre)


@legend.legend_cmd(
    pattern="yaml$",
    command=("yaml", menu_category),
    info={
        "header": "To get details of that message in yaml format.",
        "usage": "{tr}yaml reply to message",
    },
)
async def _(event):
    "To get details of that message in yaml format."
    legendevent = await event.get_reply_message() if event.reply_to_msg_id else event
    the_real_message = _format.yaml_format(legendevent)
    await eor(event, the_real_message, parse_mode=_format.parse_pre)
