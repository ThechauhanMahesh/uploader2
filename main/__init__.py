#ChauhanMahesh/Vasusen/DroneBots/COL

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = 2992000
API_HASH = "235b12e862d71234ea222082052822fd"
BOT_TOKEN = "5992685017:AAE1qIhVFn5VsZh8fwepVNDKixCId69zz-k"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
