pimport logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import BOT_TOKEN, CHAT_ID, WEBHOOK_URL

# Logging pour surveillance
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot Pocket Option prêt à l’action !")

# Commande /status
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Tout fonctionne normalement.")

# Fonction principale
async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Ajout des commandes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    # Configuration du webhook
    await app.bot.set_webhook(url=WEBHOOK_URL)

    # Lancement via webhook
    await app.run_webhook(
        listen="0.0.0.0",
        port=8000,
        webhook_url=WEBHOOK_URL
    )

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
