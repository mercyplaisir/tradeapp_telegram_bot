"""

Contains handlers of the telegram button
"""
import os
import json
from typing import Callable
from dotenv import load_dotenv,find_dotenv

import requests
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext
from binance.client import Client


from resources.buttons import TlButtons
from commons.utils import order_restructure,balance_restructure

load_dotenv(find_dotenv())

URL = 'https://tradeappapiassistant.herokuapp.com/telegram'

HISTORY_ENDPOINT = '/history'
STATUS_ENDPOINT = '/status'

BINANCE_API_URL = 'https://api.binance.com'

binance_public_key = os.getenv('BINANCEPUBLICKEY')
binance_secret_key = os.getenv('BINANCEPRIVATEKEY')

client = Client(binance_public_key,binance_secret_key)

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
    # update.message.reply_text("balance")
    _data = client.get_all_coins_info(recvWindow=60000)
    data = balance_restructure(_data)
    update.message.reply_text(data)
    # return True


def send_trading_history(update: Update, context: CallbackContext):
    """Retrieve trading history from api assistant end send it to the telegrambot"""
    # update.message.reply_text('trading history')
    req = requests.get(URL + HISTORY_ENDPOINT)
    unclean_resp = json.loads(req.json())

    resp = order_restructure(unclean_resp)
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

    data:dict = requests.get(BINANCE_API_URL+f'/api/v3/ticker/price?symbol={cryptopair}').json()
    symbol,price=data.values()
    update.message.reply_text(f"Price of {symbol} is {price}")
    print("send price of ",cryptopair)

def get_coin_value(update:Update,context:CallbackContext):
    """return the value of the coin that i habe in usdt
    ex: /value BNB"""
    coin = context.args[0] #BNB
    balance = client.get_asset_balance(asset=coin,recvWindow=60000)['free']
    data:dict = requests.get(BINANCE_API_URL+f'/api/v3/ticker/price?symbol={coin}USDT').json()
    symbol,price=data.values()
    value = balance*price
    update.message.reply_text(f"value of your {coin} is {value}")
    print(f"send balance of {coin}")

message_commands = {
    TlButtons.BALANCE: send_balance,
    TlButtons.TRADING_HISTORY: send_trading_history,
    TlButtons.STATUS: send_status,
    
}
