from dotenv import load_dotenv
import os

from telegram.ext import (
    Updater, 
    Dispatcher,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler
)

from .handlers import start , conv_handler

# getting the token from .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")


updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher



def register_handlers():
    dispatcher.add_handler(handler=CommandHandler("start", start))
    dispatcher.add_handler(conv_handler)


    updater.start_polling()
    updater.idle()