"""

Some useful functions
"""
from ast import Pass
import datetime
import hashlib
import hmac
import json
from typing import Dict, List, Tuple


# ORDERS_EXEMPLE:List = [
# ["BTCUSDT", "28", "-1", "6gCrw2kRUAF9CvJDGP16IP", "1507725176595", "0.00000000", "10.00000000", "10.00000000",
#     "10.00000000", "FILLED", "GTC", "MARKET", "SELL"],
#  


def order_format(order):
    if len(order) == 0:
        return ''
    cryptopair = order[0]
    time = str(datetime.datetime.fromtimestamp(int(int(order[4])/1000)))
    order_type = order[-1]

    return  f'{cryptopair} |   {time}  |   {order_type} \n '

def order_restructure(orders):
    result = ""
    for order in orders:
        result+=order_format(order)
    return result

def balance_restructure(data):
    result = ''
    items = data.items()
    for item in items:
        coin,balance = item
        result += f'{coin} : {balance} \n'
    return result



