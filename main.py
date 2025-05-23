import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Récupérer le token depuis les variables d’environnement
TOKEN = os.getenv("TOKEN")

# Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenue ! Le bot fonctionne via Webhook.")

# Commande test
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pong !")

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ping", ping))

    # Webhook config
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        webhook_url="https://pocket-option-bot-5b4q.onrender.com"
    )

if __name__ == "__main__":
    main()
