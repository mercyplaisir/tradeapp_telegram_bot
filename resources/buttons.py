"""Contains Telegram Buttons"""
from enum import Enum


class TlButtons(Enum):
    BALANCE = 'balance'
    STATUS = 'status'
    HISTORY = 'history'

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
        TlButtons.HISTORY: 'send_trading_history',
        TlButtons.STATUS: 'send_status'
    }

    print(commands.keys())
    for i in commands.keys():
        print(i)
