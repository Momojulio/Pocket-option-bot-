
import asyncio
from telegram.ext import Application, CommandHandler # adapte selon tes fichiers
from config import BOT_TOKEN, WEBHOOK_URL

async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("amount", set_amount))
    app.add_handler(CommandHandler("mode", set_mode))

    # Démarrer le bot en mode Webhook
    await app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=BOT_TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{BOT_TOKEN}",
    )

# Lance la coroutine si on est en script principal
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
