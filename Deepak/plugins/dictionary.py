# Urban Dictionary for LegendDeepak by @LEGEND_K_BOY

from Deepak import legend

from ..core.logger import logging
from ..core.managers import eod, eor
from ..helpers import AioHttp
from ..helpers.utils import _format

LOGS = logging.getLogger(__name__)
menu_category = "utils"


@legend.legend_cmd(
    pattern="ud ([\s\S]*)",
    command=("ud", menu_category),
    info={
        "header": "To fetch meaning of the given word from urban dictionary.",
        "usage": "{tr}ud <word>",
    },
)
async def _(event):
    "To fetch meaning of the given word from urban dictionary."
    word = event.pattern_match.group(1)
    try:
        response = await AioHttp().get_json(
            f"http://api.urbandictionary.com/v0/define?term={word}",
        )
        word = response["list"][0]["word"]
        definition = response["list"][0]["definition"]
        example = response["list"][0]["example"]
        result = "**Text: {}**\n**Meaning:**\n`{}`\n\n**Example:**\n`{}`".format(
            _format.replacetext(word),
            _format.replacetext(definition),
            _format.replacetext(example),
        )
        await eor(event, result)
    except Exception as e:
        await eod(
            event,
            text="`The Urban Dictionary API could not be reached`",
        )
        LOGS.info(e)


"""
@legend.legend_cmd(
    pattern="meaning ([\s\S]*)",
    command=("meaning", menu_category),
    info={
        "header": "To fetch meaning of the given word from dictionary.",
        "usage": "{tr}meaning <word>",
    },
)
async def _(event):
    "To fetch meaning of the given word from dictionary."
    input_str = event.pattern_match.group(1)
    input_url = "https://bots.shrimadhavuk.me/dictionary/?s={}".format(input_str)
    headers = {"USER-AGENT": "UniBorg"}
    caption_str = f"Meaning of __{input_str}__\n"
    try:
        response = requests.get(input_url, headers=headers).json()
        pronounciation = response.get("p")
        meaning_dict = response.get("lwo")
        for current_meaning in meaning_dict:
            current_meaning_type = current_meaning.get("type")
            current_meaning_definition = current_meaning.get("definition")
            caption_str += (
                f"**{current_meaning_type}**: {current_meaning_definition}\n\n"
            )
    except Exception as e:
        caption_str = str(e)
    reply_msg_id = event.message.id
    if event.reply_to_msg_id:
        reply_msg_id = event.reply_to_msg_id
    try:
        await event.client.send_file(
            event.chat_id,
            pronounciation,
            caption=f"Pronounciation of __{input_str}__",
            force_document=False,
            reply_to=reply_msg_id,
            allow_cache=True,
            voice_note=True,
            silent=True,
            supports_streaming=True,
        )
    except:
        pass
    await event.edit(caption_str)
"""
