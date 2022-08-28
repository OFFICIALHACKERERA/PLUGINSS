import os

from telethon import TelegramClient
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import logging
from pytgcalls import PyTgCalls
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


from Config import Config
BOT_USERNAME = Config.BOT_USERNAME

bot = TelegramClient('Deepak', api_id=Config.API_ID, api_hash=Config.API_HASH)
Deepak = bot.start(bot_token=sample_config.BOT_TOKEN)
client = TelegramClient(StringSession(Config.DEEPAK_STRING), Config.API_ID, Config.API_HASH)
call_py = PyTgCalls(client)
client.start()
call_py.start()
