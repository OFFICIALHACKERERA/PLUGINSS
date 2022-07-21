import asyncio
import math
import os

import heroku3
import requests
import urllib3

from userbot import legend

from ..Config import Config
from ..core.managers import eod, eor

menu_category = "tools"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# =================

Heroku = heroku3.from_key(Config.API_KEY)
heroku_api = "https://api.heroku.com"
APP_NAME = Config.APP_NAME
API_KEY = Config.API_KEY


@legend.legend_cmd(
    pattern="(set|get|del) var ([\s\S]*)",
    command=("var", menu_category),
    info={
        "header": "To manage heroku vars.",
        "flags": {
            "set": "To set new var in heroku or modify the old var",
            "get": "To show the already existing var value.",
            "del": "To delete the existing value",
        },
        "usage": [
            "{tr}set var <var name> <var value>",
            "{tr}get var <var name>",
            "{tr}del var <var name>",
        ],
        "examples": [
            "{tr}get var ALIVE_NAME",
        ],
    },
)
async def variable(var):  # sourcery no-metrics
    """
    Manage most of ConfigVars setting, set new var, get current var, or delete var...
    """
    if (Config.API_KEY is None) or (Config.APP_NAME is None):
        return await eod(
            var,
            "Set the required vars in heroku to function this normally `API_KEY` and `APP_NAME`.",
        )
    app = Heroku.app(Config.APP_NAME)
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        legend = await eor(var, "`Getting information...`")
        await asyncio.sleep(1.0)
        try:
            variable = var.pattern_match.group(2).split()[0]
            legend = "**ConfigVars**:" f"\n\n {variable} = `{heroku_var[variable]}`\n"
            if "LEGEND_STRING" in variable:
                await eor(
                    var, "Legend String is a Sensetive Data.\nProtected By LegendBot"
                )
                return
            elif variable in heroku_var:
                await eor(var, legend)
            else:
                return await var.edit(
                    "**ConfigVars**:" f"\n\n`Error:\n-> {variable} don't exists`"
                )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                await eor(
                    var,
                    "`[HEROKU]` ConfigVars:\n\n"
                    "================================"
                    f"\n```{result}```\n"
                    "================================",
                )
            os.remove("configs.json")
    elif exe == "set":
        variable = "".join(var.text.split(maxsplit=2)[2:])
        legend = await eor(var, "`Setting information...`")
        if not variable:
            return await legend.edit("`.set var <ConfigVars-name> <value>`")
        value = "".join(variable.split(maxsplit=1)[1:])
        variable = "".join(variable.split(maxsplit=1)[0])
        if not value:
            return await legend.edit("`.set var <ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if "LEGEND_STRING" in variable:
            await legend.edit("Successfully Changed")
            return
        if variable in heroku_var:
            await legend.edit(
                f"`{variable}` **successfully changed to  ->  **`{value}`"
            )
        else:
            await legend.edit(
                f"`{variable}`**  successfully added with value`  ->  **{value}`"
            )
        heroku_var[variable] = value
    elif exe == "del":
        legend = await eor(var, "`Getting information to deleting variable...`")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await legend.edit("`Please specify ConfigVars you want to delete`")
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
            return await legend.edit(f"`{variable}`**  does not exist**")

        await legend.edit(f"`{variable}`  **successfully deleted**")
        del heroku_var[variable]


@legend.legend_cmd(
    pattern="usage$",
    command=("usage", menu_category),
    info={
        "header": "To Check dyno usage of userbot and also to know how much left.",
        "usage": "{tr}usage",
    },
)
async def dyno_usage(dyno):
    """
    Get your account Dyno Usage
    """
    if (Config.APP_NAME is None) or (Config.API_KEY is None):
        return await eod(
            dyno,
            "Set the required vars in heroku to function this normally `API_KEY` and `APP_NAME`.",
        )
    dyno = await eor(dyno, "`Processing...`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Config.API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit(
            "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    # - Used -
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    # - Current -
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    return await dyno.edit(
        "**Dyno Usage**:\n\n"
        f" 🗒 `Dyno usage for`  **{Config.APP_NAME}**:\n"
        f"     •  `{AppHours}`**h**  `{AppMinutes}`**m**  "
        f"**|**  [`{AppPercentage}`**%**]"
        "\n\n"
        " -> `Dyno hours quota remaining this month`:\n"
        f"     •  `{hours}`**h**  `{minutes}`**m**  "
        f"**|**  [`{percentage}`**%**]"
    )


@legend.legend_cmd(
    pattern="(herokulogs|logs)$",
    command=("logs", menu_category),
    info={
        "header": "To get recent 100 lines logs from heroku.",
        "usage": ["{tr}herokulogs", "{tr}logs"],
    },
)
async def _(dyno):
    "To get recent 100 lines logs from heroku"
    if (Config.APP_NAME is None) or (Config.API_KEY is None):
        return await eod(
            dyno,
            "Set the required vars in heroku to function this normally `API_KEY` and `APP_NAME`.",
        )
    try:
        Heroku = heroku3.from_key(API_KEY)
        app = Heroku.app(APP_NAME)
    except BaseException:
        return await dyno.reply(
            " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
        )
    data = app.get_log()
    await eor(
        dyno, data, deflink=True, linktext="**Recent 100 lines of heroku logs: **"
    )


def prettyjson(obj, indent=2, maxlinelength=80):
    """Renders JSON content with indentation and line splits/concatenations to fit maxlinelength.
    Only dicts, lists and basic types are supported"""
    items, _ = getsubitems(
        obj,
        itemkey="",
        islast=True,
        maxlinelength=maxlinelength - indent,
        indent=indent,
    )
    return indentitems(items, indent, level=0)
