import os

from telethon import TelegramClient
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import logging
from pytgcalls import PyTgCalls
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicsample_sample_config(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


from sample_sample_config import sample_sample_config
BOT_USERNAME = sample_sample_config.BOT_USERNAME

bot = TelegramClient('Deepak', api_id=sample_sample_config.API_ID, api_hash=sample_sample_config.API_HASH)
Deepak = bot.start(bot_token=sample_sample_config.BOT_TOKEN)
client = TelegramClient(StringSession(sample_sample_config.STRING_SESSION), sample_sample_config.API_ID, sample_sample_config.API_HASH)
call_py = PyTgCalls(client)
client.start()
call_py.start()
