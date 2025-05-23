from config import TELEGRAM_TOKEN, WEBHOOK_URL



import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = "https://pocket-option-bot-5b4q.onrender.com"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenue, le bot est actif !")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # Activation du Webhook
    async def run():
        await app.bot.set_webhook(url=WEBHOOK_URL)
        await app.run_webhook(
            listen="0.0.0.0",
            port=int(os.environ.get("PORT", 10000)),
            webhook_url=WEBHOOK_URL
        )

    import asyncio
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(run())
