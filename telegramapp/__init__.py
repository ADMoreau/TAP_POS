from telegram.ext import Updater

from telegramapp.secrets import TOKEN

updater = Updater(TOKEN, use_context=True)
