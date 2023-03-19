from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("23864794"))
API_HASH = getenv("0176a32f396e45a0a33644f678507d76")
BOT_TOKEN = getenv("5921061038:AAHjBKykr_DEij3EvpLAyaZJsXidt1syhyk")

MONGO_DB_URI = getenv("mongodb+srv://TELEGRAM:TELEGRAM@cluster0.tznsnwb.mongodb.net/?retryWrites=true&w=majority")

INDEX_ID = int(getenv("-1001963941283"))
UPLOADS_ID = int(getenv("-1001909816933"))

STATUS_ID = int(getenv("STATUS_ID"))
SCHEDULE_ID = int(getenv("SCHEDULE_ID"))

CHANNEL_TITLE = getenv("CHANNEL_TITLE")
INDEX_USERNAME = getenv("INDEX_USERNAME")
UPLOADS_USERNAME = getenv("UPLOADS_USERNAME")
