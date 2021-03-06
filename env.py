import os
from dotenv import load_dotenv

load_dotenv(override=True)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_GUILD_ID = int(os.getenv("DISCORD_GUILD_ID", 0))

DATABASE = os.getenv("DATABASE")  # MongoDB database URI
DATABASE_COLLECTION = os.getenv("DATABASE_COLLECTION", "discord-bot")  # the exact collection to send updates to
BOT = os.getenv("BOT")
