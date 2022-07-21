import random
import re

from . import legend

menu_category = "utils"


@legend.legend_cmd(
    pattern="scramble(?:\s|$)([\s\S]*)",
    command=("scramble", menu_category),
    info={
        "header": "To Scramble the Word.",
        "description": "Reply to any text to scramble it.",
        "usage": "{tr}scramble <reply to message>",
    },
)
async def scramble_message(e):
    reply_message = await e.get_reply_message()
    text = e.pattern_match.group(1) or reply_message.text
    words = re.split(r"\s", text)
    scrambled = map(scramble_word, words)
    text = " ".join(scrambled)
    await e.edit(text)


def scramble_word(word):
    if len(word) < 4:
        return word

    first_letter = word[0]
    last_letter = word[-1]
    middle_letters = list(word[1:-1])
    random.shuffle(middle_letters)

    return first_letter + "".join(middle_letters) + last_letter





#official Hacker 