"""

Contains handlers of the telegram button
"""
from contextvars import Context
import json
from typing import Callable

import requests
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext

from resources.buttons import TlButtons
from commons.utils import restructure

URL = 'https://tradeappapiassistant.herokuapp.com/telegram'

HISTORY_ENDPOINT = '/history'
STATUS_ENDPOINT = '/status'

BINANCE_API_URL = 'https://api.binance.com'


def start_command(update: Update, context: CallbackContext):
    """Start Command
    funcyions: .Creates Buttons"""
    # key_buttons = commands.keys()
    # buttons = [[KeyboardButton(str(button))] for button in key_buttons]
    
    buttons = [[KeyboardButton(str(button))] for button in TlButtons]


    context.bot.send_message(chat_id=update.effective_chat.id, text="""
    click:
            /crypto BNBBTC: for getting it's price""",
                             reply_markup=ReplyKeyboardMarkup(buttons))
    


def send_balance(update: Update, context: CallbackContext):
    """Retrieve balance from binance api and send it to the telegrambot"""
    update.message.reply_text("balance")
    return True


def send_trading_history(update: Update, context: CallbackContext):
    """Retrieve trading history from api assistant end send it to the telegrambot"""
    # update.message.reply_text('trading history')
    req = requests.get(URL + HISTORY_ENDPOINT)
    unclean_resp = json.loads(req.json())

    resp = restructure(unclean_resp)
    update.message.reply_text(resp)


def send_status(update: Update, context: CallbackContext):
    """Retrieve tradeapp_status from api assistant end send it to the telegrambot"""
    # update.message.reply_text('status')
    req = requests.get(URL + STATUS_ENDPOINT)
    resp = req.json()
    update.message.reply_text(resp)


def message_handler(update: Update, context: CallbackContext):
    """Message handler from telegram """
    text = update.message.text
    command: Callable = message_commands[text]
    return command(update, context)

def get_crypto_price(update:Update,context:CallbackContext):
    """return the pricce of the given crypto
    ex: /price BNBBTC"""
    cryptopair = context.args[0]
    print(cryptopair)

    data:dict = requests.get(BINANCE_API_URL+f'/api/v3/ticker/price?symbol={cryptopair}').json()
    symbol,price=data.values()
    update.message.reply_text(f"Price of {symbol} is {price}")

message_commands = {
    TlButtons.BALANCE: send_balance,
    TlButtons.TRADING_HISTORY: send_trading_history,
    TlButtons.STATUS: send_status,
    
}
