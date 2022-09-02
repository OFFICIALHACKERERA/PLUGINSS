import sys

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from ..Config import Config
from .client import LegendClient

#Music Bot import
import os
from telethon import TelegramClient
from pytgcalls import PyTgCalls

__version__ = "1.10.6"

loop = None

if Config.DEEPAK_STRING:
    session = StringSession(str(Config.DEEPAK_STRING))
else:
    session = "USERBOT✅"

try:
    legend = LegendClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"DEEPAK_STRING - {e}")
    sys.exit()

legend.tgbot = tgbot = LegendClient(
    session="LegendTgbot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.BOT_TOKEN)

BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
API_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
BOT_USERNAME = BOT_USERNAME

bot = TelegramClient('Deepak', api_id=API_ID, api_hash=API_HASH)
Deepak = bot.start(bot_token=BOT_TOKEN)
client = TelegramClient(StringSession(Config.DEEPAK_STRING), API_ID, API_HASH)
call_py = PyTgCalls(client)
client.start()
call_py.start()
