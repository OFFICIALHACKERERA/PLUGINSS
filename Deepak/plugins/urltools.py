import requests
from validators.url import url

from Deepak import legend

from ..core.managers import eod, eor

menu_category = "utils"


@legend.legend_cmd(
    pattern="dns(?:\s|$)([\s\S]*)",
    command=("dns", menu_category),
    info={
        "header": "To get Domain Name System(dns) of the given link.",
        "usage": "{tr}dns <url/reply to url>",
        "examples": "{tr}dns google.com",
    },
)
async def _(event):
    "To get Domain Name System(dns) of the given link."
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply = await event.get_reply_message()
    if not input_str and reply:
        input_str = reply.text
    if not input_str:
        return await eod(
            event, "`Either reply to link or give link as input to get data`", 5
        )
    check = url(input_str)
    if not check:
        lolstr = f"http://{input_str}"
        check = url(lolstr)
    if not check:
        return await eod(event, "`the given link is not supported`", 5)
    sample_url = f"https://da.gd/dns/{input_str}"
    if response_api := requests.get(sample_url).text:
        await eor(event, f"DNS records of {input_str} are \n{response_api}")
    else:
        await eor(event, f"__I can't seem to find `{input_str}` on the internet__")


@legend.legend_cmd(
    pattern="short(?:\s|$)([\s\S]*)",
    command=("short", menu_category),
    info={
        "header": "To short the given url.",
        "usage": "{tr}short <url/reply to url>",
        "examples": "{tr}short https://github.com/ITS-LEGENDBOT/LEGENDBOT",
    },
)
async def _(event):
    "shortens the given link"
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply = await event.get_reply_message()
    if not input_str and reply:
        input_str = reply.text
    if not input_str:
        return await eod(
            event, "`Either reply to link or give link as input to get data`", 5
        )
    check = url(input_str)
    if not check:
        lolstr = f"http://{input_stt}"
        check = url(lolstr)
    if not check:
        return await eod(event, "`the given link is not supported`", 5)
    if not input_str.startswith("http"):
        input_str = f"http://{input_str}"
    sample_url = f"https://da.gd/s?url={input_str}"
    if response_api := requests.get(sample_url).text:
        await eor(
            event, f"Generated {response_api} for {input_str}.", link_preview=False
        )
    else:
        await eor(event, "`Something is wrong, please try again later.`")


@legend.legend_cmd(
    pattern="unshort(?:\s|$)([\s\S]*)",
    command=("unshort", menu_category),
    info={
        "header": "To unshort the given dagb shorten url.",
        "usage": "{tr}unshort <url/reply to url>",
        "examples": "{tr}unshort https://da.gd/rm6qri",
    },
)
async def _(event):
    "To unshort the given dagb shorten url."
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply = await event.get_reply_message()
    if not input_str and reply:
        input_str = reply.text
    if not input_str:
        return await eod(
            event, "`Either reply to link or give link as input to get data`", 5
        )
    check = url(input_str)
    if not check:
        lolstr = f"http://{input_str}"
        check = url(lolstr)
    if not check:
        return await eod(event, "`the given link is not supported`", 5)
    if not input_str.startswith("http"):
        input_str = f"http://{input_str}"
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith("3"):
        await eor(
            event,
            f"Input URL: {input_str}\nReDirected URL: {r.headers['Location']}",
            link_preview=False,
        )
    else:
        await eor(
            event,
            "Input URL {} returned status_code {}".format(input_str, r.status_code),
        )


# By Priyam Kalra
@legend.legend_cmd(
    pattern="hl(?:\s|$)([\s\S]*)",
    command=("hl", menu_category),
    info={
        "header": "To hide the url with white spaces using hyperlink.",
        "usage": "{tr}hl <url/reply to url>",
        "examples": "{tr}hl https://da.gd/rm6qri",
    },
)
async def _(event):
    "To hide the url with white spaces using hyperlink."
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply = await event.get_reply_message()
    if not input_str and reply:
        input_str = reply.text
    if not input_str:
        return await eod(
            event, "`Either reply to link or give link as input to get data`", 5
        )
    check = url(input_str)
    if not check:
        lolstr = f"http://{input_str}"
        check = url(lolstr)
    if not check:
        return await eod(event, "`the given link is not supported`", 5)
    await eor(event, f"[ㅤㅤㅤㅤㅤㅤㅤ]({input_str})")
