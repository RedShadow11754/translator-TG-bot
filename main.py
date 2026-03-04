from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio
import os
import dotenv
from translate import TranslatorBot
import time


dotenv.load_dotenv()
API_KEY = os.getenv('TOKEN')
user_name = os.getenv('BOT_USERNAME')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Thanks for using Translator Bot!")


async def handle_response(text):
    data = {
        "text": text,
        "target_language": "am"
    }
    bot = TranslatorBot(data)

    return await bot.translate()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text
    if message_type == 'group':
        if user_name in text:
            new_text = text.replace(user_name, "").strip()
            response = await handle_response(new_text)
        else:
            return
    else:
        now = time.time()
        response = await handle_response(text)
        the = time.time()
        print(the - now)
    print(f"Response: {response}")
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

if __name__ == '__main__':
    print("Strating... ")
    app = Application.builder().token(API_KEY).build()
    app.add_handler(CommandHandler('start', start_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)
    print("Polling...")
    app.run_polling(poll_interval=0.1)