import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Assure-toi que cette variable est bien définie dans Render
PORT = int(os.getenv("PORT", 8000))  # Port par défaut si non défini
