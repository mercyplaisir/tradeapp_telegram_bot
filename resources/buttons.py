"""Contains Telegram Buttons"""
import json
from enum import Enum


class TlButtons(Enum):
    """TELEGRAM Buttons"""
    BALANCE = 'balance'
    STATUS = 'status'
    TRADING_HISTORY = 'trading history'
    ALL = 'all infos'
    ERROR = 'erreur'
    PROFIT = 'profit'

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other

    def __hash__(self):
        return hash(self.value)



if __name__ == '__main__':
    commands = {
        TlButtons.BALANCE: 'send_balance',
        TlButtons.TRADING_HISTORY: 'send_trading_history',
        TlButtons.STATUS: 'send_status'
    }
   

    nn = [json.dumps(str(n)) for n in commands.keys()]
    print(nn)
