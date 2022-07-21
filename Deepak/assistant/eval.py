import io
import sys
import traceback

from userbot import Config, legend

from ..core.logger import logging

LOGS = logging.getLogger(__name__)

menu_category = "bot"
botusername = Config.BOT_USERNAME


async def aexec(code, event):
    exec(
        f"async def __aexec(e, client): "
        + "\n message = event = e"
        + "\n reply = await event.get_reply_message()"
        + "\n chat = (await event.get_chat()).id"
        + "".join(f"\n {l}" for l in code.split("\n")),
    )

    return await locals()["__aexec"](event, event.client)


@legend.bot_cmd(
    pattern=f"^/eval?([\s]+)?$",
    incoming=True,
    func=lambda e: e.sender_id == Config.OWNER_ID,
)
async def bo_ll(event):
    cmd = await event.get_reply_message()
    if not cmd:
        return await event.reply("Reply to a message for Eval !")
    # cmd = event.text.split(" ", maxsplit=1)[1]
    if cmd in (
        "LEGEND_STRING",
        "session",
        "BOT_TOKEN",
        "HEROKU_API_KEY",
        "DeleteAccountRequest",
    ):
        return await event.reply(
            "Sorry, This Is Sensitive Data I Cant Send It To Public.& Reported to Admin Of [LegendBot](https://t.me/LegendBot_AI) Group admin. & Dont Try To Send Any Information Without Knowing Anything."
        )
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = "**Eval:**\n`{}`\n\n**Output:**\n`{}`".format(cmd, evaluation)
    MAX_MESSAGE_SIZE_LIMIT = 4095
    if len(final_output) > MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await event.client.send_file(
                chat.id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id,
            )

    else:
        await event.reply(final_output)
