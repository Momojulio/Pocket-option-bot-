import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
from config import BOT_TOKEN, CHAT_ID, WEBHOOK_URL, PORT

import asyncio

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Commande de test
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot actif et prêt !")

# Fonction principale
async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    await app.initialize()
    await app.start()
    await app.bot.set_webhook(url=WEBHOOK_URL)
    await app.updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=WEBHOOK_URL,
    )
    await app.updater.idle()

if __name__ == "__main__":
    asyncio.run(main())
