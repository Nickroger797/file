import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    APP_ID = int(os.environ.get("APP_ID", "23331203"))
    API_HASH = os.environ.get("API_HASH", "05be4bb2e1e6806a2ffd23402079e23a")
    USER_NAME = os.environ.get("USER_NAME", "Codexownerr")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    BANNED_USERS = set(map(int, os.environ.get("BANNED_USERS", "").split())) if os.environ.get("BANNED_USERS") else set()
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    QUO_IO_API_KEY = ""
    MAX_MESSAGE_LENGTH = 4096
    BOT_PWD = os.getenv("BOT_PWD", "Aditya")
    PORT = int(os.environ.get("PORT", 8080))
    LOGGED_USER = []
    
    # Use environment variable instead of hardcoded URI
    MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://tryoutbothai:botno2@cluster1.d0w5i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1")
    
