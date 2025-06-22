#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

# ======== BOT CONFIGURATION ========
# Bot token from @BotFather
TG_BOT_TOKEN = "7560608344:AAFGpsfweysBNW1kDMpA2SOGmW64Gqs3EkM"

# Telegram API credentials
APP_ID = 29774383
API_HASH = "e452445f51c0892016e5f517c5f6e2d6"

# Channel and ownership details
CHANNEL_ID =-1002365072709
OWNER_ID =6713921355
FORCE_SUB_CHANNEL =-1002386120316  # Backup channel

# Database configuration
DB_URI = "mongodb://neetug2025nta1:1U8ZNycmBrPdKQ0m@atlas-sql-6856b206ce5d45775696769d-eiue7k.a.query.mongodb.net/sample_mflix?ssl=true&authSource=admin"
DB_NAME = "sample_mflix"  # Matches your MongoDB database

# ======== OPTIONAL SETTINGS ========
# Bot workers (4 is optimal)
TG_BOT_WORKERS = 4

# Auto-delete configuration (0 to disable)
AUTO_DELETE_TIME = 0  # Disabled by default
AUTO_DELETE_MSG = "This file will be automatically deleted in {time} seconds."
AUTO_DEL_SUCCESS_MSG = "File deleted successfully ✅"

# Force subscription message
FORCE_MSG = "Hello {first}\n\n<b>Join our backup channel to use this bot</b>"

# Custom caption (None to disable)
CUSTOM_CAPTION = None

# Security settings
PROTECT_CONTENT = True  # Prevent file forwarding

# Admin management
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "6035243720").split())]
except ValueError:
    raise Exception("Admins list contains invalid IDs")

# Startup message
START_PIC = ""  # Add image URL if needed
START_MSG = "Hello {first}\n\nI securely store files in channels with special access links."

# ======== ADVANCED SETTINGS ========
PORT = "8080"  # Web server port
DISABLE_CHANNEL_BUTTON = False  # Show share button
JOIN_REQUEST_ENABLE = None  # Join requests handling
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ Direct messages not supported!"

# Append default admin (CodeXBotz maintainer)
ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

# ======== LOGGING SETUP ========
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50_000_000,  # 50MB
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
