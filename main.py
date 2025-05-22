import os
import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pocket_option_bot import PocketOptionBot

nest_asyncio.apply()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID", "0"))  # par défaut 0

bot_logic = PocketOptionBot()

app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != CHAT_ID:
        await update.message.reply_text("Accès refusé.")
        return
    await update.message.reply_text("Bienvenue, le bot est actif.")

async def demo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(bot_logic.set_mode("demo"))

async def real(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(bot_logic.set_mode("real"))

async def set_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        try:
            amount = float(context.args[0])
            await update.message.reply_text(bot_logic.set_min_amount(amount))
        except:
            await update.message.reply_text("Montant invalide.")
    else:
        await update.message.reply_text("Utilisez /setamount 1.0 par exemple.")

async def check_assets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assets = bot_logic.get_profitable_assets()
    await update.message.reply_text("Actifs avec ROI > 90%:" + "\n".join(assets))

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("demo", demo))
app.add_handler(CommandHandler("real", real))
app.add_handler(CommandHandler("setamount", set_amount))
app.add_handler(CommandHandler("assets", check_assets))

if __name__ == "__main__":
    app.run_polling()
