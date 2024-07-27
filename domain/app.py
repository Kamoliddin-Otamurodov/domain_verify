from dotenv import load_dotenv
import os
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler , MessageHandler , Filters
import handlers
from flask import Flask , request
import requests


load_dotenv()
TOKEN = os.environ.get('TOKEN')
URL = os.environ.get('URL')

bot = Bot(TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)
app = Flask(__name__)


@app.route('/domain_verify', methods=['GET', 'POST'])
def random_dog():
    if request.method == 'GET':
        return '<h1>Domain Verify is working...!</h1>'

    if request.method == 'POST':
        body = request.get_json()
        
        updater = Update.de_json(body, bot)

        dispatcher.add_handler(handler=CommandHandler("start", handlers.start))
        dispatcher.add_handler(handlers.conv_handler)

        updater.start_polling()
        updater.idle()

        return {'message': 'ok'}


if __name__ == '__main__':
    app.run(debug=True)