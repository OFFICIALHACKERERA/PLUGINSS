from telethon.tl import functions

from ..core.logger import logging
from ..core.managers import eor

LOGS = logging.getLogger("LegendUserBot")

pawn = [
    "nsfw",
    "nsfw_gifs",
    "nsfw_gif",
    "60fpsporn",
    "porn",
    "porn_gifs",
    "porninfifteenseconds",
    "CuteModeSlutMode",
    "NSFW_HTML5",
    "the_best_nsfw_gifs",
    "verticalgifs",
    "besthqporngifs",
    "boobs",
    "pussy",
    "jigglefuck",
    "broslikeus",
    "gangbang",
    "passionx",
    "titfuck",
    "HappyEmbarrassedGirls",
    "suicidegirls",
    "porninaminute",
    "SexInFrontOfOthers",
    "tiktoknsfw",
    "tiktokporn",
    "TikThots",
    "NSFWFunny",
    "GWNerdy",
    "WatchItForThePlot",
    "HoldTheMoan",
    "OnOff",
    "TittyDrop",
    "extramile",
    "Exxxtras",
    "adorableporn",
]

hemtai = [
    "feet",
    "yuri",
    "trap",
    "futanari",
    "hololewd",
    "lewdkemo",
    "solog",
    "feetg",
    "cum",
    "erokemo",
    "les",
    "wallpaper",
    "lewdk",
    "ngif",
    "tickle",
    "lewd",
    "feed",
    "gecg",
    "eroyuri",
    "eron",
    "cum_jpg",
    "bj",
    "nsfw_neko_gif",
    "solo",
    "kemonomimi",
    "nsfw_avatar",
    "gasm",
    "poke",
    "anal",
    "slap",
    "hentai",
    "avatar",
    "erofeet",
    "holo",
    "keta",
    "blowjob",
    "pussy",
    "tits",
    "holoero",
    "lizard",
    "pussy_jpg",
    "pwankg",
    "classic",
    "kuni",
    "waifu",
    "pat",
    "8ball",
    "kiss",
    "femdom",
    "neko",
    "spank",
    "cuddle",
    "erok",
    "fox_girl",
    "boobs",
    "random_hentai_gif",
    "smallboobs",
    "hug",
    "ero",
    "smug",
    "goose",
    "baka",
    "woof",
]


async def importent(event):
    legend = ["-1001368578667", "-1001750559161"]
    if str(event.chat_id) in legend:
        await eor(event, "**Yes I'm GAY**")
        await event.client.kick_participant(event.chat_id, "me")
        return True
    return False


def nsfw(catagory):
    catagory.sort(key=str.casefold)
    horny = "**Catagory :** "
    for i in catagory:
        horny += f" `{i.lower()}` ||"
    return horny


async def unsave_gif(event, hgif):
    try:
        await event.client(
            functions.messages.SaveGifRequest(
                id=get_input_document(hgif),
                unsave=True,
            )
        )
    except Exception as e:
        LOGS.info(e)


API = "https://weaverbottest.herokuapp.com/gimme"
