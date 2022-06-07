import os

class Config:
    aid = int(os.environ.get("API_ID", None))
    ahash = os.environ.get("API_HASH", None)
    bot_token = os.environ.get("BOT_TOKEN", None)
   
   
