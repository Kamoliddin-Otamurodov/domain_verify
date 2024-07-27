from dotenv import load_dotenv
import os
from telegram import Bot


load_dotenv()
TOKEN = os.environ.get('TOKEN')
URL = os.environ.get('URL')

bot = Bot(TOKEN)

def info():
    print(bot.get_webhook_info())

def delete():
    print(bot.delete_webhook())

def set():
    print(bot.set_webhook(url=URL))

info()