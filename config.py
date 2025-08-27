import json
from os import getenv, path
from dotenv import load_dotenv
from Backend import LOGGER


load_dotenv(path.join(path.dirname(path.dirname(__file__)), "config.env"))
class Telegram:
    API_ID = int(getenv("API_ID", "27696177"))
    API_HASH = getenv("API_HASH", "0c44906a4feff3b947db76dfa7c57d88")
    BOT_TOKEN = getenv("BOT_TOKEN", "7504435560:AAFED_rcs6P_9aeJm0NbO24Xgiw")
    PORT = int(getenv("PORT", "8000"))
    BASE_URL = getenv("BASE_URL", "httpcnd.onrender.com").rstrip('/')
    AUTH_CHANNEL = [channel.strip() for channel in (getenv("AUTH_CHANNEL") or "-1002193361335").split(",") if channel.strip()]
    DATABASE = getenv("DATABASE", "mongodb+srv://tmrbotz:gRkWfPA0ToDRNe1d@cluster0.rxoovko.me=Cluster0").split(", ")
    TMDB_API = getenv("TMDB_API", "")
    IMDB_API = getenv("IMDB_API", "https://imd.workers.dev")
    UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TmrBotz/")
    UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
    MULTI_CLIENT = getenv("MULTI_CLIENT", "True").lower() == "true"
    USE_CAPTION = getenv("USE_CAPTION", "False").lower() == "true"
    USE_TMDB = getenv("USE_TMDB", "False").lower() == "true"
    OWNER_ID = int(getenv("OWNER_ID", "6987799874"))
    USE_DEFAULT_ID = getenv("USE_DEFAULT_ID", None)
