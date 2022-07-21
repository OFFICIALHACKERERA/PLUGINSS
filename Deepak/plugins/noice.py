import asyncio
import random

from . import eor, legend

menu_category = "fun"


eor = eor


KANNADIGAOSTR = [
    "`Hi !`",
    "`‘Ello, gov'nor!`",
    "`What’s crackin’?`",
    "`‘Sup, homeslice?`",
    "`Howdy, howdy ,howdy!`",
    "`hello, who's there, I'm talking.`",
    "`You know who this is.`",
    "`Yo!`",
    "`Whaddup.`",
    "`Greetings and salutations!`",
    "`hello, sunshine!`",
    "`Hey, howdy, hi!`",
    "`What’s kickin’, little chicken?`",
    "`Peek-a-boo!`",
    "`Howdy-doody!`",
    "`Hey there, freshman!`",
    "`I come in peace!`",
    "`Ahoy, matey!`",
    "`Hiya!`",
    "`Oh retarded gey! Well hello`",
]

SHGS = [
    "┐(´д｀)┌",
    "┐(´～｀)┌",
    "┐(´ー｀)┌",
    "┐(￣ヘ￣)┌",
    "╮(╯∀╰)╭",
    "╮(╯_╰)╭",
    "┐(´д`)┌",
    "┐(´∀｀)┌",
    "ʅ(́◡◝)ʃ",
    "ლ(ﾟдﾟლ)",
    "┐(ﾟ～ﾟ)┌",
    "┐('д')┌",
    "ლ｜＾Д＾ლ｜",
    "ლ（╹ε╹ლ）",
    "ლ(ಠ益ಠ)ლ",
    "┐(‘～`;)┌",
    "ヘ(´－｀;)ヘ",
    "┐( -“-)┌",
    "乁༼☯‿☯✿༽ㄏ",
    "ʅ（´◔౪◔）ʃ",
    "ლ(•ω •ლ)",
    "ヽ(゜～゜o)ノ",
    "ヽ(~～~ )ノ",
    "┐(~ー~;)┌",
    "┐(-。ー;)┌",
    "¯\_(ツ)_/¯",
    "¯\_(⊙_ʖ⊙)_/¯",
    "乁ʕ •̀ ۝ •́ ʔㄏ",
    "¯\_༼ ಥ ‿ ಥ ༽_/¯",
    "乁( ⁰͡  Ĺ̯ ⁰͡ ) ㄏ",
]

CRI = [
    "أ‿أ",
    "╥﹏╥",
    "(;﹏;)",
    "(ToT)",
    "(┳Д┳)",
    "(ಥ﹏ಥ)",
    "（；へ：）",
    "(T＿T)",
    "（πーπ）",
    "(Ｔ▽Ｔ)",
    "(⋟﹏⋞)",
    "（ｉДｉ）",
    "(´Д⊂ヽ",
    "(;Д;)",
    "（>﹏<）",
    "(TдT)",
    "(つ﹏⊂)",
    "༼☯﹏☯༽",
    "(ノ﹏ヽ)",
    "(ノAヽ)",
    "(╥_╥)",
    "(T⌓T)",
    "(༎ຶ⌑༎ຶ)",
    "(☍﹏⁰)｡",
    "(ಥ_ʖಥ)",
    "(つд⊂)",
    "(≖͞_≖̥)",
    "(இ﹏இ`｡)",
    "༼ಢ_ಢ༽",
    "༼ ༎ຶ ෴ ༎ຶ༽",
]
# ===========================================


@legend.legend_cmd(
    pattern="crie$",
    command=("crie", menu_category),
    info={
        "header": "Try Yourself",
        "usage": "{tr}crie",
    },
)
async def cri(e):
    """y u du dis, i cry everytime !!"""
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await eor(e, random.choice(CRI))


@legend.legend_cmd(
    pattern="hey$",
    command=("hey", menu_category),
    info={
        "header": "Try Yourself",
        "usage": "{tr}hey",
    },
)
async def hoi(hello):
    """Greet everyone!"""
    if not hello.text[0].isalpha() and hello.text[0] not in ("/", "#", "@", "!"):
        await eor(hello, random.choice(KANNADIGAOSTR))


@legend.legend_cmd(
    pattern="shrug$",
    command=("shrug", menu_category),
    info={
        "header": "Try Yourself",
        "usage": "{tr}shrug",
    },
)
async def shrugger(shg):
    r"""¯\_(ツ)_/¯"""
    if not shg.text[0].isalpha() and shg.text[0] not in ("/", "#", "@", "!"):
        await eor(shg, random.choice(SHGS))


@legend.legend_cmd(
    pattern="nopee$",
    command=("nopee", menu_category),
    info={
        "header": "Try Yourself",
        "usage": "{tr}nopee",
    },
)
async def _(event):
    animation_interval = 0.1
    animation_ttl = range(0, 7)
    await eor(event, "nope")
    animation_chars = [
        "No",
        "Problem",
        "Boss",
        "Yeah ! No problem",
        "No Problem Boss.lol",
        "No Problem Boss😇.Lol",
        "No Problem Man😇.Lol",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 7])


@legend.legend_cmd(
    pattern="okk$",
    command=("okk", menu_category),
    info={
        "header": "Try Yourself",
        "usage": "{tr}okk",
    },
)
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 18)
    # input_str = event.pattern_match.group(1)
    # if input_str == "ok":
    await event.edit("ok")
    animation_chars = [
        "οκ",
        "ѕιя",
        "мιѕs",
        "οκ bro",
        "οκ ϐяο",
        "οκ gƒ",
        "οκ bƒ",
        "οκ ∂єαя",
        "gο αи∂ ѕαγ οκ",
        "οκ ℓοℓ",
        "οκ ѕκ",
        "οκ ∂и",
        "οκ",
        "sis",
        "Yeah",
        "O",
        "K",
        "οκ ѕιя/мιѕѕ! 😇",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
