from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
from resources.handlers import start_command,message_handler

TOKEN = "2097715946:AAEnO6Ce8GtgvC1Cxt4uhvV40ts2Dw3H3T0"

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher  # .dispacther

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

    print("started")
    updater.start_polling()
