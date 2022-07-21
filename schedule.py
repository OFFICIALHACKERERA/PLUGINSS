from asyncio import sleep

from userbot import legend

menu_category = "utils"


@legend.legend_cmd(
    pattern="schd (\d*) ([\s\S]*)",
    command=("schd", menu_category),
    info={
        "header": "To schedule a message after given time(in seconds).",
        "usage": "{tr}schd <time_in_seconds>  <message to send>",
        "examples": "{tr}schd 120 hello",
    },
)
async def _(event):
    "To schedule a message after given time"
    legend = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = legend[1]
    ttl = int(legend[0])
    await event.delete()
    await sleep(ttl)
    await event.respond(message)
