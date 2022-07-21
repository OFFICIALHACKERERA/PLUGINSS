import asyncio

from Deepak import legend

from ..core.managers import eor

menu_category = "fun"


@legend.legend_cmd(
    pattern="^\:/$",
    command=("\:", menu_category),
    info={
        "header": "Animation command",
        "usage": "\:",
    },
)
async def kek(keks):
    "Animation command"
    keks = await eor(keks, ":\\")
    uio = ["/", "\\"]
    for i in range(15):
        await asyncio.sleep(0.5)
        txt = ":" + uio[i % 2]
        await keks.edit(txt)


@legend.legend_cmd(
    pattern="^\-_-$",
    command=("-_-", menu_category),
    info={
        "header": "Animation command",
        "usage": "-_-",
    },
)
async def lol(lel):
    "Animation command"
    lel = await eor(lel, "-__-")
    okay = "-__-"
    for _ in range(15):
        await asyncio.sleep(0.5)
        okay = okay[:-1] + "_-"
        await lel.edit(okay)


@legend.legend_cmd(
    pattern="^\;_;$",
    command=(";_;", menu_category),
    info={
        "header": "Animation command",
        "usage": ";_;",
    },
)
async def fun(e):
    "Animation command"
    e = await eor(e, ";__;")
    t = ";__;"
    for _ in range(15):
        await asyncio.sleep(0.5)
        t = t[:-1] + "_;"
        await e.edit(t)


@legend.legend_cmd(
    pattern="oof$",
    command=("oof", menu_category),
    info={
        "header": "Animation command",
        "usage": "{tr}oof",
    },
)
async def Oof(e):
    "Animation command."
    t = "Oof"
    legendevent = await eor(e, t)
    for _ in range(15):
        await asyncio.sleep(0.5)
        t = t[:-1] + "of"
        await legendevent.edit(t)


@legend.legend_cmd(
    pattern="type ([\s\S]*)",
    command=("type", menu_category),
    info={
        "header": "Type writter animation.",
        "usage": "{tr}type text",
    },
)
async def typewriter(typew):
    "Type writter animation."
    message = typew.pattern_match.group(1)
    sleep_time = 0.2
    typing_symbol = "|"
    old_text = ""
    typew = await eor(typew, typing_symbol)
    await asyncio.sleep(sleep_time)
    for character in message:
        old_text = old_text + "" + character
        typing_text = old_text + "" + typing_symbol
        await typew.edit(typing_text)
        await asyncio.sleep(sleep_time)
        await typew.edit(old_text)
        await asyncio.sleep(sleep_time)


@legend.legend_cmd(
    pattern="repeat (\d*) ([\s\S]*)",
    command=("repeat", menu_category),
    info={
        "header": "repeats the given text with given no of times.",
        "usage": "{tr}repeat <count> <text>",
        "examples": "{tr}repeat 10 LegendDeepak",
    },
)
async def _(event):
    "To repeat the given text."
    lol = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = lol[1]
    count = int(lol[0])
    repsmessage = (f"{message} ") * count
    await eor(event, repsmessage)


