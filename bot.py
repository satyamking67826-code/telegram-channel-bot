import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"Namaste! Aapka Telegram Bot chal raha hai."
)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"Yeh aapka Telegram Channel Bot hai."
)

def main():
token = os.environ.get("BOT_TOKEN")

if not token:
    raise RuntimeError("BOT_TOKEN set nahi hai.")

app = Application.builder().token(token).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

print("Telegram Bot started!")
app.run_polling()

if __name__ == "__main__":
main()
