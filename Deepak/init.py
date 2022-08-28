import os

from telethon import TelegramClient
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import logging
from pytgcalls import PyTgCalls
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicsample_config(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


from sample_config import sample_config
BOT_USERNAME = sample_config.BOT_USERNAME

bot = TelegramClient('Deepak', api_id=sample_config.API_ID, api_hash=sample_config.API_HASH)
Deepak = bot.start(bot_token=sample_config.BOT_TOKEN)
client = TelegramClient(StringSession(sample_config.DEEPAK_STRING), sample_config.API_ID, sample_config.API_HASH)
call_py = PyTgCalls(client)
client.start()
call_py.start()