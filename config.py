# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "23673651"))
API_HASH = getenv("API_HASH", "f032bfa12ee46e1283f6fb23cfca5c6b")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6677821706").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://apomgran:oJeWS0gstI3sxNRM@cluster0.j1kpnv6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002685378156")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002652379070"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "50000"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "50000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
