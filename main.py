import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import BOT_TOKEN, CHAT_ID, WEBHOOK_URL

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Commande de base
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Bot bien lancé et fonctionnel !")

# Création de l'application Telegram
app = Application.builder().token(BOT_TOKEN).build()

# Ajout du handler
app.add_handler(CommandHandler("start", start))

# Lancement du bot avec webhook
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=BOT_TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{BOT_TOKEN}",
    )
