from pathlib import Path

from telegram.ext import *

THISFOLDER = Path(__file__).resolve().parent
TOKENFOLDER = f"{THISFOLDER}/token.txt"

# with open(TOKENFOLDER, "r") as f:
#     toke = str(f.read())
# print(toke)
updater = Updater(token="2097715946:AAEnO6Ce8GtgvC1Cxt4uhvV40ts2Dw3H3T0",use_context=True)
dispacher = updater.dispatcher


def handle_message(update, context):
    update.message.reply_text(f"you said {update.message.text}")


dispacher.add_handler(MessageHandler(Filters.text, handle_message))

updater.start_polling()
