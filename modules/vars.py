#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29426008"))
API_HASH = environ.get("API_HASH", "fedd630ba4bd77044ee4e5a00e5300e6")
BOT_TOKEN = environ.get("BOT_TOKEN", "8291699148:AAEAI9nBzrJ39PNe0smKnxngO89bDD3Tdxw")

OWNER = int(environ.get("OWNER", "5504044604"))
CREDIT = environ.get("CREDIT", "𝐒𝐂𝐇𝐑𝐎𝐃𝐈𝐍𝐆𝐄𝐑")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5504044604').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5504044604').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))


