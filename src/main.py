import requests

from telegram.ext import *

TOKEN = "2097715946:AAEnO6Ce8GtgvC1Cxt4uhvV40ts2Dw3H3T0"
updater = Updater(token= TOKEN,use_context=True)
dispacher = updater.dispatcher

def balance():
    pass

def status():
    pass


def trading_history():
    pass

def handle_message(update, context):
    update.message.reply_text(f"you said {update.message.text}")


dispacher.add_handler(MessageHandler(Filters.text, handle_message))
dispacher.add_handler(MessageHandler(Filters.text, trading_history))
dispacher.add_handler(MessageHandler(Filters.text, status))
dispacher.add_handler(MessageHandler(Filters.text, balance))


updater.start_polling()