@legend.legend_cmd(
    pattern="meme",
    command=("meme", menu_category),
    info={
        "header": "Animation command",
        "usage": [
            "{tr}meme <emoji/text>",
            "{tr}meme",
        ],
    },
)
async def meme(event):
    "Animation command."
    memeVar = event.text
    sleepValue = 0.5
    memeVar = memeVar[6:]
    if not memeVar:
        memeVar = "✈️"
    event = await eor(event, "-------------" + memeVar)
    await asyncio.sleep(sleepValue)
    await event.edit("------------" + memeVar + "-")
    await asyncio.sleep(sleepValue)
    await event.edit("-----------" + memeVar + "--")
    await asyncio.sleep(sleepValue)
    await event.edit("----------" + memeVar + "---")
    await asyncio.sleep(sleepValue)
    await event.edit("---------" + memeVar + "----")
    await asyncio.sleep(sleepValue)
    await event.edit("--------" + memeVar + "-----")
    await asyncio.sleep(sleepValue)
    await event.edit("-------" + memeVar + "------")
    await asyncio.sleep(sleepValue)
    await event.edit("------" + memeVar + "-------")
    await asyncio.sleep(sleepValue)
    await event.edit("-----" + memeVar + "--------")
    await asyncio.sleep(sleepValue)
    await event.edit("----" + memeVar + "---------")
    await asyncio.sleep(sleepValue)
    await event.edit("---" + memeVar + "----------")
    await asyncio.sleep(sleepValue)
    await event.edit("--" + memeVar + "-----------")
    await asyncio.sleep(sleepValue)
    await event.edit("-" + memeVar + "------------")
    await asyncio.sleep(sleepValue)
    await event.edit(memeVar + "-------------")
    await asyncio.sleep(sleepValue)
    await event.edit("-------------" + memeVar)
    await asyncio.sleep(sleepValue)
    await event.edit("------------" + memeVar + "-")
    await asyncio.sleep(sleepValue)
    await event.edit("-----------" + memeVar + "--")
    await asyncio.sleep(sleepValue)
    await event.edit("----------" + memeVar + "---")
    await asyncio.sleep(sleepValue)
    await event.edit("---------" + memeVar + "----")
    await asyncio.sleep(sleepValue)
    await event.edit("--------" + memeVar + "-----")
    await asyncio.sleep(sleepValue)
    await event.edit("-------" + memeVar + "------")
    await asyncio.sleep(sleepValue)
    await event.edit("------" + memeVar + "-------")
    await asyncio.sleep(sleepValue)
    await event.edit("-----" + memeVar + "--------")
    await asyncio.sleep(sleepValue)
    await event.edit("----" + memeVar + "---------")
    await asyncio.sleep(sleepValue)
    await event.edit("---" + memeVar + "----------")
    await asyncio.sleep(sleepValue)
    await event.edit("--" + memeVar + "-----------")
    await asyncio.sleep(sleepValue)
    await event.edit("-" + memeVar + "------------")
    await asyncio.sleep(sleepValue)
    await event.edit(memeVar + "-------------")
    await asyncio.sleep(sleepValue)
    await event.edit(memeVar)


@legend.legend_cmd(
    pattern="give",
    command=("give", menu_category),
    info={
        "header": "Animation command",
        "usage": [
            "{tr}give <emoji/text>",
            "{tr}give",
        ],
    },
)
async def give(event):
    "Animation command."
    giveVar = event.text
    sleepValue = 0.5
    lp = giveVar[6:]
    if not lp:
        lp = " 🍭"
    event = await eor(event, lp + "        ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + "       ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + "      ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + "     ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + "    ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + "   ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + "  ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + " ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + lp)
    await asyncio.sleep(sleepValue)
    await event.edit(lp + "        ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + "       ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + "      ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + "     ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + "    ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + "   ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + "  ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + " ")
    await asyncio.sleep(sleepValue)
    await event.edit(lp + lp + lp + lp + lp + lp + lp + lp + lp)


@legend.legend_cmd(
    pattern="sadmin$",
    command=("sadmin", menu_category),
    info={
        "header": "Shouts Admin Animation command",
        "usage": "{tr}sadmin",
    },
)
async def _(event):
    "Shouts Admin Animation command."
    animation_ttl = range(13)
    event = await eor(event, "sadmin")
    animation_chars = [
        "@aaaaaaaaaaaaadddddddddddddmmmmmmmmmmmmmiiiiiiiiiiiiinnnnnnnnnnnnn",
        "@aaaaaaaaaaaaddddddddddddmmmmmmmmmmmmiiiiiiiiiiiinnnnnnnnnnnn",
        "@aaaaaaaaaaadddddddddddmmmmmmmmmmmiiiiiiiiiiinnnnnnnnnnn",
        "@aaaaaaaaaaddddddddddmmmmmmmmmmiiiiiiiiiinnnnnnnnnn",
        "@aaaaaaaaadddddddddmmmmmmmmmiiiiiiiiinnnnnnnnn",
        "@aaaaaaaaddddddddmmmmmmmmiiiiiiiinnnnnnnn",
        "@aaaaaaadddddddmmmmmmmiiiiiiinnnnnnn",
        "@aaaaaaddddddmmmmmmiiiiiinnnnnn",
        "@aaaaadddddmmmmmiiiiinnnnn",
        "@aaaaddddmmmmiiiinnnn",
        "@aaadddmmmiiinnn",
        "@aaddmmiinn",
        "@admin",
    ]
    for i in animation_ttl:
        await asyncio.sleep(1)
        await event.edit(animation_chars[i % 13])
