import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "29055333"))
  API_HASH = os.environ.get("API_HASH", "a6d154242eaef80a163bf5d0a7763882")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "7995863380:AAH8gQj2gbSyNvpIcsAVYnKmlthU5vhPnQA")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "CWT_Files_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002526508320"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "MoneyKamalo.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "0eefb93e1e3ce9470a7033115ceb1bad13a9d674")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6828129421"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://anjireddyb98:3qiaVJINXarqFNKp@cluster0.kohnpcd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002024495069")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002630777690"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", False))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [𝐕𝐚𝐦𝐬𝐢 🐦‍🔥](https://telegram.me/Vamsi_2008_vamsi)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Vamsi_2008_vamsi)
"""
  HOME_TEXT = """
**Hello, [{}](tg://user?id={})\n\nThis is a Permanent FileStore Bot Created by 𝐕𝐚𝐦𝐬𝐢 🐦‍🔥 and He Can Only Use me**.
"""
