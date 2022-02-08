from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import CommandHandler, Updater, CallbackContext, MessageHandler, Filters

TOKEN = "2097715946:AAEnO6Ce8GtgvC1Cxt4uhvV40ts2Dw3H3T0"
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# TOKENFOLDER = f"./token.txt"
#
# with open(TOKENFOLDER, "r") as f:
#     token = json.load(f)

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher  # .dispacther
key_buttons = ['balance', 'trading history', 'status']


def start_command(update: Update, context: CallbackContext):
    """Start Command
    funcyions: .Creates Buttons"""
    global key_buttons

    buttons = [[KeyboardButton(button)] for button in key_buttons]
    context.bot.send_message(chat_id=update.effective_chat.id, text='welcome to tradeapp',
                             reply_markup=ReplyKeyboardMarkup(buttons))


def send_balance(update: Update, context: CallbackContext):
    update.message.reply_text("balance")


def send_trading_history(update: Update, context: CallbackContext):
    update.message.reply_text('trading history')


def send_status(update: Update, context: CallbackContext):
    update.message.reply_text('status')


def message_handler(update: Update, context: CallbackContext):
    text = update.message.text

    if text == 'balance':
        send_balance(update, context)
    elif text == 'trading history':
        send_trading_history(update, context)
    elif text == 'status':
        send_status(update, context)


def main():
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

    print("started")
    updater.start_polling()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
