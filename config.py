from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("23864794"))
API_HASH = getenv("0176a32f396e45a0a33644f678507d76")
BOT_TOKEN = getenv("5921061038:AAHjBKykr_DEij3EvpLAyaZJsXidt1syhyk")

MONGO_DB_URI = getenv("mongodb+srv://TELEGRAM:TELEGRAM@cluster0.tznsnwb.mongodb.net/?retryWrites=true&w=majority")

INDEX_ID = int(getenv("-1001963941283"))
UPLOADS_ID = int(getenv("-1001909816933"))

STATUS_ID = int(getenv("-1001909816933"))
SCHEDULE_ID = int(getenv("-1001909816933"))

CHANNEL_TITLE = getenv("@Anime_pirates")
INDEX_USERNAME = getenv("@Auto_animes_channelindex")
UPLOADS_USERNAME = getenv("@Auto_animes_channel")
