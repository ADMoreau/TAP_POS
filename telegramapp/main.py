from telegramapp import updater
from telegramapp.class_utils import error
from telegramapp.conversations import conv_handler





def main():
    dp = updater.dispatcher

    dp.add_handler(conv_handler)

    dp.add_error_handler(error)

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
