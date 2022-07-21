import random

from .. import legend
from ..core.logger import logging

menu_category = "tools"

LOGS = logging.getLogger(__name__)


@legend.legend_cmd(
    pattern="swt(?:\s|$)([\s\S]*)",
    command=("swt", menu_category),
    info={
        "header": "Try It Your Self.",
        "description": "Random Flags",
        "flags": {
            "ex": "Try Yourself",
            "think": "Try Yourself",
            "wave": "Try Yourself",
            "wtf": "Try Yourself",
            "love": "Try Yourself",
            "confuse": "Try Yourself",
            "dead": "Try Yourself",
            "sad": "Try Yourself",
            "dog": "Try Yourself",
        },
        "usage": [
            "{tr}swt <flags>",
        ],
        "examples": [
            "{tr}swt ex",
        ],
    },
)
async def _(event):
    input_str = event.pattern_match.group(1)
    if input_str in "ex":
        emoticons = [
            "u is mard",
            "u is man",
            "u is aurat",
            "u is woman",
            "u is gey",
            "u is chakka",
        ]
    elif input_str in "think":
        emoticons = [
            "(҂⌣̀_⌣́)",
            "（；¬＿¬)",
            "(-｡-;",
            "┌[ O ʖ̯ O ]┐",
            "〳 ͡° Ĺ̯ ͡° 〵",
        ]
    elif input_str in "wave":
        emoticons = [
            "(ノ^∇^)",
            "(;-_-)/",
            "@(o・ェ・)@ノ",
            "ヾ(＾-＾)ノ",
            "ヾ(◍’౪◍)ﾉﾞ♡",
            "(ό‿ὸ)ﾉ",
            "(ヾ(´・ω・｀)",
        ]
    elif input_str in "wtf":
        emoticons = [
            "༎ຶ‿༎ຶ",
            "(‿ˠ‿)",
            "╰U╯☜(◉ɷ◉ )",
            "(;´༎ຶ益༎ຶ)♡",
            "╭∩╮(︶ε︶*)chu",
            "( ＾◡＾)っ (‿|‿)",
        ]
    elif input_str in "loves":
        emoticons = [
            "乂❤‿❤乂",
            "(｡♥‿♥｡)",
            "( ͡~ ͜ʖ ͡°)",
            "໒( ♥ ◡ ♥ )७",
            "༼♥ل͜♥༽",
        ]
    elif input_str in "confuse":
        emoticons = [
            "(・_・ヾ",
            "｢(ﾟﾍﾟ)",
            "﴾͡๏̯͡๏﴿",
            "(￣■￣;)!?",
            "▐ ˵ ͠° (oo) °͠ ˵ ▐",
            "(-_-)ゞ゛",
        ]
    elif input_str in "dead":
        emoticons = [
            "(✖╭╮✖)",
            "✖‿✖",
            "(+_+)",
            "(✖﹏✖)",
            "∑(✘Д✘๑)",
        ]
    elif input_str in "sad":
        emoticons = [
            "(＠´＿｀＠)",
            "⊙︿⊙",
            "(▰˘︹˘▰)",
            "●︿●",
            "(　´_ﾉ` )",
            "彡(-_-;)彡",
        ]
    elif input_str in "dog":
        emoticons = [
            "-ᄒᴥᄒ-",
            "◖⚆ᴥ⚆◗",
        ]
    else:
        emoticons = [
            "( ͡° ͜ʖ ͡°)",
            "¯\_(ツ)_/¯",
            "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
            "ʕ•ᴥ•ʔ",
            "(▀ Ĺ̯▀   )",
            "(ง ͠° ͟ل͜ ͡°)ง",
            "༼ つ ◕_◕ ༽つ",
            "ಠ_ಠ",
            "(☞ ͡° ͜ʖ ͡°)☞",
            "¯\_༼ ି ~ ି ༽_/¯",
            "c༼ ͡° ͜ʖ ͡° ༽⊃",
        ]
    index = random.randint(0, len(emoticons))
    output_str = emoticons[index]
    await event.edit(output_str)
