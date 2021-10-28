from telegram import *
from telegram.ext import *

with open("./token.txt","r") as f:
    token=f.read()

updater = Updater(token=token)
dispacher= updater.dispacther

updater.start_polling()
