from Deepak import legend

from ..core.managers import eod, eor

menu_category = "Extra"


@legend.legend_cmd(
    pattern="upper(?: |$)([\s\S]*)",
    command=("upper", menu_category),
    info={
        "header": "Text operation change to upper text",
        "usage": "{tr}upper <input text /reply to text>",
        "examples": "{tr}upper Reply to valid text or give valid text as input",
    },
)
async def some(event):
    """Text Format upper"""
    intxt = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not intxt and reply:
        intxt = reply.text
    if not intxt:
        return await eod(
            event, "**ಠ∀ಠ  Reply to valid text or give text as input...you moron!!**"
        )
    mystring = intxt.upper()
    await eor(event, mystring)


@legend.legend_cmd(
    pattern="lower(?: |$)([\s\S]*)",
    command=("lower", menu_category),
    info={
        "header": "Text operation change to lower text",
        "usage": "{tr}lower <input text /reply to text>",
        "examples": "{tr}lower Reply to valid text or give valid text as input",
    },
)
async def good(event):
    """Text Format lower"""
    intxt = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not intxt and reply:
        intxt = reply.text
    if not intxt:
        return await eod(
            event, "**ಠ∀ಠ  Reply to valid text or give text as input...you moron!!**"
        )
    mystring = intxt.lower()
    await eor(event, mystring)


@legend.legend_cmd(
    pattern="title(?: |$)([\s\S]*)",
    command=("title", menu_category),
    info={
        "header": "Text operation change to title text",
        "usage": "{tr}title<input text /reply to text>",
        "examples": "{tr}title Reply to valid text or give valid text as input",
    },
)
async def stuff(event):
    """Text Format title"""
    intxt = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not intxt and reply:
        intxt = reply.text
    if not intxt:
        return await eod(
            event, "**ಠ∀ಠ  Reply to valid text or give text as input...you moron!!**"
        )
    mystring = intxt.title()
    await eor(event, mystring)


@legend.legend_cmd(
    pattern="(|r)camel(?: |$)([\s\S]*)",
    command=("camel", menu_category),
    info={
        "header": "Text operation change to camel text",
        "usage": [
            "{tr}camel <input text /reply to text>",
            "{tr}rcamel <input text /reply to text>",
        ],
        "examples": [
            "{tr}camel Reply to valid text or give valid text as input",
            "{tr}rcamel Reply to valid text or give valid text as input",
        ],
    },
)
async def here(event):
    """Text Format camel"""
    cmd = event.pattern_match.group(1).lower()
    intxt = event.pattern_match.group(2)
    reply = await event.get_reply_message()
    if not intxt and reply:
        intxt = reply.text
    if not intxt:
        return await eod(
            event, "**ಠ∀ಠ  Reply to valid text or give text as input...you moron!!**"
        )
    if cmd == "r":
        bad = list(intxt.lower())[::2]
        legend = list(intxt.upper())[1::2]
    else:
        bad = list(intxt.upper())[::2]
        legend = list(intxt.lower())[1::2]
    mystring = "".join(f"{i}{j}" for i, j in zip(bad, legend))
    await eor(event, mystring)
