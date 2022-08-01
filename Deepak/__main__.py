import sys

import Deepak
from Deepak import BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import legend
from .start import killer
from .utils import (
    add_bot_to_logger_group,
    hekp,
    install_extrarepo,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("⚡UserBot🥇")

print(Deepak.__copyright__)
print("Licensed under the terms of the " + Deepak.__license__)

cmdhr = Config.HANDLER


async def extrarepo():
    if Config.EXTRA_REPO:
        await install_extrarepo(
            Config.EXTRA_REPO, Config.EXTRA_REPOBRANCH, "xtraplugins"
        )


try:
    LOGS.info("Starting Userbot")
    legend.loop.run_until_complete(setup_bot())
    LOGS.info("TG Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


async def startup_process():
    try:
        await verifyLoggerGroup()
        await load_plugins("plugins")
        await load_plugins("assistant")
        await killer()
        print("----------------")
        print("Starting Bot Mode!")
        print("⚜ UserBot Has Been Deployed Successfully ⚜")
        print("OWNER - @OFFICIALHACKERERA")
        print("----------------")
        await verifyLoggerGroup()
        await add_bot_to_logger_group(BOTLOG_CHATID)
        if PM_LOGGER_GROUP_ID != -100:
            await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
        await startupmessage()
        await extrarepo()
        await hekp()
    except Exception as e:
        LOGS.error(f"{str(e)}")
        sys.exit()


legend.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    legend.disconnect()
else:
    try:
        legend.run_until_disconnected()
    except ConnectionError:
        pass
