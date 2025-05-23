import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
USE_WEBHOOK = os.getenv("USE_WEBHOOK", "True").lower() == "true"
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
TRADE_AMOUNT = float(os.getenv("TRADE_AMOUNT", 1))
USE_REAL_ACCOUNT = os.getenv("USE_REAL_ACCOUNT", "False").lower() == "true"
PORT=10000
