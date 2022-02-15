"""

Contains handlers of the telegram button
"""
from typing import Callable

from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext

from resources.buttons import TlButtons

import requests


URL = 'https://tradeappapiassistant.herokuapp.com/telegram'

HISTORY_ENDPOINT ='/history'
STATUS_ENDPOINT = '/status'


def start_command(update: Update, context: CallbackContext):
    """Start Command
    funcyions: .Creates Buttons"""
    key_buttons = commands.keys()

    buttons = [[KeyboardButton(button)] for button in key_buttons]
    context.bot.send_message(chat_id=update.effective_chat.id, text='welcome to tradeapp',
                             reply_markup=ReplyKeyboardMarkup(buttons))
    return True


def send_balance(update: Update, context: CallbackContext):
    update.message.reply_text("balance")
    return True


def send_trading_history(update: Update, context: CallbackContext):
    #update.message.reply_text('trading history')
    req = requests.get(URL+HISTORY_ENDPOINT)
    return req.json()


def send_status(update: Update, context: CallbackContext):
    #update.message.reply_text('status')
    req = requests.get(URL+STATUS_ENDPOINT)
    return req.json()


def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    command: Callable = commands[text]
    return command(update, context)


commands = {
    TlButtons.BALANCE: send_balance,
    TlButtons.TRADING_HISTORY: send_trading_history,
    TlButtons.STATUS: send_status
}