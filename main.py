from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
from config import TELEGRAM_TOKEN, WEBHOOK_URL
import logging
import asyncio

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Définir le menu de démarrage
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Basculer vers le compte réel", callback_data="real")],
        [InlineKeyboardButton("Basculer vers le compte démo", callback_data="demo")],
        [InlineKeyboardButton("Définir montant min trade", callback_data="set_min")],
        [InlineKeyboardButton("Afficher journal de performance", callback_data="log")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Bienvenue ! Choisissez une option :", reply_markup=reply_markup)

# Réagir aux clics de boutons
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "real":
        await query.edit_message_text("Mode réel activé.")
    elif data == "demo":
        await query.edit_message_text("Mode démo activé.")
    elif data == "set_min":
        await query.edit_message_text("Envoyez le montant minimum souhaité.")
    elif data == "log":
        await query.edit_message_text("Voici le journal de performances... (à compléter)")

# Créer et lancer le bot avec Webhook
async def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    await app.bot.set_webhook(url=WEBHOOK_URL)
    logger.info("Bot lancé avec webhook...")
    await app.start()
    await app.updater.start_polling()  # Optionnel si tu veux écouter aussi en local
    await app.updater.idle()

if __name__ == "__main__":
    asyncio.run(main())
